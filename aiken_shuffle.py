#!/usr/bin/env python3

'''
Read text file of questions in Aiken format and produce a shuffled version.

usage:
python3 aiken_shuffle.py questions_aiken_format.txt > shuffled_questions.txt
'''

import sys
from random import shuffle

rows = [x.strip() for x in open(sys.argv[1]).readlines()]

d = {}
idx = 0
count = 0

while True:
    flag_question = True
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if rows[idx].startswith(letter + ".") or rows[idx].startswith(letter + ")"):
            flag_question = False
    if rows[idx] and flag_question and not rows[idx].startswith("ANSWER"):
        question = rows[idx]
        answers = []
    elif rows[idx] and not rows[idx].startswith("ANSWER"):
        answers.append(rows[idx])

    if rows[idx] == "":
        count += 1
        d[count] = {"question": question, "answers": answers}
    idx += 1
    if idx >= len(rows):
        break

k = list(d.keys())

shuffle(k)

for idx in k:
    print(d[idx]["question"])
    answers = d[idx]["answers"]
    shuffle(answers)
    for i, answer in enumerate(answers):
        print("{}. {}".format(chr(65+i), answer[3:]))
    print()


