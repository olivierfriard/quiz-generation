#!/usr/bin/env python3

"""
Create a Latex quiz from a text file with questions in Aiken format (see https://docs.moodle.org/400/en/Aiken_format).
Formula in Latex format are supported using square brackets (example: [E = mc^2])
If your system does not have a working Latex installation the PDF can be then generated using the Overleaf service (https://www.overleaf.com) for example.

(c) Olivier Friard 2022

Usage:
python3 aiken2latez.py FILE.txt > FILE.tex


"""

TITLE = "Test"
DATE = "YYYY-MM-DD"

__version__ = "0.0.1"

HEADER = rf"""
\documentclass[11pt]{{article}}

\usepackage{{amsmath,amssymb,amsfonts}}
\usepackage{{graphicx}}

\setlength{{\topmargin}}{{-.5in}} \setlength{{\textheight}}{{9.25in}}
\setlength{{\oddsidemargin}}{{0in}} \setlength{{\textwidth}}{{6.8in}}

\begin{{document}}

\Large

\noindent{{\bf {TITLE}\hfill {DATE}}}
\medskip\hrule

\begin{{enumerate}}
"""


FOOTER = r"""\end{enumerate}
\end{document} 
"""

import sys

file_name = sys.argv[1]

with open(file_name, "r") as f_in:
    rows = [x.strip("\n") for x in f_in.readlines()]

answers = {}

print(HEADER)

for row in rows:

    if not row:
        continue

    flag_answer = False
    for idx, init_answer in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        if row.startswith(init_answer + ") ") or row.startswith(init_answer + "."):
            answers[idx] = row[3:]
            flag_answer = True
            break

    if not flag_answer:
        if "ANSWER:" in row:
            print(rf"\item {question}")
            print(r"\begin{enumerate}")
            for ans in sorted(answers):
                if "[" in answers[ans] and "]" in answers[ans]:
                    answer = answers[ans].replace("[", "$").replace("]", "$")
                else:
                    answer = answers[ans]
                print(rf"    \item {answer}")
            print(r"\end{enumerate}")
            print()

            answers = {}
            flag_answer = False
        else:
            question = row
    else:
        flag_answer = False

print(FOOTER)
