def check_valid_input(letter_guessed, old_letters_guessed):
    """
    :param letter_guessed: a string that represents the character that the player inserts.
    :param old_letters_guessed:a list, that includes old guesses of the player.
    :return: False or True that represents the string quality and if letter already guessed.
    :rtype: bool
    """
    if len(letter_guessed) >= 2 or not letter_guessed.isalpha() or letter_guessed.lower() in old_letters_guessed:
        return False
    return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    :param letter_guessed: a string that represents the character that the player inserts.
    :param old_letters_guessed: a list that represents the player's guesses.
    :return: Bool
    """
    old_letters_guessed = sorted(old_letters_guessed, key=str.lower)
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True  # the letter was added to the list successfully.

    else:
        print('X')
        for i in range(len(old_letters_guessed)):
            old_letters_guessed[i] = old_letters_guessed[i].lower()
        print(' -> '.join(old_letters_guessed))
        return False  # the letter wasn't added to the list successfully.