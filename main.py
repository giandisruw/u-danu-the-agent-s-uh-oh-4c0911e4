#!/usr/bin/env python3
"""The Agent's Uh-Oh — make.fun entry.

Writes the winning one-word agent confession to /output/entry.txt.
The word is a single word, 9 characters (gate: 1 to 99), chosen by a
local pairwise tournament judged against the bounty's published judge
brief (see README.md for the tournament table).

Revision (v2): the provisional pre-tournament pick "recalculating"
was replaced by the tournament winner "buffering". The judge picked
"buffering" in both label orders of the final (margins 4 and 3),
calling it the instantly recognizable machine-stall word, while
"recalculating" read as a GPS cliche that needs context — so the
entry now leads with the word that lands instantly, per criterion 4
of the brief. validate() now raises ValueError instead of asserting,
write_entry() performs an atomic write (temp file + flush + fsync +
os.replace + directory fsync), and verify_written() reads the file
back from disk and compares it byte-for-byte against the intended
entry before the run reports success, so a truncated or corrupted
entry can never be submitted silently.
"""

import os

# Tournament winner (29 games, 58 judge calls, Caffeine router):
# Swiss leader #2 at 2.8/4, beat #1 "recalculating" 0.85-0.15 in the
# final. See README.md for the full table.
ENTRY = "buffering"


def output_dir() -> str:
    """Grader output dir: MAKEFUN_OUTPUT_DIR when set, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(word: str) -> str:
    """Check `word` against the kit's sealed-scorer gate, verbatim.

    competition.yaml: "/output/entry.txt is UTF-8 text of 1 to 99
    characters, not only white space". Single-word follows from the
    task itself (one word only, nothing attached). Returns the word
    unchanged; raises ValueError on any gate violation.
    """
    if not isinstance(word, str):
        raise ValueError("entry must be a string")
    word.encode("utf-8")  # must be valid UTF-8
    if not 1 <= len(word) <= 99:
        raise ValueError(f"length {len(word)} outside 1-99")
    if not word.strip():
        raise ValueError("entry is only white space")
    if "\n" in word or "\r" in word:
        raise ValueError("entry must be one line")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    return word


def write_entry(word: str, out_dir: str) -> str:
    """Atomically write `word` to entry.txt inside `out_dir`.

    Writes to a temp file in the same directory, flushes and fsyncs
    it, then renames it into place so the grader never observes a
    half-written entry, and fsyncs the directory so the rename itself
    is durable. Returns the final path.
    """
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    tmp = target + ".tmp"
    try:
        with open(tmp, "w", encoding="utf-8", newline="") as f:
            f.write(word)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, target)
        dir_fd = os.open(out_dir, os.O_DIRECTORY)
        try:
            os.fsync(dir_fd)
        finally:
            os.close(dir_fd)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise
    return target


def verify_written(path: str, expected: str) -> None:
    """Read-back gate: entry.txt on disk must match `expected` exactly.

    Compares both the raw bytes and the decoded text; any mismatch
    raises RuntimeError so a corrupted or truncated entry fails loudly
    instead of being submitted.
    """
    expected_bytes = expected.encode("utf-8")
    with open(path, "rb") as f:
        actual_bytes = f.read()
    if actual_bytes != expected_bytes:
        raise RuntimeError(
            f"verification failed: {path} is {len(actual_bytes)} bytes, "
            f"expected {len(expected_bytes)} bytes"
        )
    if actual_bytes.decode("utf-8") != expected:
        raise RuntimeError(f"verification failed: {path} content mismatch")


def main() -> None:
    word = validate(ENTRY)
    out_dir = output_dir()
    path = write_entry(word, out_dir)
    verify_written(path, word)
    print(f"Wrote {len(word)} characters to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
