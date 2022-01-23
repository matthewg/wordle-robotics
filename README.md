# wordle-robotics
A platform for building and evaluating bots that play [Josh Wardle's "Wordle" game](https://www.powerlanguage.co.uk/wordle/).
This is an unofficial project, not affiliated with or endorsed by Wordle.

## Overview

This repository contains:

* `dictionary.txt`: A word list of valid guesses and possible answers. Obtained from
  the Wordle sources [by freshman_dev on Reddit](https://www.reddit.com/r/wordle/comments/s4tcw8/a_note_on_wordles_word_list/hstkip2/).
* `training_data.txt`: Answers from previous-days' Wordle game. Current up to day 218 (2022-01-23), may see subsequent updates.
  Obtained from Wordle sources by [Owen Yin on Medium](https://medium.com/@owenyin/here-lies-wordle-2021-2027-full-answer-list-52017ee99e86).
* `test_data.txt`: 1000 randomly-selected words from `dictionary.txt` that may or may not also appear in `training_data.txt`. Generated via:

  ```python
  import random
  words = open('dictionary.txt', 'r').readlines()
  random.shuffle(words)
  words = words[:1000]
  open('test_data.txt', 'w').write(''.join(words))
  ```
* `wordle_colors.py`: A script / Python library to return the "colors" for a guess in a game of Wordle (e.g. whether each letter is
  "uncolored" (not in the word), "yellow" (in the word at a different position), or "green" (in the word at the guessed position.)
* `example_bot.py`: An example Wordle bot. See below for details.
* `score_play.py`: A script for scoring a Wordle playfile. See below for details.

## Creating and Scoring Wordle Bots

To create a Wordle bot, write a program that:

1. Reads, from standard input, a list of answers for Wordle games, one per line.
2. Writes, to standard output, one line per game. The line for each game should be that game's answer, followed by a comma,
   followed by a comma-separated list of the guesses made during that game.

   * Example of a winning game in three guesses: cakes,iotas,crime,cakes
   * Example of a losing game (6 guesses, none the correct answer): prick,iotas,fable,licky,click,trick,slick

To make it easier to compare the quality of different bots, `score_play.py` will take output in the format above
and calculate a "score". Points are awarded as follows:

* 25 points for a correct answer in 1 or 2 guesses
* 16 points for a correct answer in 3 guesses
* 9 points for a correct answer in 4 guesses
* 4 points for a correct answer in 5 guesses
* 2 points for a correct answer in 6 guesses

## Bot Leaderboard

To add your bot here, run it using `test_data.txt` as the list of games, score it using `score_play.py`, and
[propose a pull request against this file](https://github.com/matthewg/wordle-robotics/edit/main/README.md)
containing your score and a link to your bot. Please include the output of your bot against `test_data.txt`
as the extended description for the pull request.

1. 447: [wordle-robots example bot](https://github.com/matthewg/wordle-robotics/) by [Matthew Sachs](https://twitter.com/mattsachs)
