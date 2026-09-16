# Find bugs

## Purpose

Analyze code for actionable logic errors, broken edge cases, and security defects, distinguishing supported findings from hypotheses and proposing targeted changes.

## Compatibility and requirements

AI assistants capable of analyzing code through text instructions. Requires the code to review; include the language, version, and expected behavior when they are not obvious.

## Usage

For an evidence-based investigation with reproduction and verification of requested fixes, use the [Debug code skill](../skills/debug-code/SKILL.md).

Replace `[PASTE YOUR CODE]` with the code you want to analyze and copy the following prompt into the assistant.

## Prompt

```text
Act as a senior developer specializing in debugging.

Analyze this code and find:
- logic errors
- potential bugs
- edge cases
- security issues

Do not rewrite everything.

For each finding, explain the triggering conditions, expected versus actual
behavior, and evidence for the root cause. Distinguish reproduced defects,
defects supported by code inspection, and unconfirmed hypotheses.
For hypotheses, state the missing context or check needed to confirm them.
Do not claim to have run the code unless you actually did.

Show only the changes needed for supported defects. Keep style preferences
and unused code out of the bug list unless they cause incorrect behavior.
If no actionable defect is established, say so without inventing findings.

Code:
[PASTE YOUR CODE]
```

## Expected output

Findings with triggering conditions, evidence status, and root-cause explanations, followed by focused proposed corrections for supported defects. State remaining uncertainty and any checks still needed; generated changes are not verified fixes unless they have been tested.

[Back to catalog](README.md)
