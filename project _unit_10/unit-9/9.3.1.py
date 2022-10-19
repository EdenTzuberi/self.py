def my_mp3_playlist(file_path):
    """
    the function gets a file path that represents playlist. the function return a tuple that:
    it's first element presents the longest song in the file
    the second element presents the number of songs in the file
    the third element presents the artist that appears more than once in the file (guess there is only one artist).
    :param file_path: playlist of songs, in every line: song name; artist;length of the song.
    :type file_path: file
    :return: tuple that includes three elements as mention above.
    :rtype: tuple
    """
    playlist_file = open(file_path, "r")
    playlist = playlist_file.read()
    playlist_file.close()
    playlist_lines = playlist.split('\n')
    new_list = []
    r_tuple = ()
    time_list = []

    i = 0
    for item in playlist_lines:
        new_list.append(playlist_lines[i].split(';'))
        i += 1
    (new_list[0]).remove('')

    j = 0
    for item in new_list:
        if '' in item:
            (new_list[j]).remove('')
        j += 1

    max_minutes = 0
    max_seconds = 0

    for item in new_list:
        time_list.append(item[-1].split(':'))

    for item in time_list:
        if max_minutes <= int(item[0]) and max_seconds <= int(item[1]):
            max_minutes = int(item[0])
            max_seconds = int(item[1])
            max_length = str(max_minutes) + ':' + str(max_seconds)

    for item in new_list:
        if max_length in item:
            element_1 = item[0]

    element_2 = len(new_list)

    for item_1 in new_list:
        for item_2 in new_list:
            if item_1[1] == item_2[1]:
                artist_name = item_1[1]
                break
    element_3 = artist_name

    return element_1, element_2, element_3


print(my_mp3_playlist(r"C:\Users\edent\OneDrive\שולחן העבודה\playlist.txt"))
