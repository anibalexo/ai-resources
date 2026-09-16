# Resource tooling implementation plan

See the [specification](spec.md) for scope and acceptance criteria.

| Resource | Change and verification |
| --- | --- |
| `scripts/install-resources.ps1` and `scripts/install-resources.py` | PowerShell entry point and portable installation engine; temporary-project tests for AC-01 through AC-03 |
| `scripts/validate-resources.py` | Read-only validation with actionable errors; positive and negative fixtures for AC-04 |
| `scripts/tests/` | Standard-library tests for dry runs, conflict preservation, updates, links, and invalid resources |
| `docs/examples/order-history/` | Linked fictional specification, plan, tasks, and usage example for AC-05 |
| `workflows/fix-bug.md` | Reuse debugging and test-generation guidance for AC-06 |
| `.github/workflows/validate.yml` | Linux and Windows validation and tests for AC-07 |
| Resource catalogs and root README | Discoverable commands, requirements, examples, and links |

Implement the validator and installer before documenting their exact commands, then exercise sample projects and connect CI. Use managed-file hashes to distinguish safe updates from local customizations. Preflight every destination before writing. Keep installation support material under `.agents/` and leave the target project's docs and AGENTS.md untouched. Omitted optional links become labeled text rather than dangling links.

No database or application-model changes. No automatic removal of old installations: the manifest records ownership and updates, while deleting obsolete files remains an explicit manual action. Filesystem failures can leave a partial installation; unchanged unmanaged files with identical contents can be adopted on retry. Conflicts are detected before writes, but this is not a transactional filesystem operation.
