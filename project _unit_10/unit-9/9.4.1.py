def choose_word(file_path, index):
    """
    the function will choose the secret word that the player needs to guess.
    :param file_path: text file
    :type file_path: string
    :param index: the word location.
    :type index: int
    :return: a tuple that includes two elements: 1. num of different words in the file.
                                                 2. the index's word.
    :rtype tuple
    """
    file = open(file_path, "r")
    data = file.read()
    words_list = data.split(' ')                  # split the data to a list by ' '
    words_list_without_duplicates = list(dict.fromkeys(words_list))  # remove duplicates from list
    element_1 = len(words_list_without_duplicates)

    if index > len(words_list):
        element_2 = words_list[index % len(words_list) - 1]
    else:
        element_2 = words_list[index - 1]

    print(words_list)
    print(words_list_without_duplicates)
    return element_1, element_2


print(choose_word(r"C:\Users\edent\OneDrive\שולחן העבודה\words.txt", 3))