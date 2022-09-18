import math as m
def check():
    while True:
        try:
            k = int(input())
            return k
        except ValueError:
            print('Ошибка. Пожалуйста, повторите ввод: ')

def act(x,y,n):
    if n==1:
        return x+y
    elif n==2:
        return x-y
    elif n==3:
        return x*y
    elif n==4:
        return x/y
def func(x,y,n):
    if n==1:
        return m.e**(x+y)
    elif n==2:
        return m.sin(x+y)
    elif n==3:
        return m.cos(x+y)
    elif n==4:
        return x**y
print('Введите первое число (делимое\уменьшаемое):')
x = check()
print('Введите второе число (делитель\уменьшаемое):')
y = check()
print('Выбирите действие:','\n','1-Арифметические действия','\n','2-Рассчет функций')
z=check()
if z==1:
    print('Выбирите действие:','\n','1-Сложение','\n','2-Вычитание','\n','3-Умножение','\n','4-Деление')
    n=check()
    res= act(x,y,n)
    print (res)
elif z==2:
    print('Выбирите функцию:','\n', '1-e^(x+y)','\n','2-sin(x+y)','\n','3-cos(x+y)','\n','4-x^y')
    n=check()
    res= func(x,y,n)
    print (res)