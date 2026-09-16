# Improve performance

## Purpose

Identify performance problems in code, rank them by impact, and propose simple optimizations with targeted changes.

## Compatibility and requirements

AI assistants capable of analyzing code through text instructions. Requires the code to optimize. Include the language, framework, data volume, and available measurements to put the impact of the problems in context.

## Usage

Replace `[PASTE YOUR CODE]` with the code you want to analyze and copy the following prompt into the assistant along with the relevant context.

## Prompt

```text
Analyze this code for performance problems.

Pay particular attention to:
- repeated operations
- unnecessary queries
- expensive loops
- unnecessary renders
- duplicate calls
- memory usage
- unnecessary complexity

Rank the problems by impact:
HIGH / MEDIUM / LOW.

Then propose the simplest possible optimization and show
only the code you would change.

Code:
[PASTE YOUR CODE]
```

## Expected output

A list of problems classified as HIGH, MEDIUM, or LOW impact, followed by the simplest possible optimization and only the code that would change. Verify improvements with comparable measurements before and after, and check that the expected behavior is preserved.

[Back to catalog](README.md)
