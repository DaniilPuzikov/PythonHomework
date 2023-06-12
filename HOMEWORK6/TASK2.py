# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def Find_index(min,max,list1,index):
    for i in range(len(list1)):
        if min<=list1[i]<=max:
            index.append(i)


from random import randint
size = int(input('Введите размер списка: '))
list1 = [randint(1,20) for i in range (size)]
print(list1)
min = int(input('Введите минимальное значение диапазона: '))
max = int(input('Введите максимальное значение диапазона: '))
index = list()
Find_index(min,max,list1,index)
print(index)