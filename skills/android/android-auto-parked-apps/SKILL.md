---
name: android-auto-parked-apps
description: Assess and adapt eligible Android app experiences for parked use in Android Auto or Android Automotive OS within current platform restrictions.
---

# Android Auto Parked Apps

## Workflow

Verify the app category and exact Google car-platform eligibility rules before planning. Do not assume a regular phone activity can be displayed in a car. Separate parked-only behavior from driving-optimized experiences and follow current distraction-optimization requirements. Inspect manifest declarations, supported templates or parked-app APIs, input restrictions, lifecycle, display sizing, and approval requirements. Keep any experience unavailable while the vehicle is moving unless explicitly permitted by platform policy. Test only through supported emulator or vehicle environments and describe limitations honestly.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve existing behavior and project conventions.
- Verify important changes with an observable check.
- Report evidence, caveats, and unverified areas separately.
