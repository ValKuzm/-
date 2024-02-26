import csv
# импортируе библиотеку
# реализуем функцию, которая присваивает к строке числовое значение, возвращает количество песен
def create_hash(artist_name, arrs):
    count_songs = 0
    song_info = set()
    for arr in arrs:
        if arr["artist_name"] == artist_name:
            if arr["track_name"] not in song_info:
                song_info.add(arr["track_name"])
                count_songs += 1
            else:
                continue
    return count_songs

# считываем файл как список со словарями
with open('songs.csv', encoding='UTF-8') as file:
    reader = csv.DictReader(file, delimiter=';', quotechar='"')
    songs = list(reader)[1:]
    for i in range(10):
        print(create_hash(input(), songs))