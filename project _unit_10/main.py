from functions import HANGMAN_HEADER
from functions import print_hangman
from functions import show_hidden_word
from functions import choose_word
from functions import try_update_letter_guessed
from functions import check_win
from functions import print_old_letters_guessed


def main():
    HANGMAN_HEADER()
    old_letters_guesses = []
    errors = 0

    file_path = input('Enter file path: ')
    index = int(input("Enter index: "))
    secret_word = choose_word(file_path, index)

    print("let's start!")
    print_hangman(1)

    for i in range(len(secret_word)):
        print(show_hidden_word(secret_word, old_letters_guesses))
        print_hangman(errors)

        if not check_win(secret_word, old_letters_guesses):
            letter = input("insert one letter: ")
            check = try_update_letter_guessed(letter, old_letters_guesses)
            try_update_letter_guessed(letter, old_letters_guesses)
            print('\n' + '->'.join(old_letters_guesses))
            print_hangman(errors)

            if not check:
                errors += 1
                old_letters_guesses.append(letter)
                print('\n' + '->'.join(old_letters_guesses))
                print(':(')
                print_hangman(errors)

        if errors == 6:
            print('\n' + '->'.join(old_letters_guesses))
            print_hangman(errors)
            print('LOSE')
            break

        if check_win(secret_word, old_letters_guesses):
            print_hangman(errors)
            print('WIN')
            break


if __name__ == "__main__":
    main()

# C:\Users\edent\OneDrive\שולחן העבודה\words.txt
