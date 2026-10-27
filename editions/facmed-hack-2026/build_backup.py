#!/usr/bin/env python3
"""Backup deck without the live quiz: slides-backup.md / .html / .pdf.

Builds from the same module files as build.sh but leaves slides.md alone. Each quiz
slide keeps its question and options; the QR/PIN box becomes a static "answer in the
Zoom chat" box and the live-results iframe is dropped. Use it if the quiz app is down.

Usage: python3 build_backup.py           -> slides-backup.md
       python3 build_backup.py --html    -> + slides-backup.html (Marp)
       python3 build_backup.py --pdf     -> + slides-backup.html + slides-backup.pdf (Chrome headless)
"""
import glob
import os
import re
import subprocess
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))

parts = [open("_header.md").read()]
parts += [open(f).read() for f in sorted(glob.glob("[0-9][0-9]-*.md"))]
md = parts[0] + "\n\n---\n\n".join(parts[1:])

quiz_url = open("quiz_url.txt").read().strip()
md = md.replace("{{QUIZ_URL}}", quiz_url.removeprefix("https://"))  # speaker notes only
md = md.replace("{{QUIZ_PIN_LABEL}}", "")

ANSWER_BOX = ('<div class="quizbox"><div><b>Your answer</b>'
              '<span>{}</span></div></div>')
# The word-cloud exercise has an inline (static-positioned) box; the polls have the corner box.
md, n_inline = re.subn(r'<div class="quizbox" style="[^"]*">.*?</div></div>',
                       '<div class="quizbox" style="position:static; display:inline-flex; margin-top:10px;">'
                       '<div><b>Your answer</b><span>A few words in the Zoom chat</span></div></div>', md)
md, n_box = re.subn(r'<div class="quizbox">.*?</div></div>',
                    ANSWER_BOX.format("Type the letter(s) in the Zoom chat"), md)
md, n_iframe = re.subn(r'<iframe class="livequiz[^"]*"[^>]*></iframe>\n?', "", md)

REWORD = [
    ("quizzes and discussion, on real data", "questions and discussion, on real data"),
    ("- **Live quiz** on your phone or laptop: next slide.",
     "- **Questions** on the slides: answer in the Zoom chat, or unmute."),
    ("- **Quizzes, discussion**,", "- **Questions, discussion**,"),
    ('<span class="qnum">Live quiz · first question · join now</span>',
     '<span class="qnum">First question · answer in the Zoom chat</span>'),
    ("Exercise · 3 minutes · live quiz", "Exercise · 3 minutes · Zoom chat"),
    ("A few words, in the live quiz.", "A few words, in the Zoom chat."),
    ("Then we look at the word cloud: how many", "Then we read the chat: how many"),
    ("the room's answers to the opening quiz", "the room's answers to the first question"),
]
for old, new in REWORD:
    if old not in md:
        sys.exit(f"build_backup.py: wording not found, update REWORD: {old!r}")
    md = md.replace(old, new)
md = re.sub(r'(<span class="qnum">)Poll (\d) of 6', r"\1Question \2 of 6", md)
md = md.replace('<span class="kicker">Poll 2 · the answer', '<span class="kicker">Question 2 · the answer')
md = re.sub(r'^title: "(.*)"$', r'title: "\1 (backup, no live quiz)"', md, count=1, flags=re.M)

# Nothing quiz-related may survive on the slides themselves (comments are speaker notes).
visible = re.sub(r"<!--.*?-->", "", md, flags=re.S)
visible = visible.split("\n---\n", 1)[1]  # skip the front matter / CSS
left = [l for l in visible.splitlines()
        if re.search(r"live quiz|quiz_qr|livequiz|QUIZ_|Vote live", l, re.I)]
if left:
    sys.exit("build_backup.py: quiz remnants on slides:\n" + "\n".join(left))

open("slides-backup.md", "w").write(md)
print(f"Built slides-backup.md: {n_box + n_inline} quiz boxes replaced, {n_iframe} live panels removed.")

if len(sys.argv) > 1 and sys.argv[1] in ("--html", "--pdf"):
    subprocess.run(["npx", "-y", "@marp-team/marp-cli@4.1.2", "slides-backup.md", "--html",
                    "--allow-local-files", "-o", "slides-backup.html"], check=True)
if len(sys.argv) > 1 and sys.argv[1] == "--pdf":
    chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    subprocess.run([chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={os.getcwd()}/slides-backup.pdf",
                    f"file://{os.getcwd()}/slides-backup.html"], check=True, stderr=subprocess.DEVNULL)
    print("Wrote slides-backup.pdf")
