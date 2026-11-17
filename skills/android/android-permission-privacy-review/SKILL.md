---
name: android-permission-privacy-review
description: Review Android runtime permission flows and privacy-sensitive data access for least privilege and clear user control.
---

# Android Permission Privacy Review

## Workflow

Inventory manifest permissions and correlate each with a user-facing feature. Prefer system pickers and scoped APIs over broad storage, media, or location access when they satisfy the use case. Request permissions just in time, explain the user benefit, handle denial and permanent denial, and avoid repeatedly prompting. Check API-level behavior, one-time grants, approximate location, background access, notifications, camera, microphone, and media access. Keep sensitive data out of logs. Test grant, denial, revocation, and settings-return flows.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve unrelated behavior and existing project conventions.
- Verify important changes with an appropriate observable check.
- Report evidence, caveats, and unverified areas separately.
