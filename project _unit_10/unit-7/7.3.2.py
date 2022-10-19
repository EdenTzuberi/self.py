def check_win(secret_word, old_letters_guessed):
    """
    :param secret_word: the string presents the secret word the player needs to guess.
    :type secret_word: string
    :param old_letters_guessed: a list that includes all the old guesses of the player.
    :type old_letters_guessed: list
    :return: The function return True if all the letters consist the secret_word and for else it returns False
    :rtype: Bool
    """
    for item in secret_word:
        if item not in old_letters_guessed:
            return False
    return True