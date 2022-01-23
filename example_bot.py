#!/usr/bin/python3

import random
import sys

import wordle_colors


def play_wordle(wordlist, answer):
    random.shuffle(wordlist)
    guesses = []
    
    while len(guesses) < 6:
        if len(guesses) == 0:
            guess = 'cares'
        else:
            available_letters = set('abcdefghijklmnopqrstuvwxyz')
            for guess in guesses:
                colors = wordle_colors.colors(answer, guess)
                for i in range(5):
                    if colors[i] == wordle_colors.UNCOLORED:
                        available_letters.discard(guess[i])
            previous_guess = guesses[-1]
            previous_colors = wordle_colors.colors(answer, previous_guess)
            guess = None

            need_letters = []
            for i in range(5):
                if previous_colors[i] == wordle_colors.YELLOW:
                    need_letters.append(previous_guess[i])
            
            for word in wordlist:
                if word in guesses:
                    continue
                word_is_usable = True
                unused_yellow_letters = need_letters[:]
                for i in range(5):
                    if word[i] not in available_letters:
                        word_is_usable = False
                        break

                    if previous_guess[i] == wordle_colors.GREEN and word[i] != previous_guess[i]:
                        word_is_usable = False
                        break

                    if word[i] in unused_yellow_letters:
                        unused_yellow_letters.remove(word[i])

                    if not word_is_usable:
                        break

                if word_is_usable and not unused_yellow_letters:
                    guess = word
                    break

        if not guess:
            guess = wordlist[0]
        guesses.append(guess)
        if guess == answer:
            break
        
    return guesses


if __name__ == '__main__':
    wordlist = []
    with open('dictionary.txt', 'r') as wordfile:
        for word in wordfile:
            word = word.replace('\n', '')
            wordlist.append(word)

    for answer in sys.stdin:
        answer = answer.replace('\n', '')
        guesses = play_wordle(wordlist, answer)
        print(f'{answer},{",".join(guesses)}')
