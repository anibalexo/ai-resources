# Security and Data Protection

Reusable rules and defensive standards for preventing vulnerabilities, data leakage, and unauthorized access.

## Purpose and scope

Applies to all application code, configuration files, and automated scripts. Use these rules to ensure software operates within secure boundaries and prevents common vulnerabilities (such as OWASP Top 10 risks).

## Compatible tools and installation

Compatible with Codex, Claude Code, Cursor, GitHub Copilot, and Antigravity.
- For project-level adoption, install into `.agents/rules/security.md`, `.cursorrules`, or link directly from the project's `AGENTS.md`.

## Rules and conventions

### 1. Zero hardcoded credentials
- Never store secrets, passwords, API tokens, webhook secrets, encryption keys, or certificates directly in source code, commit history, or test fixtures.
- Retrieve all sensitive configurations from environment variables or dedicated secret managers at runtime.
- Verify that secret files (e.g., `.env`, `.env.production`, `*.pem`, `*.key`) are included in `.gitignore` before writing code.

### 2. Injection prevention
- **SQL / ORM:** Always use parameterized queries or trusted ORM methods. Never construct queries via string concatenation or format strings with untrusted inputs.
- **Commands / Shell:** Avoid passing user input to system shell execution commands (`os.system`, `subprocess` with `shell=True`, `exec`). When invoking subprocesses, pass arguments as explicit lists with `shell=False`.
- **Output escaping:** Ensure outputs rendered into HTML, XML, or markdown contexts are automatically escaped to prevent Cross-Site Scripting (XSS).

### 3. Sensitive data handling and logging hygiene
- Never log Personally Identifiable Information (PII) such as plaintext passwords, credit card numbers, authorization headers, authentication tokens, or personal identifiers.
- Filter or sanitize sensitive fields from request payloads before outputting error traces or logging debug dumps.

### 4. Explicit authorization and access control
- Enforce authentication and permission checks on every backend endpoint or service method. Never rely on frontend UI hiding as a security control.
- Validate object ownership (prevent Insecure Direct Object References / IDOR): ensure the authenticated user owns or has explicit permission to access the requested resource ID.

### 5. Input validation and boundary enforcement
- Validate all incoming data (payloads, headers, query parameters, file uploads) against strict schemas or typed validators before passing them into internal domain layers.
- Restrict file upload extensions, validate content types, and store uploaded files outside web-accessible execution paths.

## Examples

### Good (Parameterized and secure)

```python
# Safe database query using parameterized input
def get_user_profile(user_id: int) -> User | None:
    return User.objects.filter(id=user_id, is_active=True).first()

# Safe subprocess execution
import subprocess
def convert_document(source_path: str, target_path: str) -> None:
    # Arguments passed as a list, shell=False
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", source_path, target_path], check=True)
```

### Bad (Vulnerable to injection)

```python
# CRITICAL: Vulnerable to SQL injection!
def get_user_profile_insecure(user_id: str):
    query = f"SELECT * FROM users WHERE id = '{user_id}' AND is_active = 1"
    cursor.execute(query)

# CRITICAL: Vulnerable to shell injection!
import os
def convert_document_insecure(source_path: str):
    os.system(f"soffice --headless --convert-to pdf {source_path}")
```
