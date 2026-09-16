# Order history usage

Draft example only: this feature is not implemented in this repository. The instructions below describe the intended contract and must be checked against real behavior before publication.

## View orders

Authenticate using the target application's normal mechanism, then request `GET /api/orders/history`. The proposed endpoint returns your orders from newest to oldest, up to 20 per page.

Illustrative response:

```json
{
  "items": [
    {"id": 42, "created_at": "2026-01-10T12:00:00Z", "total": "25.00", "status": "paid"}
  ],
  "next_cursor": null
}
```

If `next_cursor` is present, pass that exact opaque value as the `cursor` query parameter for the next page. Do not construct or modify cursors. A null cursor means there are no additional pages.

## Empty results and errors

- No orders: HTTP 200, empty `items`, and null `next_cursor`.
- Missing authentication: HTTP 401; authenticate before retrying.
- Invalid or expired cursor: HTTP 400; restart from the first page.

The endpoint is intended to expose only the signed-in customer's orders. It does not create, modify, or refund orders. See the [specification](spec.md) for the complete proposed contract.
