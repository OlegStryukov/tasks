a = [
    {'name':'Катя', 'surname':'Сидорова', 'gender':'Женский', 'exp':'1', 'point':[9,8,9,8,9], 'point_exam':9, 'enab': '1' },
    {'name':'Жора', 'surname':'Пупкин', 'gender':'Мужской', 'exp':'1', 'point':[9,7,6,5,4], 'point_exam':5, 'enab': '1' },
    {'name':'Коля', 'surname':'Покемонов', 'gender':'Мужской', 'exp':'0', 'point':[4,5,6,7,8] , 'point_exam':8, 'enab': '1' },
    {'name':'Лена', 'surname':'Колена', 'gender':'Женский', 'exp':'1', 'point':[9,8,9,8,9], 'point_exam':9, 'enab': '1' }
]

def point(variable,val,exam):
    sum_mid_point = 0
    counter = 0
    for solo in a:
        if solo[variable] == val:
            if exam == 0:
                mid_point_solo = sum(solo['point'])/5
                sum_mid_point += mid_point_solo
                counter +=1
            elif exam == 1:
                sum_mid_point += solo['point_exam']
                counter+=1    
    mid_point = sum_mid_point/counter
    return mid_point

def best ():
    integral_max = 0
    best_list = []
    for solo in a:
        mid_point_solo = sum(solo['point'])/5
        integral = 0.6 * mid_point_solo + 0.4 * solo['point_exam']
        if integral > integral_max:
            integral_max = integral      
    for solo in a:
        mid_point_solo = sum(solo['point'])/5
        integral = 0.6 * mid_point_solo + 0.4 * solo['point_exam']
        if integral == integral_max: 
            fullname = solo['name'] + ' ' + solo['surname']
            best_list.append(fullname)
    if len(best_list) > 1:        
        print('Лучшие студенты: ' + ', '.join([str(i) for i in best_list]) + ' ' + 'с интегральной оценкой ' + str(integral))  
    else:
        print('Лучший студент: ' + ', '.join([str(i) for i in best_list]) + ' ' + 'с интегральной оценкой ' + str(integral))         

while True:    
    instruction = ['Средняя оценка за домашние задания по группе: X',
                   'Средняя оценка за экзамен: Y',
                   'Средняя оценка за домашние задания у мужчин: A',
                   'Средняя оценка за экзамен у мужчин: B',
                   'Средняя оценка за домашние задания у женщин: C',
                   'Средняя оценка за экзамен у женщин: D',
                   'Средняя оценка за домашние задания у студентов с опытом: E',
                   'Средняя оценка за экзамен у студентов с опытом: F',
                   'Средняя оценка за домашние задания у студентов без опыта: G',
                   'Средняя оценка за экзамен у студентов без опыта: H']
    for i in instruction:
        print(i)
    select = input('Выберите команду: ')
    
    if select == 'X':
        print('Средняя оценка за домашние задания по группе: '+ str(point('enab','1',0))) 

    if select == 'Y':
        print('Средняя оценка за экзамен: ' + str(point('enab','1',1)))

    if select == 'A':
        print('Средняя оценка за домашние задания у мужчин: '+str(point('gender','Мужской',0)))  

    if select == 'B':
        print('Средняя оценка за экзамен у мужчин: '+str(point('gender','Мужской',1))) 

    if select == 'C':
        print('Средняя оценка за домашние задания у женщин: '+str(point('gender','Женский',0))) 

    if select == 'D':
        print('Средняя оценка за экзамен у женщин: '+str(point('gender','Женский',1)))
        
    if select == 'E':
         print('Средняя оценка за домашние задания у студентов с опытом: '+str(point('exp','1',0))) 

    if select == 'F':
        print('Средняя оценка за экзамен у студентов с опытом: '+str(point('exp','1',1)))  

    if select == 'G':
        print('Средняя оценка за домашние задания у студентов без опыта: '+str(point('exp','0',0))) 

    if select == 'H':
        print('Средняя оценка за экзамен у студентов без опыта: '+str(point('exp','0',1)))

    if select == '1':
        best()


    break                            