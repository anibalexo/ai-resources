# Generate tests

## Purpose

Generate tests for a function covering expected behavior, invalid inputs, empty values, boundaries, expected errors, and unusual cases.

## Compatibility and requirements

AI assistants capable of analyzing code and generating tests through text instructions. Requires the function to test and the testing framework used. Include the expected behavior, dependencies, and the project's test configuration.

## Usage

For a repository-based workflow that identifies the behavioral contract and runs the resulting tests, use the [Generate tests skill](../skills/generate-tests/SKILL.md).

Replace `[TESTING FRAMEWORK]` with the project's testing framework and `[PASTE THE FUNCTION]` with the function you want to test. Copy the following prompt into the assistant along with the relevant context.

## Prompt

```text
Analyze this function as if you were responsible
for QA and development.

Generate tests for:
- expected behavior
- invalid inputs
- empty values
- boundaries
- expected errors
- unusual cases

Use:
[TESTING FRAMEWORK]

For each test, specify:
1. what we are testing
2. expected result
3. test code

Code:
[PASTE THE FUNCTION]
```

## Expected output

A set of tests with an explanation of what each one checks, its expected result, and the test code in the specified framework. Review the expectations and run the tests in the project to verify that they work.

[Back to catalog](README.md)
