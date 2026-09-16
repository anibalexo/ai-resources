# Review architecture

## Purpose

Define a simple, scalable architecture for a feature before writing code, avoiding overengineering.

## Compatibility and requirements

AI assistants capable of analyzing requirements and proposing software architectures through text instructions. Requires the feature description and the stack used. For existing projects, include the current structure, integrations, and relevant constraints.

## Usage

Replace `[DESCRIPTION]` with the feature's requirements and `[STACK]` with the project's technologies. Copy the following prompt into the assistant along with the relevant context.

## Prompt

```text
I want to build this feature:

[DESCRIPTION]

My stack is:
[STACK]

Design a simple, scalable architecture.

Specify:
- necessary components or modules
- responsibilities of each one
- folder structure
- data flow
- necessary endpoints
- data model
- validations
- error handling

Avoid overengineering.

Do not write code yet.
```

## Expected output

An architecture proposal without code detailing the components, their responsibilities, folder structure, data flow, endpoints, data model, validations, and error handling.

[Back to catalog](README.md)
