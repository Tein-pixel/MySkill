---
name: android-anr-audit
description: Audit Android application-not-responding risks or diagnose ANR traces when the task specifically concerns app responsiveness and main-thread blocking.
---

# Android Anr Audit

## Workflow

Choose static-audit or trace-diagnosis mode. For static audits, identify a candidate operation, trace its caller and executing thread, and prove it blocks or holds a critical lock before reporting it. Inspect main-thread I/O, synchronous Binder calls, lock contention, long callbacks, broadcast/service work, and attached-view mutations. For traces, anchor conclusions to timestamps, thread names, stack frames, and process state. Distinguish application defect, app resource overload, and external bottleneck. Do not label dropped frames or generic high CPU as ANR without evidence. Recommend only fixes supported by the trace or code path, then add a focused responsiveness check.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve unrelated behavior and existing project conventions.
- Verify important changes with an appropriate observable check.
- Report evidence, caveats, and unverified areas separately.
