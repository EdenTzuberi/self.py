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


#####################

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


#####################

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


#####################

def choose_word(file_path, index):
    """
    the function will choose the secret word that the player needs to guess.
    :param file_path: text file
    :type file_path: string
    :param index: the word location.
    :type index: int
    :return: a tuple that includes two elements: 1.num of different words in the file.  2.the index's word.
    :rtype tuple
    """
    file = open(file_path, "r")
    data = file.read()
    words_list = data.split(' ')  # split the data to a list by ' '
    words_list_without_duplicates = list(dict.fromkeys(words_list))  # remove duplicates from list
    element_1 = len(words_list_without_duplicates)

    if index > len(words_list):
        element_2 = words_list[index % len(words_list) - 1]
    else:
        element_2 = words_list[index - 1]

    return element_2


#####################

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


#######################

def HANGMAN_HEADER():
    HANGMAN_ASCII_ART = """Welcome to the game Hangman
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                          __/ |                      
                         |___/"""
    print(HANGMAN_ASCII_ART)


#######################

def print_hangman(num_of_tries):
    """
    :param num_of_tries: num of wrong guesses.
    :type num_of_tries: int
    :return: None, it's prints the hangman state that compatible to the wrong guesses.
    """
    HANGMAN_PHOTOS = {
        "picture 1":
            "x-------x",
        "picture 2":
            """x-------x
|
|
|
|
|""",
        "picture 3":
            """x-------x
|       |
|       0
|
|
|""",

        "picture 4":
            """x-------x
|       |
|       0
|       |
|
|""",

        "picture 5":
            """x-------x
|       |
|       0
|      /|\\
|
|""",

        "picture 6":
            """x-------x
|       |
|       0
|      /|\\
|      /
|""",

        "picture 7":
            """x-------x
|       |
|       0
|      /|\\
|      / \\
|"""
    }

    if num_of_tries == 1:
        print(HANGMAN_PHOTOS["picture 1"])
    elif num_of_tries == 2:
        print(HANGMAN_PHOTOS["picture 2"])
    elif num_of_tries == 3:
        print(HANGMAN_PHOTOS["picture 3"])
    elif num_of_tries == 4:
        print(HANGMAN_PHOTOS["picture 4"])
    elif num_of_tries == 5:
        print(HANGMAN_PHOTOS["picture 5"])
    elif num_of_tries == 6:
        print(HANGMAN_PHOTOS["picture 6"])
    elif num_of_tries == 7:
        print(HANGMAN_PHOTOS["picture 7"])


#######################

def print_old_letters_guessed(old_letters_guessed):
    for i in range(len(old_letters_guessed)):
        old_letters_guessed[i] = old_letters_guessed[i].lower()
    print(' -> '.join(old_letters_guessed))
