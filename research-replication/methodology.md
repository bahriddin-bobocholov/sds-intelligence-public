# Methodology Note

## Research objective
The broader SDS research program examines whether governance-document language can be transformed into structured empirical measures of accountability, discretion, and related governance characteristics.

This public-safe demonstration focuses on research process, not proprietary scoring logic.

## Reproducibility principles
1. Immutable input reference using SHA-256.
2. Deterministic processing with a fixed random seed.
3. Explicit train/test split logic.
4. No post-outcome information.
5. Transparent toy baseline.

## Leakage awareness
Potential leakage sources include:
- duplicate or near-duplicate clauses
- clauses from the same source document crossing train/test splits
- institution-specific drafting patterns
- post-outcome metadata
- annotation artifacts

## Interpretation
This example does not establish predictive validity. It demonstrates versioning, hashing, reproducibility, and auditability.
