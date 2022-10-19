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