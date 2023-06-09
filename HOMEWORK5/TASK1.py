# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def Degree(a,b):
    if b==1:
        return a
    if b==0:
        return 1
    if b<0:
        return '1/'+str(Degree(a,-b-1)*a)
    return Degree(a,b-1)*a

a=int(input('Введите первое число: '))
b=int(input('Введите второе число: '))
print(Degree(a,b))