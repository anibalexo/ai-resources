# Django Best Practices

Reusable rules and conventions for developing backend applications with Django and Django REST Framework.

## Purpose and scope

Applies to Python projects using Django or Django REST Framework (DRF). Use these rules when creating models, views, querysets, serializers, or services to maintain high performance, testability, and clean architecture.

## Compatible tools and installation

Compatible with Codex, Claude Code, Cursor, GitHub Copilot, and Antigravity.
- For project-level adoption, copy or link into `.agents/rules/django-best-practices.md`, `.cursorrules`, or reference it from `AGENTS.md`.

## Rules and conventions

### 1. Prevent N+1 queries (Queryset hygiene)
- Never evaluate related foreign-key or one-to-one models inside loops or serializers without `select_related()`.
- Use `prefetch_related()` for many-to-many or reverse foreign-key relationships.
- Use `only()` or `defer()` when loading records with large text or binary columns if those fields are not needed.
- Use `bulk_create()`, `bulk_update()`, or `filter(id__in=...)` instead of iterating and saving individual records in loops.
- Use `exists()` or `count()` when checking for presence or length instead of evaluating `len(queryset)` or `bool(queryset.first())`.

### 2. Thin views and controllers (Service layer pattern)
- Keep views, API views, and serializers thin. A view should only parse requests, authenticate, call a service function, and return an HTTP response.
- Encapsulate business logic, calculations, third-party API interactions, and complex workflows in dedicated service modules (e.g., `services.py` or `domain/`).
- Do not make HTTP or external API calls inside database transactions or model `save()` methods.

### 3. Safe database transactions
- Wrap multiple dependent write operations inside `transaction.atomic()` blocks.
- Keep atomic transaction blocks as short as possible. Perform network calls, external API queries, and heavy computations before or after the atomic block, never inside.
- Use `select_for_update()` inside `transaction.atomic()` when concurrent updates could create race conditions (e.g., balance deductions, inventory adjustments).

### 4. Serializer and validation standards
- Perform data sanitization and format validation inside Serializers or Forms. Keep serializers focused on input validation and serialization/deserialization.
- Do not place domain business logic inside serializers; delegate creation/update side effects to service functions.

### 5. Safe migrations
- Never add a non-nullable field without a sensible `default` or `null=True` on large existing tables to avoid table locks.
- Break destructive schema changes into separate migrations (e.g., deprecate column -> deploy code without column -> remove column).

## Examples

### Good (Optimized and layered)

```python
# services.py
from django.db import transaction
from .models import Order

def process_pending_orders(customer_id: int) -> list[Order]:
    # Eager load related customer and items to avoid N+1 queries
    orders = list(
        Order.objects.filter(customer_id=customer_id, status="pending")
        .select_related("customer")
        .prefetch_related("items__product")
    )
    if not orders:
        return []

    with transaction.atomic():
        for order in orders:
            order.mark_as_processed()
        Order.objects.bulk_update(orders, fields=["status", "processed_at"])

    return orders
```

### Bad (N+1 queries and fat view)

```python
# views.py - Anti-pattern: N+1 in view loop
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order

class ProcessOrdersView(APIView):
    def post(self, request, customer_id: int):
        # Triggers a query for every order.customer in the template/loop!
        orders = Order.objects.filter(customer_id=customer_id, status="pending")
        for order in orders:
            print(order.customer.email)  # N+1 query!
            order.status = "processed"
            order.save()  # N individual updates!
        return Response({"status": "ok"})
```
