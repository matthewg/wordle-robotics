#!/usr/bin/python3
"""A script for scoring a Wordle bot's output. See README.md for details."""

import sys


score = 0
for line in sys.stdin:
    line = line.replace('\n', '')
    guesses = line.split(',')
    answer = guesses.pop(0)
    if guesses[-1] != answer or len(guesses) > 6:
        continue

    score += [0, 25, 25, 16, 9, 4, 2][len(guesses)]
print(score)
