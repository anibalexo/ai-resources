# Git Conventions

Reusable conventions for commit formatting, branch naming, and repository hygiene across software projects.

## Purpose and scope

Applies to version-controlled repositories using Git. Use these rules to maintain a readable, bisectable git history and prevent accidental leakage of sensitive files or build artifacts.

## Compatible tools and installation

Compatible with Codex, Claude Code, Cursor, GitHub Copilot, and Antigravity.
- For project-level adoption, install into `.agents/rules/git-conventions.md`, `.cursorrules`, or link directly from the project's `AGENTS.md` or `CONTRIBUTING.md`.

## Rules and conventions

### 1. Conventional commit format
Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```text
<type>(<optional scope>): <short description in present tense>

[optional body explaining motivation and breaking changes]

[optional footer(s) referencing issue IDs]
```

- **Standard types:**
  - `feat`: A new feature or capability.
  - `fix`: A bug fix or defect correction.
  - `refactor`: Code change that neither fixes a bug nor adds a feature.
  - `test`: Adding missing tests or correcting existing tests.
  - `docs`: Documentation changes only.
  - `perf`: Code change that improves performance.
  - `chore`: Maintenance tasks, dependencies, tooling, or repository configuration.
- **Description guidelines:**
  - Use the imperative present tense ("add feature", not "added" or "adds").
  - Do not capitalize the first letter of the description.
  - Do not place a period at the end of the subject line.

### 2. Branch naming convention
Use lowercase kebab-case prefixed with the category:
- `feature/<feature-name>` or `feat/<feature-name>`
- `bugfix/<ticket-id>-<defect>` or `fix/<defect>`
- `hotfix/<critical-patch>`
- `refactor/<target-area>`

### 3. Atomic commits and minimal diffs
- Commit cohesive, single-purpose changes. Avoid bundling unrelated fixes, formatting changes, and new features into a single commit.
- Never stage or commit commented-out dead code or temporary debugging statements (e.g., `console.log`, `print()`, `breakpoint()`).

### 4. Repository hygiene and secret prevention
- Never commit environment files (`.env`, `.env.local`), database files (`*.sqlite3`), or credentials.
- Ensure `.gitignore` ignores local virtual environments (`.venv/`, `env/`), bytecode caches (`__pycache__/`, `*.pyc`), and editor directories (`.idea/`, `.vscode/settings.json` with personal preferences).

## Examples

### Good commit messages
- `feat(auth): add google oauth2 login endpoint`
- `fix(orders): handle race condition during stock reservation`
- `refactor(billing): extract stripe client into dedicated service module`
- `test(users): add unit tests for password reset token expiration`

### Bad commit messages
- `fixes` (vague, lacks context)
- `WIP` (unfinished changes without purpose)
- `Update models.py and views.py` (describes files touched rather than intent)
- `Fixed bug with user login and cleaned up css` (combines unrelated changes)
