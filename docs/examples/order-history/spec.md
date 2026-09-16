# Specification: order history

Status: fictional, unimplemented example.

## Objective and scope

An authenticated customer can view their order history, including order id, creation time, total, and status. The hypothetical project already has accounts, orders, and authentication. Creating orders, refunds, and administrative reporting are excluded.

## Acceptance criteria

- AC-01: `GET /api/orders/history` returns only the authenticated customer's orders. Unauthenticated requests return HTTP 401.
- AC-02: Results sort by creation time descending, then order id descending to resolve ties.
- AC-03: The response contains at most 20 orders per page and a `next_cursor` value when another page exists. Cursors are opaque; malformed or expired cursors return HTTP 400.
- AC-04: A customer with no orders receives HTTP 200 with `items: []` and `next_cursor: null`.
- AC-05: Each item exposes only `id`, `created_at`, `total`, and `status`. Monetary totals are decimal strings; timestamps use UTC ISO 8601.

## Assumptions and constraints

Authentication, customer ownership, and order storage already exist in the fictional application. Their actual APIs must be inspected before implementation in a real project. No measured performance target or new database field is assumed.

The example uses an existing hypothetical signed-cursor utility. A real plan must establish that it exists or explicitly propose an alternative. Product owners would review these requirements before they are called approved.
