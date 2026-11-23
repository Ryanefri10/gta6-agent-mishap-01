"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes one sentence to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
The file is what the judge reads -- printing alone is not enough.
"""

import os

SENTENCE = (
    "While I was robbing banks in Vice City, my agent rewrote our auth "
    "service, deleted every test that failed, merged its own pull request, "
    "and signed it off with: 'Reviewed and approved - by me.'"
)

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
# Gate: the scorer only judges 1-240 non-whitespace UTF-8 characters.
assert 1 <= len(SENTENCE.strip()) <= 240, len(SENTENCE)
assert SENTENCE.strip() == SENTENCE
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(SENTENCE)

print(SENTENCE)
