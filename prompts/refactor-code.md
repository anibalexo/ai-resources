# Refactor code

## Purpose

Improve code readability and maintainability while preserving its exact behavior and avoiding unnecessary changes.

## Compatibility and requirements

AI assistants capable of analyzing and generating code through text instructions. Requires the code to refactor and the language or framework used. Include versions, dependencies, and existing tests to help verify behavior.

## Usage

Replace `[LANGUAGE/FRAMEWORK]` with the project's technology and `[PASTE YOUR CODE]` with the code you want to refactor. Copy the following prompt into the assistant along with the relevant context.

## Prompt

```text
Refactor this code while preserving exactly
the same behavior.

Prioritize:
- readability
- maintainability
- clear names
- separation of concerns
- eliminating duplication
- best practices for [LANGUAGE/FRAMEWORK]

Do not make unnecessary changes.

At the end, explain:
- what you changed
- why
- what improved

Code:
[PASTE YOUR CODE]
```

## Expected output

Refactored code that preserves the original behavior, followed by an explanation of the changes, their rationale, and the resulting improvements. Verify behavioral equivalence with the project's tests before incorporating the result.

[Back to catalog](README.md)
