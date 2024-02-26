import csv
# импортируем библиотеку
with open('songs.csv', encoding='UTF-8') as file:
    # считываем файл как список со словарями
    reader = csv.DictReader(file, delimiter=';', quotechar='"')
    songs = list(reader)[1:]
    # записываем все буква алфавита
    alphavit = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alphavit = alphavit + alphavit.upper()
    # реализуем сортировку
    russian_artists = list()
    foreign_artists = list()
    for song in songs:
        flag = True
        for i in alphavit:
            if i in song['artist_name']:
                flag = False
        if not flag:
            russian_artists.append(song['artist_name'])
        else:
            foreign_artists.append(song['artist_name'])
    print(len(russian_artists))
    print(len(foreign_artists))