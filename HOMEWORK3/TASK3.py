# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; 
# B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. 
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, 
# либо только русские буквы.

# *Пример:*

# ноутбук
#     12

word = input('Введите слово: ')
n = word.upper()
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
point1=['A','E','I','O','U','L','N','S','T','R','А','В','Е','И','Н','О','Р','С','Т']
point2=['D','G','Д','К','Л','М','П','У']
point3=['B','C','M','P','Б','Г','Ё','Ь','Я']
point4=['F','H','V','W','Y','Й','Ы']
point5=['K','Ж','З','Х','Ц','Ч']
point8=['J','X','Ш','Э','Ю']
point10=['Q','Z','Ф','Щ','Ъ']
count=0
for i in range(len(n)):
    for j in range(len(point1)):
        if n[i]==point1[j]:
            count+=1
for i in range(len(n)):
    for j in range(len(point2)):
        if n[i]==point2[j]:
            count+=2
for i in range(len(n)):
    for j in range(len(point3)):
        if n[i]==point3[j]:
            count+=3
for i in range(len(n)):
    for j in range(len(point4)):
        if n[i]==point4[j]:
            count+=4
for i in range(len(n)):
    for j in range(len(point5)):
        if n[i]==point5[j]:
            count+=5
for i in range(len(n)):
    for j in range(len(point8)):
        if n[i]==point8[j]:
            count+=8
for i in range(len(n)):
    for j in range(len(point10)):
        if n[i]==point10[j]:
            count+=10
print(count)