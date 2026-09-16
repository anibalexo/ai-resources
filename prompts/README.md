# Prompts

Reusable instructions for specific tasks, such as reviewing changes, analyzing requirements, or writing documentation.

## Organization

Save each prompt in a Markdown file with a descriptive name, such as `review-changes.md`. Use a separate folder when it needs examples or supporting files.

## What to document

- Purpose and situations in which it is useful.
- Compatible tools and required context.
- Variables the user must replace.
- Full prompt text and expected output format.

## Usage

Read the requirements, replace the variables, and paste the prompt into a compatible assistant along with the specified context. Review the output before incorporating it into the project.

## Catalog

- [Find bugs](find-bugs.md): identifies problems, explains their causes, and proposes only the necessary changes.
- [Add a feature](add-feature.md): analyzes the logic, affected files, data flow, and edge cases before implementing step by step.
- [Refactor code](refactor-code.md): improves clarity and maintainability while preserving behavior and explains the changes made.
- [Review architecture](review-architecture.md): proposes a simple, scalable architecture for a feature before writing code.
- [Generate tests](generate-tests.md): generates tests for expected behavior and edge cases, with an explanation and expected result for each test.
- [Improve performance](improve-performance.md): ranks problems by impact and proposes simple optimizations, showing only the code that would change.

[Back to index](../README.md)
