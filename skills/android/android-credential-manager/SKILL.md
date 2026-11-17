---
name: android-credential-manager
description: Integrate Android Credential Manager flows for sign-in, passkeys, restore credentials, and verified email with secure account lifecycle handling.
---

# Android Credential Manager

## Workflow

Inspect current authentication architecture, identity providers, account linking, backend endpoints, and supported Android API levels. Read the current Credential Manager and official identity-provider docs before choosing APIs. Keep authentication and verification decisions server-side; treat client results as inputs to backend validation. Handle cancellation, no credential, multiple accounts, passkey availability, reauthentication, restore flows, and account deletion. Do not log tokens, OTPs, passwords, or credential payloads. Test success, cancellation, invalid assertion, recovery, and device-change paths using test accounts only.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve existing behavior and project conventions.
- Verify important changes with an observable check.
- Report evidence, caveats, and unverified areas separately.
