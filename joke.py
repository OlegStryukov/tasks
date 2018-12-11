time = 10
dis = input('Петрович заболел? Да/Нет: ')
if dis == 'Да':
    while time < 18 and time > 9:     
        print('Я выкапываю яму')
        print('Ожидаем')
        print('Серега закапывает')
        print('Перекур')
        time = int(input('Введите текущее время: '))
elif dis == 'Нет':
    while time < 18 and time > 9:  
        print('Я выкапываю яму')
        print('Петрович кладет туда саженец')
        print('Серега закапывает')
        print('Перекур')
        time = int(input('Введите текущее время: '))

