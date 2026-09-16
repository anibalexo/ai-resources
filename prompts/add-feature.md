# Add a feature

## Purpose

Plan and implement a feature by first defining the logic, affected files, data flow, and edge cases.

## Compatibility and requirements

AI assistants capable of analyzing and generating code through text instructions. Requires a description of the feature and the project's stack. Also provide the code or access to relevant files and the versions used so the assistant can identify the necessary changes.

## Usage

Replace `[DESCRIBE THE FEATURE]` with the feature's requirements and `[FRAMEWORK + LANGUAGE + DATABASE]` with the project's stack. Copy the following prompt into the assistant along with the context of the existing code.

## Prompt

```text
I need to implement this feature:

[DESCRIBE THE FEATURE]

Stack:
[FRAMEWORK + LANGUAGE + DATABASE]

Before writing code:
1. define the necessary logic
2. identify the files that need to be modified
3. explain the data flow
4. identify potential edge cases

Then generate the implementation step by step.

Do not invent APIs, libraries, or functions that do not exist.
```

## Expected output

An initial analysis of the logic, affected files, data flow, and edge cases, followed by a step-by-step implementation using existing APIs, libraries, and functions.

[Back to catalog](README.md)
