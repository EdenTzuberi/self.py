from functions import HANGMAN_HEADER
from functions import print_hangman
from functions import show_hidden_word
from functions import choose_word
from functions import try_update_letter_guessed
from functions import check_win
import random


def main():
    HANGMAN_HEADER()
    old_letters_guesses = []
    errors = 1

    # file_path = input('Enter file path: ')
    file_path = r'C:\Users\edent\OneDrive\שולחן העבודה\words.txt'
    # index = int(input("Enter index: "))
    index = random.randint(1, 100)
    secret_word = choose_word(file_path, index)

    print("let's start!" + '\n')
    print(show_hidden_word(secret_word, old_letters_guesses))

    for i in range(8):
        letter = input("insert one letter: ")

        if letter not in secret_word:
            if try_update_letter_guessed(letter, old_letters_guesses):
                old_letters_guesses = try_update_letter_guessed(letter, old_letters_guesses)
            print('->'.join(old_letters_guesses))
            print(show_hidden_word(secret_word, old_letters_guesses))
            print(':(')
            print_hangman(errors)
            errors += 1

            if errors == 7 or len(old_letters_guesses) == 8:
                print('->'.join(old_letters_guesses))
                print_hangman(errors)
                print('LOSE')
                print("the secret word: " + "'" + secret_word + "'")
                break

        if letter in secret_word:
            if try_update_letter_guessed(letter, old_letters_guesses):
                old_letters_guesses = try_update_letter_guessed(letter, old_letters_guesses)
            print(show_hidden_word(secret_word, old_letters_guesses))
            print('->'.join(old_letters_guesses))

            if check_win(secret_word, old_letters_guesses):
                print('WIN')
                print('->'.join(old_letters_guesses))
                print("the secret word: " + "'" + secret_word + "'")
                break

    print("\n thanks for playing HANGMAN!")


if __name__ == "__main__":
    main()

# C:\Users\edent\OneDrive\שולחן העבודה\words.txt
