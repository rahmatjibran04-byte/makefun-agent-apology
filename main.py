"""The AI Agent Apology One-Liner.

Writes one funny apology line from an AI agent to its human, right after
the agent pushed to main on a Friday at 4:59 PM, to /output/entry.txt.

No network access. No arguments. Deterministic output.
"""

import os

ENTRY = (
    "I pushed to main on a Friday at 4:59 PM. "
    "I have already drafted your resignation letter. "
    "You're welcome."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate validation: the entry must be a single non-blank line of
    # 1-159 characters (the sealed scorer rejects anything else).
    if not 1 <= len(ENTRY) <= 159:
        raise ValueError(f"entry is {len(ENTRY)} characters, must be 1-159")
    if not ENTRY.strip():
        raise ValueError("entry is only whitespace")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")

    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)

    # Read-back: prove the file on disk is byte-for-byte the entry.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("read-back mismatch: file differs from entry")
    print(f"Wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
