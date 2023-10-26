import random


from enum import Enum


class GameState(Enum):
    """Docstring for GameState."""
    IN_PROGRESS = 'In-progress'
    LOST = 'Sorry, no more lives, you lost.'
    WON = 'Congrats! You won!'


class Hangman:
    """Wordgame Hangman"""
    def __init__(self, wordlist, numlives=5):
        """Create initial state of the game."""
        self.wordlist = wordlist
        self.numlives = numlives
        self.word = random.choice(wordlist).lower()
        self.word_guessed = ['_']*len(self.word)
        self.guesses = []
        self.game_state = GameState.IN_PROGRESS

    def check_guess(self, guess):
        """Returns True if guess is in the word, else False."""
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            for n, c in enumerate(self.word):
                if c == guess:
                    self.word_guessed[n] = c
        else:
            print(f'Sorry, {guess} is not in the word. Try again.')
            self.numlives -= 1

        print(self.word_guessed)
        print(f'{self.numlives} lives left.')
        self.guesses.append(guess)

    def ask_for_input(self):
        """Asks and validates user input for a single alphabet."""
        guess = input("Guess a letter: ")
        if not (len(guess) == 1 and guess.isalpha()):
            print('Invalid letter. Please enter a single alphabet.')
        elif guess in self.guesses:
            print('Already tried that letter.')
        else:
            self.check_guess(guess)

    def update_game_state(self):
        if self.numlives <= 0:
            self.game_state = GameState.LOST
        elif self.word_guessed.count('_') == 0:
            self.game_state = GameState.WON

    def play_game(self):
        # Keep playing the game until no more lives or winner.
        while self.game_state == GameState.IN_PROGRESS:
            self.ask_for_input()
            self.update_game_state()
        # Show endgame message
        print(self.game_state.value)


if __name__ == '__main__':
    wordlist = ['Raspberry', 'Strawberry', 'Apple', 'Blueberry', 'Avocado']
    game = Hangman(wordlist)
    game.play_game()