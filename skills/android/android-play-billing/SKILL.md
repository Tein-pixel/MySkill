---
name: android-play-billing
description: Integrate or upgrade Google Play Billing with lifecycle-safe purchase flows, product queries, acknowledgement, entitlement verification, and policy-aware handling.
---

# Android Play Billing

## Workflow

Inspect the existing Billing Library version, product model, backend verification flow, subscription status model, and target Play distribution. Read current official Billing documentation and deprecation deadlines before selecting a version. Query products and offers dynamically; do not hard-code price assumptions. Treat client callbacks as untrusted until purchases are verified by a trusted backend where required. Handle pending, cancelled, refunded, expired, and restored purchases, plus acknowledgement deadlines and network failures. Keep purchase UI clear and never simulate successful payment. Test with Play test tracks and license testers when authorized.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve existing behavior and project conventions.
- Verify important changes with an observable check.
- Report evidence, caveats, and unverified areas separately.
