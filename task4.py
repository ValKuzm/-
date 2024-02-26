import csv
# импортируем библиотеку
russian_artists = [el for el in open('russian_artists.txt']
    songs = russian_artists + foreign_artists
    # записываем все буква алфавита
    alphavit = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alphavit = alphavit + alphavit.upper()
    # реализуем сортировку
    foreign_artists = [el for el in open(foreign_artists.txt']
    for song in songs:
        flag = True
        for i in alphavit:
            if i in song['artist_name']:
                flag = False
        if not flag:
            russian_artists.add(song['artist_name'])
        else:
            foreign_artists.add(song['artist_name'])
    print(len(list(russian_artists)))
    print(len(list(foreign_artists)))
