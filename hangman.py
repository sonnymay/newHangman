import random

# List of words for the hangman game
words = ['python', 'java', 'hangman', 'computer', 'programming']

def get_word():
    """
    Select a random word from the list.
    """
    word = random.choice(words)
    return word.upper()

def play(word):
    """
    Main game loop for hangman.
    """
    word_completion = "_" * len(word)  # word to be displayed
    guessed = False
    guessed_letters = []
    attempts = 6

    print("Let's play Hangman!")
    print(display_hangman(attempts))
    print(word_completion)
    print("\n")

    while not guessed and attempts > 0:
        guess = input("Please guess a letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                attempts -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        else:
            print("Not a valid guess.")
        print(display_hangman(attempts))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of attempts. The word was " + word + ". Better luck next time!")

def display_hangman(attempts):
    """
    Display the hangman figure for the current number of attempts.
    """
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   -----
                   |   |
                       |
                       |
                       |
                       |
                """,
                """
                   -----
                   |   |
                   O   |
                       |
                       |
                       |
                """,
                """
                   -----
                   |   |
                   O   |
                   |   |
                       |
                       |
                """,
                """
                   -----
                   |   |
                   O   |
                  /|   |
                       |
                       |
                """,
                """
                   -----
                   |   |
                   O   |
                  /|\\  |
                       |
                       |
                """,
                """
                   -----
                   |   |
                   O   |
                  /|\\  |
                  /    |
                       |
                """,
                """
                   -----
                   |   |
                   O   |
                  /|\\  |
                  / \\  |
                       |
                """
    ]
    return stages[6 - attempts]

def main():
    """
    Kick off the game.
    """
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()
