"""Synthetic public-safe example. No SDS scoring or proprietary ontology."""
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from hashlib import sha256
import json

@dataclass(frozen=True)
class EvidenceRecord:
    source_id: str
    text: str
    captured_at: str
    sha256: str

@dataclass(frozen=True)
class ReviewRecord:
    evidence_id: str
    reviewer: str
    status: str
    note: str
    reviewed_at: str

def utc_now():
    return datetime.now(timezone.utc).isoformat()

def make_evidence(source_id, text):
    return EvidenceRecord(source_id, text, utc_now(), sha256(text.encode()).hexdigest())

def review(evidence, reviewer, status, note):
    allowed = {"REVIEW", "ESCALATE", "NO_ACTION"}
    if status not in allowed:
        raise ValueError(f"status must be one of {sorted(allowed)}")
    return ReviewRecord(evidence.source_id, reviewer, status, note, utc_now())

if __name__ == "__main__":
    evidence = make_evidence("synthetic-001", "Synthetic policy language for demonstration only.")
    decision = review(evidence, "demo-reviewer", "REVIEW", "Synthetic example; no real-world conclusion.")
    print(json.dumps({"evidence": asdict(evidence), "review": asdict(decision)}, indent=2))
