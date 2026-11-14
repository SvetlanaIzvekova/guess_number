from random import randint

x = randint(1, 101)
print('Угадайте число от 1 до 100.')
n = 0

while n != x:
    n = int(input('Введите число: '))
    if n < x:
        print('Ваше число меньше того, что загадано')
        print('Попробуйте еще раз')
    elif x < n:
        print("Ваше число больше того, что загадано")
        print('Попробуйте еще раз') 
    else:
        print('Отличная интуиция! Вы угадали число:', x)       