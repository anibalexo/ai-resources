# Prompts

Portable prompts for focused code reviews, refactoring, test generation, and performance analysis. Copy them into an assistant with the relevant code and context; no skill installation is required.

## Organization

Save each prompt in a Markdown file with a descriptive name, such as `review-changes.md`. Use a separate folder when it needs examples or supporting files.

## What to document

- Purpose and situations in which it is useful.
- Compatible tools and required context.
- Variables the user must replace.
- Full prompt text and expected output format.

## Usage

Read the requirements, replace the variables, and paste the prompt into a compatible assistant along with the specified context. Review the output before incorporating it into the project.

These prompts are short alternatives for working with supplied snippets, including in assistants without skill support. For repository-based investigation, execution, and verification, prefer the corresponding [skills](../skills/README.md) when available.

For feature specification and technical design, use [Plan a feature](../workflows/plan-feature.md). For implementation and verification, use [Implement a feature](../workflows/implement-feature.md). Keep these broader procedures in workflows rather than duplicating them as prompts.

## Catalog

- [Find bugs](find-bugs.md): separates supported defects from hypotheses, explains their causes, and proposes focused corrections.
- [Refactor code](refactor-code.md): improves clarity and maintainability while preserving behavior and explains the changes made.
- [Generate tests](generate-tests.md): generates tests for expected behavior and edge cases, with an explanation and expected result for each test.
- [Improve performance](improve-performance.md): distinguishes measured bottlenecks from suspected ones, explains estimated impact, and proposes focused optimizations.

[Back to index](../README.md)
