import csv
import datetime
# импортируе библиотеки
# напишем функцию, которая сортирует список быстрой сортировкой
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    x = datetime.datetime(2002, 1, 1)
    print(song[-1])
    b1 = [song[-1] for song[-1] in arr if song[-1] < x]
    bx = [song[-1] for song[-1] in arr if song[-1] == x]
    b2 = [song[-1] for song[-1] in arr if song[-1] > x]
    return quick_sort(b1) + bx + quick_sort(b2)
# считываем файл
with open('songs.csv', encoding='UTF-8') as file:
    reader = csv.reader(file, delimiter=';', quotechar='"')
    songs = list(reader)[1:]
    for song in songs:
        song[-1] = datetime.datetime(int(song[-1][6:]), int(song[-1][3:5]), int(song[-1][:2]))
        quick_sort(songs)