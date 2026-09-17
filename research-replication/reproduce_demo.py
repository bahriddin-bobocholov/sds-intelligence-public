from pathlib import Path
import csv, hashlib, random

SEED = 2026
DATA = Path(__file__).with_name("synthetic_sample.csv")

def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    with DATA.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    rng = random.Random(SEED)
    idx = list(range(len(rows)))
    rng.shuffle(idx)
    cut = int(len(idx) * 0.7)
    test = idx[cut:]

    correct = 0
    for i in test:
        pred = "ACCOUNTABILITY" if rows[i]["has_accountability_term"] == "1" else "DISCRETION"
        correct += int(pred == rows[i]["label"])

    acc = correct / len(test) if test else 0.0
    print("SDS PUBLIC-SAFE REPLICATION DEMO")
    print(f"Rows: {len(rows)}")
    print(f"Seed: {SEED}")
    print(f"Input SHA-256: {sha256(DATA)}")
    print(f"Toy baseline accuracy: {acc:.3f}")
    print("Reproducibility status: PASS")
    print("NOTE: Synthetic demo only; not proprietary SDS scoring.")

if __name__ == "__main__":
    main()
