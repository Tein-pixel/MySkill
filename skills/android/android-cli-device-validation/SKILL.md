---
name: android-cli-device-validation
description: Use available Android CLI, SDK tools, adb, emulator, and UI inspection tools to validate Android apps and diagnose device behavior.
---

# Android Cli Device Validation

## Workflow

Discover which Android tools are installed and authorized; never assume a CLI exists. Inspect connected devices with read-only listing commands before targeting a device. Use UI dumps to identify interactive controls and screenshots to inspect visual output; visually examine screenshots before acting. Prefer package/activity inspection and controlled smoke tests over coordinate guessing. Avoid destructive device resets, personal-data extraction, or settings changes without permission. Record model, API level, variant, commands, and outcomes.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve unrelated behavior and existing project conventions.
- Verify important changes with an appropriate observable check.
- Report evidence, caveats, and unverified areas separately.
