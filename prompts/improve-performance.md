# Improve performance

## Purpose

Identify potential performance bottlenecks, distinguish measurements from hypotheses, and propose simple optimizations with targeted changes and a verification approach.

## Compatibility and requirements

AI assistants capable of analyzing code through text instructions. Requires the code to optimize. Include the language, framework, data volume, and available measurements to put the impact of the problems in context.

## Usage

For a repository-based workflow with baseline measurements and verification, use the [Optimize performance skill](../skills/optimize-performance/SKILL.md).

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

Separate bottlenecks supported by supplied measurements from suspected ones.
Explain the evidence and relevant workload for each finding.
Rank expected impact as HIGH / MEDIUM / LOW and explain the ranking.
When measurements are missing, label the ranking provisional and state what
to measure. Do not invent speedups or treat a loop or query as a bottleneck
without explaining why it matters for the workload.

Then propose the simplest possible optimization and show
only the code you would change.
Preserve behavior and describe how to compare before and after under the
same conditions. Do not claim an improvement was measured unless it was.
If no useful optimization is supported, say so.

Code:
[PASTE YOUR CODE]
```

## Expected output

Findings with measured or suspected status, justified impact rankings marked provisional when needed, and focused proposed optimizations. Include comparable before-and-after measurement steps and behavior checks. Distinguish actual results from verification that remains to be performed.

[Back to catalog](README.md)
