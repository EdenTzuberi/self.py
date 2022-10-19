def who_is_missing(file_name):
    """
    The function looking for a number that is missing in a list of numbers that in a file path,
    and crate a new file with this number.
    :param file_name: a file path that includes a list of numbers from 1 to n, the list in the file is not sorted.
           there is one number in the list who is missing.
    :type file_name: string
    :return: None
    """
    num_list = []

    with open(file_name, "r") as file_source:
        string_of_num = (file_source.readline()).strip()
        num_list = string_of_num.split(",")
        num_list = sorted(num_list)

    i = 1

    for item in num_list:
        if int(item) == i:
            i += 1
        else:
            missing_num = i
            missing_num_file = open(r"C:\Users\edent\OneDrive\שולחן העבודה\found.txt", "w")
            missing_num_file.write(str(missing_num))
            missing_num_file.close()
            return missing_num


who_is_missing(r'C:\Users\edent\OneDrive\שולחן העבודה\findMe.txt')
