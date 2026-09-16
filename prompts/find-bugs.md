# Find bugs

## Purpose

Analyze code to identify logic errors, potential bugs, edge cases, security issues, and unnecessary code, with explanations and targeted changes.

## Compatibility and requirements

AI assistants capable of analyzing code through text instructions. Requires the code to review; include the language, version, and expected behavior when they are not obvious.

## Usage

For an evidence-based investigation with reproduction and verification of requested fixes, use the [Find bugs skill](../skills/find-bugs/SKILL.md).

Replace `[PASTE YOUR CODE]` with the code you want to analyze and copy the following prompt into the assistant.

## Prompt

```text
Act as a senior developer specializing
in debugging.

Analyze this code and find:
- logic errors
- potential bugs
- edge cases
- security issues
- unnecessary code

Do not rewrite everything.

First explain the exact cause of each problem,
then show me only the necessary changes.

Code:
[PASTE YOUR CODE]
```

## Expected output

An explanation of the cause of each identified problem, followed only by the changes needed to fix it.

[Back to catalog](README.md)
