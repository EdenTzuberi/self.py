def is_valid_input(letter_guessed):
    """
    The function is getting a letter_guessed, and return if the value is valid or 	  not (True or False)
    type letter_guessed: str
    :return: if the letter is valid or not
    :rtype: bool
    """

    if len(letter_guessed) > 1 and not (letter_guessed.isalpha()):
        return False
    elif not letter_guessed.isalpha():
        return False
    elif len(letter_guessed) > 1:
        return False
    return True