def get_value():
    while True:
        try:
            X = int(input('Введите число: '))
            return X
        except ValueError:
            print('Ошибка. Пожалуйста, повторите ввод: ')

x=get_value()
if x<-5:
    print('(-infinity,-5)')
elif x>5:
    print('(5,+infinity)')
else:
    print('[-5,5]')