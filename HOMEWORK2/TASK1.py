# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input('Введите количество монет: '))
count_zero=0
count_one=0
for i in range(n):
    r = int(input('Введите 0, если решка, 1 если орёл: '))
    if r==1:
        count_one+=1
    if r==0:
        count_zero+=1
    if r!=1 and r!=0:
        print('Некорректное значение')
        break
if count_zero>=count_one:
    print(count_one,'раз(а)')
else:
    print(count_zero,'раз(а)')