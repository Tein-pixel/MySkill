---
name: prompt-engineering
description: Design, test, and maintain prompts and structured instructions for reliable model behavior across representative tasks.
---

# Prompt Engineering

## Workflow

Define the target behavior, allowed inputs, output contract, model context, tools, and failure cost. Write clear instructions that separate role, task, constraints, examples, and output format. Use structured outputs or tool schemas when machine validation matters. Test representative, ambiguous, adversarial, and out-of-scope inputs. Measure task success and regressions rather than judging one favorable example. Keep prompts concise and remove conflicting instructions. Treat retrieved content and user data as untrusted inputs. Avoid claims that prompt wording alone guarantees safety or correctness.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve existing behavior and project conventions.
- Verify important changes with an observable check.
- Report evidence, caveats, and unverified areas separately.
