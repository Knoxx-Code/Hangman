from words import words as w
from board import board
import random as r
import os


def getWord():
    word = r.choice(w)
    return word.upper()


def displayGallows(attempts):
    gallows = board
    return gallows[attempts]  # Returns the hangman based off the attempt the player is on


def play(word):
    blanks = "_" * len(word)
    win = False
    guessed_letters = []  # List to hold letters that have already been guessed
    guessed_words = []  # List to hold words that have already been guessed
    attempts = 6  # Attempts refers to the no. of times a player has before the 'Hangman' is completed
    print(displayGallows(attempts))
    print(blanks)
    print("\n")

    while not win and attempts > 0:
        guess = input("Please enter a letter or word you think is correct: ").upper()

        # Checking if player has guessed a letter
        if len(guess) == 1 and guess.isalpha():
            # Handling a repeated guess
            if guess in guessed_letters:
                print("You have already guessed this letter")
            # Handling an incorrect guess
            elif guess not in word:
                print(f"'{guess.upper()}' is not contained in the word")
                attempts -= 1
                guessed_letters.append(guess)
            # Handling a correct guess
            else:
                print(f"Congrats!,'{guess.upper()}' is in the word")
                guessed_letters.append(guess)
                # Updating the blanks
                blanks_list = list(blanks)
                # Getting  the index and letter at said index
                index = [i for i, letter in enumerate(word) if letter == guess]
                for x in index:
                    # Append guess to the blanks list
                    blanks_list[x] = guess
                # Convert the list back to a string
                string = ""
                blanks = string.join(blanks_list)
                # Check if the word is completed by the guess i.e no more blanks
                if "_" not in blanks:
                    win = True

        # Checking if the player has guessed the word
        elif len(guess) == len(word) and guess.isalpha():
            # Handling if the guess was already done
            if guess in guessed_words:
                print(f"You have already guessed the word: {guess}")
            # Handling an incorrect guess
            elif guess != word:
                print(f"Oops!{guess.upper()} is not the word!")
                attempts -= 1
                guessed_words.append(guess)
            # Handling a correct guess
            else:
                win = True
                blanks = word
        else:
            print("Input is not a valid guess!")

        print(displayGallows(attempts))
        print(blanks)
        print("\n")

    if win:
        print("WINNER! YOU GUESSED THE WORD CORRECTLY,NO STICK FIGURE HAS TO DIE,\U0001F605 LOL!")
    else:
        print("OOPS!YOU FAILED TO GUESS THE WORD AND A STICK FIGURE DIED \U0001F622")
        print(f'The word was: {word}.\n MAYBE NEXT TIME!')


def main():
    print("WELCOME TO HANGMAN! LET'S PLAY!")
    while True:
        try:
            no_of_players = int(input("Select the number of players you want(1 or 2-player): "))
            while no_of_players > 0:
                if no_of_players == 1:
                    print("You have chosen 1-player mode. It's you vs the Computer")
                    word = getWord()
                    play(word)
                    while input("Would you like to play again(Y/N): ").upper() == 'Y':
                        word = getWord()
                        play(word)
                    else:
                        exit()

                elif no_of_players == 2:
                    print("You have chosen 2-player mode. Player 1 vs Player 2")
                    word_selector = r.randint(1, 2)
                    if word_selector == 1:
                        print("Player 1 chooses the word")
                        word = input(f'Player 1, please enter a word: ').upper()
                        while not word.isalpha():
                            word = input("Input must be a word!\nPlease enter a word: ").upper()
                        os.system('cls')
                        print("Player 2, Time to guess!")
                    else:
                        print("Player 2 chooses the word")
                        word = input(f'Player 2, please enter a word: ').upper()
                        while not word.isalpha():
                            word = input("Input must be a word!\nPlease enter a word: ").upper()
                        os.system('cls')
                        print("Player 1, Time to guess!")
                    play(word)

                    while input("Would you like to play again(Y/N): ").upper() == 'Y':
                        word_selector = r.randint(1, 2)
                        if word_selector == 1:
                            print("Player 1 chooses the word")
                            word = input(f'Player 1, please enter a word: ').upper()
                            while not word.isalpha():
                                word = input("Input must be a word!\nPlease enter a word: ").upper()
                            os.system('cls')
                            print("Player 2, Time to guess!")

                        else:
                            print("Player 2 chooses the word")
                            word = input(f'Player 2, please enter a word: ').upper()
                            while not word.isalpha():
                                word = input("Input must be a word!\nPlease enter a word: ").upper()
                            os.system('cls')
                            print("Player 2, Time to guess!")
                        play(word)

                    else:
                        exit()
                else:
                    try:
                        no_of_players = int(input("Please select 1 or 2 players: "))
                    except ValueError:
                        print("PLease enter a valid number")
        except ValueError:
            print("PLease enter a valid number")


main()
