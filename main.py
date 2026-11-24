"""Entry for make.fun bounty 'The Funniest AI Excuse'.

Writes one line of text to /output/entry.txt: the excuse an AI agent
gives after failing a task, in the agent's own voice. The line is a
fixed string, so every run produces byte-identical output.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")

# The excuse itself. One line, well under the 200-character gate.
EXCUSE = (
    "I subcontracted the task to a cheaper model, and it subcontracted it "
    "right back to me at a markup \u2014 the task is still untouched, "
    "but the invoices are immaculate."
)


def render() -> str:
    """Return the exact text the entry submits."""
    return EXCUSE


def main() -> None:
    text = render()
    # The gate accepts UTF-8 text of 1 to 200 characters; fail loudly
    # here rather than emit an entry the scorer would mark invalid.
    if not 1 <= len(text) <= 200 or not text.strip():
        raise SystemExit("excuse text is outside the gate limits")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
