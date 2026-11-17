---
name: agent-skill-evaluation
description: Evaluate Agent Skills for instruction quality, activation precision, task performance, safety, and regression using representative behavioral tests.
---

# Agent Skill Evaluation

## Workflow

Define the skill's intended trigger, non-trigger cases, required behavior, and unacceptable failure modes before testing. Build a versioned test set covering positive, negative, ambiguous, adversarial, boundary, and regression prompts. Run tests on a named compatible agent/model/runtime with the skill enabled and an appropriate baseline without it. Use blind or independently scored outputs where practical; avoid evaluating a skill solely by the same model that authored it. Score correctness, instruction adherence, evidence quality, tool discipline, safety, latency, and output utility. Record model/version, settings, test data, rubric, failures, and limitations. Do not label a test plan as a benchmark result or infer general improvement from a few cherry-picked runs.

## Completion checks
- State sources, snapshot date, and search limitations.
- Check overlap, safety, maintenance, and license before adoption.
- Distinguish original work from upstream-derived ideas.
- Record tests actually run and leave unrun evaluations marked as pending.
- Preserve repository history and existing working skills.
