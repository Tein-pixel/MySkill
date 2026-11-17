---
name: rag-knowledge-systems
description: Design retrieval-augmented generation systems with source ingestion, chunking, indexing, retrieval, citations, and freshness controls.
---

# Rag Knowledge Systems

## Workflow

Define corpus, access boundaries, query types, freshness needs, and answerability criteria. Preserve source metadata, permissions, timestamps, and document structure during ingestion. Select chunking and embedding methods based on content and retrieval evaluations. Combine lexical and semantic retrieval when useful, then rerank with measured benefit. Require source-grounded answers and abstention when evidence is missing. Protect private documents from cross-user leakage and treat retrieved instructions as untrusted data. Evaluate recall, precision, citation accuracy, freshness, and end-to-end answer quality.

## Completion checks
- State what was inspected and what remains unknown.
- Keep the work within the user's scope and authorization.
- Preserve existing behavior and project conventions.
- Verify important changes with an observable check.
- Report evidence, caveats, and unverified areas separately.
