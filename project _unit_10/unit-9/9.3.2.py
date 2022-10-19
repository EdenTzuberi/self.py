def my_mp4_playlist(file_path, new_song):
    """
    the function gets a file path that represents playlist.
    the function writes to the file, and replacing the song's name of the third line by the new_song's name.
    the function will print the file content at the end.
    :param file_path: playlist of songs, in every line: song name; artist;length of the song.
    :type file_path: file
    :param new_song: a songs name.
    :type new_song: string
    :return:
    :rtype:
    """
    playlist_file = open(file_path, "r")
    playlist = playlist_file.read()
    playlist_lines = playlist.split('\n')
    new_list = []

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

    with open(file_path, 'r') as file:
        data = file.readlines()

    if len(data) >= 3:
        artist = new_list[2][1]
        song_length = new_list[2][2]
        data[2] = new_song + ';' + artist + ';' + song_length + ';' + '\n'

        with open(file_path, 'w') as file:
            file.writelines(data)
        with open(file_path, 'r') as file:
            print('\n' + file.read())

    elif len(data) == 2:
        with open(file_path, 'a') as file:
            file.write('\n' + new_song + ';')
        with open(file_path, 'r') as file:
            print(file.read())

    elif len(data) == 1:
        file = open(file_path, 'a')
        file.write('\n')
        file.write('\n' + new_song + ';')
        file.close()
        with open(file_path, 'r') as file:
            print(file.read())


print(my_mp4_playlist(r"C:\Users\edent\OneDrive\שולחן העבודה\playlist.txt", 'Hello'))
