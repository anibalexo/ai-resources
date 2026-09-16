import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]


def load(filename):
    spec = importlib.util.spec_from_file_location(filename.replace('-', '_'), ROOT / 'scripts' / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


installer = load('install-resources.py')
validator = load('validate-resources.py')


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='ai-resources-test-')
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name)
        self.target = self.base / 'project with spaces'
        self.target.mkdir()
        self.source = self.base / 'source'
        self.source.mkdir()
        for folder in ['skills', 'workflows', 'docs']:
            shutil.copytree(ROOT / folder, self.source / folder)

    def run_install(self, **kwargs):
        with contextlib.redirect_stdout(io.StringIO()):
            installer.install(self.source, self.target, **kwargs)

    def test_dry_run_has_no_side_effects(self):
        self.run_install(workflows=['plan-feature'], dry_run=True)
        self.assertEqual(list(self.target.iterdir()), [])

    def test_full_install_links_manifest_and_existing_instructions(self):
        instructions = self.target / 'AGENTS.md'
        instructions.write_text('Keep my instructions.\n')
        self.run_install()
        self.assertEqual(instructions.read_text(), 'Keep my instructions.\n')
        self.assertEqual(validator.validate(self.target), [])
        manifest = json.loads((self.target / installer.MANIFEST).read_text())
        for relative, record in manifest['files'].items():
            self.assertEqual(installer.digest((self.target / relative).read_bytes()), record['sha256'])
        self.assertTrue((self.target / '.agents/workflows/fix-bug.md').exists())
        self.run_install()  # Repetition must not conflict.

    def test_workflow_selection_installs_dependencies_only(self):
        self.run_install(workflows=['plan-feature'])
        installed = self.target / '.agents/skills'
        self.assertTrue((installed / 'specify-feature/SKILL.md').exists())
        self.assertTrue((installed / 'plan-implementation/SKILL.md').exists())
        self.assertFalse((installed / 'debug-code').exists())
        self.assertFalse((self.target / '.agents/workflows/implement-feature.md').exists())
        self.assertEqual(validator.validate(self.target), [])

    def test_conflict_preflight_preserves_all_files(self):
        conflict = self.target / '.agents/skills/debug-code/SKILL.md'
        conflict.parent.mkdir(parents=True)
        conflict.write_text('My customized skill.\n')
        with self.assertRaisesRegex(ValueError, 'No files written'):
            self.run_install()
        self.assertEqual(conflict.read_text(), 'My customized skill.\n')
        self.assertFalse((self.target / installer.MANIFEST).exists())
        self.assertFalse((self.target / '.agents/workflows').exists())

    def test_update_requires_flag_and_preserves_customizations(self):
        self.run_install(skills=['debug-code'])
        source_skill = self.source / 'skills/debug-code/SKILL.md'
        source_skill.write_text(source_skill.read_text() + '\nNew upstream instruction.\n')
        with self.assertRaises(ValueError):
            self.run_install(skills=['debug-code'])
        self.run_install(skills=['debug-code'], update=True)
        target_skill = self.target / '.agents/skills/debug-code/SKILL.md'
        self.assertIn('New upstream instruction.', target_skill.read_text())
        target_skill.write_text(target_skill.read_text() + '\nLocal customization.\n')
        with self.assertRaises(ValueError):
            self.run_install(skills=['debug-code'], update=True)
        self.assertIn('Local customization.', target_skill.read_text())

    def test_invalid_selection_cannot_escape_target(self):
        with self.assertRaises(ValueError):
            self.run_install(skills=['../outside'])
        self.assertEqual(list(self.target.iterdir()), [])

    def test_file_as_parent_is_rejected_before_writes(self):
        (self.target / '.agents').write_text('Not a directory.')
        with self.assertRaisesRegex(ValueError, 'not a directory'):
            self.run_install()
        self.assertEqual((self.target / '.agents').read_text(), 'Not a directory.')

    def test_incremental_selection_retains_previous_catalog(self):
        self.run_install(skills=['debug-code'])
        self.run_install(skills=['generate-tests'], update=True)
        catalog = (self.target / '.agents/skills/ai-resources.md').read_text()
        self.assertIn('debug-code', catalog)
        self.assertIn('generate-tests', catalog)
        self.assertEqual(validator.validate(self.target), [])

    def test_symlink_destination_is_rejected(self):
        outside = self.base / 'outside'
        outside.mkdir()
        try:
            (self.target / '.agents').symlink_to(outside, target_is_directory=True)
        except OSError:
            self.skipTest('Creating symlinks requires privileges on this platform.')
        with self.assertRaisesRegex(ValueError, 'Symbolic'):
            self.run_install()
        self.assertEqual(list(outside.iterdir()), [])

    @unittest.skipUnless(os.name == 'nt', 'PowerShell entry point is exercised on Windows.')
    def test_powershell_preview_and_install(self):
        command = ['powershell.exe', '-NoProfile', '-File', str(ROOT / 'scripts/install-resources.ps1'),
                   '-TargetPath', str(self.target), '-Workflows', 'plan-feature', '-Python', sys.executable]
        result = subprocess.run(command + ['-WhatIf'], capture_output=True, text=True)
        if result.returncode and 'running scripts is disabled' in result.stderr and not os.environ.get('CI'):
            self.skipTest('Host execution policy blocks PowerShell scripts; use the Python entry point. CI must exercise the wrapper.')
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(list(self.target.iterdir()), [])
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertTrue((self.target / '.agents/workflows/plan-feature.md').is_file())


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix='ai-validator-test-')
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.skill = self.root / 'skills/sample-skill/SKILL.md'
        self.skill.parent.mkdir(parents=True)
        self.skill.write_text('---\nname: sample-skill\ndescription: A valid example.\n---\n# Sample\n', encoding='utf-8')

    def test_repository_is_valid(self):
        self.assertEqual(validator.validate(ROOT), [])

    def test_metadata_and_stale_invocation(self):
        self.skill.write_text('---\nname: wrong-name\ndescription: Example.\n---\nUse $removed-skill.\n')
        errors = '\n'.join(validator.validate(self.root))
        self.assertIn('name must match', errors)
        self.assertIn('unknown local skill', errors)

    def test_missing_metadata_fails(self):
        self.skill.write_text('# Missing frontmatter\n')
        self.assertIn('missing YAML frontmatter', '\n'.join(validator.validate(self.root)))

    def test_validator_cli_returns_failure(self):
        (self.root / 'README.md').write_text('[Broken](deleted.md)\n')
        result = subprocess.run([sys.executable, str(ROOT / 'scripts/validate-resources.py'), '--root', str(self.root)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn('deleted.md', result.stderr)

    def test_links_fragments_and_reference_definitions(self):
        (self.root / 'README.md').write_text('[Good](skills/sample-skill/SKILL.md#sample)\n[Bad](missing.md)\n[Anchor](skills/sample-skill/SKILL.md#missing)\n[Reference][gone]\n')
        errors = validator.validate(self.root)
        self.assertEqual(len(errors), 3, errors)

    def test_fenced_examples_are_not_links(self):
        (self.root / 'README.md').write_text('```markdown\n[Example](nonexistent.md)\n```\n')
        self.assertEqual(validator.validate(self.root), [])

    def test_duplicate_heading_and_folded_scalar(self):
        self.skill.write_text('---\nname: sample-skill\ndescription: >\n  A folded\n  description.\n---\n# Sample\n# Sample\n')
        (self.root / 'README.md').write_text('[Second](skills/sample-skill/SKILL.md#sample-1)\n')
        self.assertEqual(validator.validate(self.root), [])


if __name__ == '__main__':
    unittest.main()
