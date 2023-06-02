# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5


from random import randint
n = int(input('Введите размер массива: '))
list = [randint(1,10) for i in range(n)]
print(list)
x = int(input('Введите значение: '))
close_num=0
close_dif=1000
for i in range(n):
    if abs(x-list[i])<close_dif:
        close_dif=abs(x-list[i])
        close_num=list[i]
print(close_num)