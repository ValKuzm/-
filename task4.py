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
    russian_artists = set()
    foreign_artists = set()
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
