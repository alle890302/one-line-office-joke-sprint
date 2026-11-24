#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint entry.

Final line (pass 1): "I asked for a raise and got a pizza party. I now own 14% of a pepperoni."

Weighing vs the judge's ordered criteria:
1. One-line joke about office life: yes, a single line, setup + punchline.
2. Funny: the punchline surprises — a raise turned into a pizza party is a
   familiar office gripe, but "I now own 14% of a pepperoni" pays it off
   with a concrete, absurd image anyone who has sat in an office recognises.
3. One line: two short sentences on one line, no rambling.
4. Fresh: the pepperoni-ownership turn is a specific detail, not a generic
   complaint; the joke is not one everyone has already heard.
5. Clear on first read: no reference the reader cannot follow, tight wording.
72 chars, inside the 1-200 gate.

Pass 2 (revision): tested two genuine challengers and kept pass 1.
- Printer/Management ("The printer only works when nobody needs it. We have
  named it Management."): good turn, but its setup is a well-worn observation;
  loses to the pizza line on freshness (criterion 4) and laugh size (2).
- "We're a family" ("My boss said we're a family. I checked the org chart:
  I'm the cousin nobody invites to weddings."): a known trope, and it asks
  the reader to hold two images at once; weaker on first-read clarity (5).
- Tightening the pizza line ("more money" for "a raise") loses the office
  word for no gain. Pass 1 stands.
"""
import os

ENTRY = "I asked for a raise and got a pizza party. I now own 14% of a pepperoni."

if __name__ == "__main__":
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
