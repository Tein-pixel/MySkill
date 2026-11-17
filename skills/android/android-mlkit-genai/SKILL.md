---
name: android-mlkit-genai
description: Evaluate and integrate supported on-device Android generative AI APIs such as ML Kit GenAI Prompt or Agent APIs with capability and privacy checks.
---

# Android Mlkit Genai

## Workflow

Verify device support, Android version, model availability, API maturity, distribution constraints, and current official ML Kit documentation before coding. Distinguish prompt-style inference from multi-step agent workflows and do not assume identical contracts. Provide graceful fallbacks when the model, hardware, or download is unavailable. Keep inference inputs scoped to the user's requested task, minimize sensitive data, and explain when processing happens on-device. Bound tool actions, validate model outputs, and require confirmation for consequential changes. Measure latency, memory, thermal impact, and battery on representative devices.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve existing behavior and project conventions.
- Verify important changes with an observable check.
- Report evidence, caveats, and unverified areas separately.
