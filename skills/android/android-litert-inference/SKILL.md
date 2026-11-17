---
name: android-litert-inference
description: Build or optimize on-device TensorFlow Lite or LiteRT inference with model compatibility, accelerator selection, preprocessing, and performance measurement.
---

# Android Litert Inference

## Workflow

Identify the model format, input/output tensors, quantization, operator requirements, supported ABI, and target device capabilities. Check current official LiteRT runtime and delegate APIs; distinguish legacy TensorFlow Lite paths from current LiteRT interfaces. Validate model provenance and license. Implement deterministic preprocessing/postprocessing, bounded memory use, and lifecycle-aware interpreter/compiled-model ownership. Select CPU/GPU/NPU delegates only after capability checks and measurement. Test numerical correctness against a reference implementation and compare latency, memory, and thermal behavior. Never claim accelerator use unless logs or profiling confirm it.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve existing behavior and project conventions.
- Verify important changes with an observable check.
- Report evidence, caveats, and unverified areas separately.
