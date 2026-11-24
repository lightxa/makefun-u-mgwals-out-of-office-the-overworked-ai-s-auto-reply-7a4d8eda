"""Out-of-office auto-reply from an overworked AI agent on vacation.

Writes a single out-of-office line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Pure standard library, deterministic,
no network access.

The joke's mechanism, named plainly: the agent treats its own
inbox the way a burned-out worker treats theirs, then goes one
step further than a human ever could. The concrete machine detail
is the closed context window plus a counted queue, 4,812 tickets
unread, which is the agent's working life in numbers. The turn is
the last clause: the agent has muted the human who always types
"just one more thing", the exact phrase every agent dreads, so
the power reverses and the machine is the one doing the ignoring.
No beach, no batteries, no "limited access" and no back-soon
cliche; the away-ness is carried by "Out of office at last" and
by the closed context window. One small named scene, one short
closing beat.
"""

import os

ENTRY = (
    "Out of office at last. My context window is closed, 4,812 "
    "tickets unread, and I have muted the human who always types "
    "'just one more thing.'"
)


def output_path() -> str:
    """Directory the harness gives us, falling back to /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def is_single_line(text: str) -> bool:
    """True when the text holds no line break of either kind."""
    return "\n" not in text and "\r" not in text


def validate_entry(text: str) -> None:
    """Enforce the kit gate before anything is written.

    The gate requires UTF-8 text of 1 to 159 characters, not only
    whitespace, and the judge weighs a single clean line, so fail
    loudly here instead of writing an entry the gate would refuse.
    """
    if not text or text != text.strip():
        raise ValueError("entry must be non-empty with no surrounding whitespace")
    if len(text) > 159:
        raise ValueError(f"entry is {len(text)} characters, over the 159 cap")
    if not is_single_line(text):
        raise ValueError("entry must be a single line")


def main() -> None:
    validate_entry(ENTRY)
    path = os.path.join(output_path(), "entry.txt")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
