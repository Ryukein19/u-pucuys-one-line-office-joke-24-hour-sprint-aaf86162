import os
# One-liner entry (121 chars): the line below is the whole submission.
# Writes to /output/entry.txt.
LINE = "The meeting was so long the intern finished the internship, got hired, and is now chairing the meeting about the meeting."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
