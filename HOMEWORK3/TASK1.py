# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

from random import randint
n = int(input('Введите размер массива: '))
list = [randint(1,10) for i in range(n)]
print(list)
x = int(input('Введите искомое значение: '))
count = 0
for i in range(n):
    if x==list[i]:
        count+=1
print(f'Число {x} встречается {count} раз(а)')