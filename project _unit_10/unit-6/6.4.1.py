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