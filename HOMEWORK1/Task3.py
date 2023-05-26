# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

n=int(input('Введите номер билета: '))
count = 0
half1=n//1000
half2=n%1000
sum1=0
sum2=0
while half1>0:
    sum1+=half1%10
    half1//=10
    count+=1
while half2>0:
    sum2+=half2%10
    half2//=10
    count+=1
if count==6:
    if sum1==sum2:
        print('Билет счастливый')
    else:
        print('Билет не счастливый')
else:
    print('Число должно состоять из 6 цифр')
