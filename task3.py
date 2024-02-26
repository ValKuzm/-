import csv
# импортируем библиотеку
with open('songs.csv', encoding='UTF-8') as file:
    # открываем файл как список со словарями внутри
    reader = csv.DictReader(file, delimiter=';', quotechar='"')
    songs = list(reader)[1:]
    # реализуем поисковую систему
    name_artist = input()
    while name_artist != '0':
        for song in songs:
            if song['artist_name'] == name_artist:
                print(f'У {song["artist_name"]} найдена песня: {song["track_name"]}')
                break
        else:
            print('К сожалению, ничего не удалось найти')
        name_artist = input()


