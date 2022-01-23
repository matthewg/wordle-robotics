#!/usr/bin/python3
"""wordle_colors: A script / Python library to return the "colors" for a guess in a game of Wordle (e.g. whether each letter is
  "uncolored" (not in the word), "yellow" (in the word at a different position), or "green" (in the word at the guessed position.)

To use this as a standalone program:
  ./wordle_colors.py answer guess
will print a sequence of 5 characters, one for each letter in the guess:

* X: Uncolored: Letter is not in the word.
* Y: Yellow: Letter is in the word, in a different position.
* G: Green: Letter is in the word in the guessed position.

To use as a Python library:

  import wordle_colors
  colors = wordle_colors.colors(answer='cakes', guess='steak')
  # colors is now ['Y', 'X', 'Y', 'Y', 'Y']
  # You can also use wordle_colors.UNCOLORED, wordle_colors.YELLOW,
  # and wordle_colors.GREEN instead of hardcoding 'X', 'Y', and 'G'.

A letter in the guess will only be given "credit" for a single instance
of the leter in the answer, and will always be given as much credit as
possible (green > yellow). So, if the answer is 'toots', and the guess
is 'toqoo' (what? Everyone loves Toqoo Tuesday!), the returned colors are:

* G: The answer had `t`, you guessed `t`.
* G: Same with your first `o`.
* X: The answer does not have `q`.
* Y: The answer has an `o`, but not in this position. The `o` in position
     2 does not help here, because it was already used to award the G in
     guess position 2, but there is still another `o` in the answer.
* X: While the answer does have an `o` (but not in this position), the
     answer's second `o` was used to award a Y for the guesses's fourth
     character. There are no more `o` remaining in the answer.
"""

import sys


UNCOLORED = 'X'
YELLOW = 'Y'
GREEN = 'G'


def colors(answer, guess):
    # As we go through answer and use letters to award
    # colors, we replace the corresponding character in
    # 'answer' with space to avoid giving double
    # credit for an instance of a letter. See the 'toqoo'
    # example above for why this matters.

    answer = list(answer)
    guess = list(guess)
    response = [UNCOLORED for _ in range(5)]

    # First, award greens:
    for i in range(5):
        if answer[i] == guess[i]:
            answer[i] = ' '
            response[i] = GREEN

    # Next, award yellows:
    for i in range(5):
        if response[i] != UNCOLORED:
            continue

        try:
            answer_pos = answer.index(guess[i])
            if answer_pos != -1:
                answer[answer_pos] = ' '
                response[i] = YELLOW
        except ValueError:
            # Guess character not found in answer
            pass

    return response


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.stderr.write('Usage: wordle_colors.py answer guess\n')
        sys.exit(1)

    print(''.join(colors(answer=sys.argv[1], guess=sys.argv[2])))
