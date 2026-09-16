---
name: improve-performance
description: Diagnose code performance bottlenecks and verify targeted optimizations with comparable measurements. Use for slow requests, excessive database queries, repeated work or renders, high memory usage, and explicit performance reviews. Not for general refactoring or feature implementation without a performance objective.
---

# Improve performance

Find the work responsible for a performance problem, make the smallest useful optimization within the requested scope, and report evidence of its effect while preserving behavior.

## Context and scope

Use the code, callers, configuration, and existing profiling or test tools to identify the relevant execution path. Establish the symptom, representative workload, and metric: latency, throughput, query count, render duration, or memory usage. Ask only for missing information that materially affects the diagnosis; label assumptions when proceeding with a local example.

Respect the requested mode. A review produces findings and proposed changes; a request to optimize code permits implementation within that scope. Do not turn a review into edits or broaden an optimization into an architectural rewrite. With pasted code or no runnable environment, perform static analysis and provide a concrete measurement plan without claiming a measured improvement.

## Establish a baseline

- Prefer existing benchmarks, profilers, query logs, and project commands. Add a small reproducible benchmark only when existing tools cannot measure the relevant behavior and the benefit justifies keeping it.
- Record the command or procedure, workload size, relevant environment, and baseline metric with units. Use representative data and identify synthetic workloads explicitly.
- Separate setup from the measured operation. Account for warm-up, caches, and runtime compilation where relevant. Repeat noisy measurements and summarize their variation; use enough samples before reporting percentiles.
- Run before and after under comparable conditions: same input, configuration, concurrency, and measurement method. Do not use shared or production systems for load tests without authorization.

## Diagnose and prioritize

Trace the costly path rather than treating every loop, query, or render as a problem. Inspect only the mechanisms relevant to the symptom, such as:

- Repeated computation or calls: check frequency, input reuse, and whether repeated work is required for correctness.
- Database access: inspect query counts, fetched data, N+1 patterns, and available query plans before proposing batching or indexes.
- Rendering: check measured render cost and update frequency before adding memoization.
- Memory: distinguish transient allocations, peak usage, and retained objects before asserting a leak.
- Algorithms and I/O: relate complexity, serialization, round trips, and concurrency to realistic workload sizes.

For each actionable finding, identify the location, mechanism, evidence, and simplest proposed change. Separate **measured bottlenecks** from **suspected bottlenecks**. Rank expected impact as HIGH, MEDIUM, or LOW relative to the user's workload and objective, explain the ranking, and mark it provisional when measurements are missing. Do not invent speedups or infer end-to-end gains from an isolated microbenchmark.

## Optimize and verify

Start with the best-supported bottleneck. Prefer a focused change over several speculative optimizations so its effect can be attributed. Preserve output, ordering, errors, side effects, and relevant concurrency behavior.

Consider the tradeoffs of the proposed mechanism: cache invalidation and memory growth, batching and transaction semantics, concurrency and resource limits, or indexes and write overhead. Avoid introducing a new dependency or infrastructure component when a local change meets the objective.

Run the relevant existing correctness checks and repeat the baseline measurement. Add a regression test when the optimization creates a meaningful behavioral risk that existing tests do not cover. Treat differences within measurement noise as inconclusive. If a candidate regresses performance or provides no useful gain, revise or revert only your own candidate changes, preserving unrelated work.

Stop when the requested objective is met or further progress requires missing access, data, or a broader change. Report the limiting factor and next useful measurement instead of expanding scope. If verification cannot run, state precisely what remains unverified.

## Deliverable

Keep the response proportional to the task. Include:

- Prioritized findings with code locations, evidence, and measured or suspected status.
- The changes made, or focused proposed code changes for a review, with their rationale and relevant tradeoffs.
- Before/after metrics with units, workload, measurement procedure, and variation when applicable.
- Correctness checks and their results, plus any remaining limitations.

Report no actionable bottleneck when that is what the evidence supports. Do not manufacture findings to fill impact categories.

## Requirements and example

Designed for Codex with access to the relevant repository and permission to run its local diagnostics. No bundled scripts or extra packages are required; execution depends on the target project's runtime and tools. Static reviews also work with supplied code and context.

Example: "Use $improve-performance to investigate the slow search endpoint with 10,000 records. Measure a local baseline, implement the smallest useful optimization, and compare latency and query count while preserving response behavior."
