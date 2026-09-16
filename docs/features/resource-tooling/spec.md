# Resource tooling

Status: implementation scope requested by the repository owner.

## Objective and scope

Make this resource repository easier to adopt and maintain through a project installer, a resource validator, a worked documentation example, a bug-fixing workflow, and continuous validation. No plugin packaging, production deployment, or automatic updates to other projects are included.

## Acceptance criteria

- AC-01: A PowerShell entry point installs selected skills and workflows into an existing target project's `.agents/` directory. Selected workflows bring their linked skill dependencies. A preview performs no writes.
- AC-02: Installation adapts Markdown links, records source revision and installed file hashes, and provides suggested project instructions without editing the project's `AGENTS.md`.
- AC-03: Conflicting unmanaged or locally modified files stop installation before writes. Explicit updates may replace only unchanged managed files. Invalid selections and symbolic-link destinations are rejected. Repeated installation is safe.
- AC-04: A dependency-free Python validator checks skill metadata, resource names, local Markdown links and heading fragments, and known skill invocations. It reports actionable failures and returns a nonzero exit status.
- AC-05: A worked example connects requirements, technical planning, tasks, and usage documentation without presenting fictional implementation or test results as real.
- AC-06: A bug-fixing workflow covers reproduction, diagnosis, regression tests, focused correction, verification, and failure recovery using existing skills.
- AC-07: GitHub Actions runs validation and automation tests on pushes and pull requests. The installer is exercised on temporary sample projects, including its PowerShell entry point on Windows.

## Constraints and verification

Scripts use Python 3.10+ and the standard library. The PowerShell wrapper supports PowerShell 5.1+ and calls Python; it does not change execution policy or install dependencies. Source documentation remains in English. Existing project content and customizations are preserved.

Verify with `python scripts/validate-resources.py` and `python -m unittest discover -s scripts/tests -v`. Run the PowerShell entry point against a temporary project. CI execution on GitHub remains unverified until the workflow actually runs there.
