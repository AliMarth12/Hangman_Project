# wordsWord Game - Hangman

## Description
This directory houses a Python-based application for enjoying the traditional word game Hangman through a command-line interface.

## How to Install and Run?
To run and engage in this game, ensure that Python 3 is included in your system's PATH.

Clone the repository and navigate to the 'HangmanProject' directory in your Terminal. Alternatively, you can download or copy-paste the 'milestone_5.py' script to your computer and change your working directory to the corresponding path in the Terminal.

Execute the program using the command python3 milestone_5.py.

## Gameplay / Usage
At the start, the game will present you with a hidden word to decipher, showing only the word's length.
To make your guesses, simply type an English alphabet and press Enter.
You have a total of 5 lives to spare, and incorrect guesses will be tracked by the number of lives remaining. Remember, invalid and duplicate inputs won't be counted as incorrect guesses.

When the character you guess is part of the word, the program will unveil it in one or more of its positions. However, if your guess is not in the word, you'll lose 1 life.

## Project Organization
This project is structured as a Python class named 'Hangman.' To set up the initial game state, you simply instantiate this class.

## License
---