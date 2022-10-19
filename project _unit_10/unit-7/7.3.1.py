def show_hidden_word(secret_word, old_letters_guessed):
    """
    :param secret_word: the string presents the secret word the player needs to guess.
    :type secret_word: string
    :param old_letters_guessed: a list that includes all the old guesses of the player.
    :type old_letters_guessed: list
    :return: a string that consist from letters and '_'.
    :rtype: string
    """
    new_list = []
    i = 0
    while i < len(secret_word):
        new_list.append('_')
        i += 1

    j = 0
    for item in secret_word:
        if item in old_letters_guessed:
            new_list[j] = str(item)
            j += 1
        else:
            j += 1

    return str(' '.join(new_list))