import csv
import datetime
# импортируе библиотеки
# считываем файл
with open('songs.csv', encoding='UTF-8') as file:
    reader = csv.reader(file, delimiter=';', quotechar='"')
    songs = list(reader)[1:]
    # определяем для каждого число прослушиваний исходя из данной формулы
    for song in songs:
        count_name = len(song[1])
        count_song = len(song[2])
        data_base = '01.01.2002'
        data_song = song[-1]
        raznost = abs(datetime.datetime(2002, 1, 1) - datetime.datetime(int(data_song[6:]), int(data_song[3:5]), int(data_song[:2])))
        count_streams = abs(int((str(raznost)[:4])) // (count_song + count_name))
        # там, где 0 прослушиваний вписываем число, высчитанное по формуле
        if song[0] == '0':
            song[0] = count_streams
# записываем все в новый файл
with open('songs_new.csv', 'w', encoding='UTF-8') as file:
    writer = csv.writer(file, delimiter=';', quotechar='"')
    writer.writerow(['streams', 'artist_name', 'track_name', 'date'])
    writer.writerows(songs)
# открываем новый файл, чтобы найти все песни выпущенные ранее данной даты
with open('songs_new.csv', encoding='UTF-8') as file:
    reader = csv.reader(file, delimiter=';', quotechar='"')
    songs = list(reader)[1:]
    for song in songs:
        if int(song[-1][6:]) <= 2002:
            print(f"Название песни - {song[-2]}, артист - {song[1]}, количество прослушиваний - {song[0]}")