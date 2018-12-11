#Задача №1
#Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:

#p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
#l – list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
#s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
#a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
#Внимание: p, s, l, a - это пользовательские команды, а не названия функций. Функции должны иметь выразительное название, передающие её действие.

#Задача №2
#Почитать про lambda-функции. И что такое *args и **kwargs.

#Задача №3.
#d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
#m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
#as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень;




documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }

def name (num):
   for i in range(len(documents)):
        if documents[i]['number'] == num:
            return documents[i]['name']
def passport ():
     for i in range(len(documents)):
        if documents[i]['type'] == 'passport':
            return 'Passport '+ documents[i]['number'] +' '+ documents[i]['name']
def shelf (num):
    for key, itemlist in directories.items():
        for item in itemlist:
            if num == item:
                return key
def adding():
    tmpdictdoc = {}
    tmpdictdoc['type'] = input('Введите тип документа: ')
    tmpdictdoc['number'] = input('Введите номер документа: ')
    tmpdictdoc['name'] = input('Укажите фамилию и имя: ')
    documents.append(tmpdictdoc)    
    direct = input('Введите номер полки: ')
    directories[direct].append(tmpdictdoc['number']) 
    tmpdictdoc.clear()

def delete (number):
    for i in range(len(documents)):
        if documents[i]['number'] == number:
            documents[i]['number'] = 'Номер удален'
    for key, item in directories.items():
        if number in item:
            item.remove(number)


def moving ():
    number_doc = input('Введите номер документа: ')
    number_shelf = input('Введите номер целевой полки: ')
    for item in directories.values():
        if number_doc in item:
            item.remove(number_doc)
    directories[number_shelf].append(number_doc)

def add_shelf():
    number_shelf = input('Введите номер полки: ')
    if number_shelf in directories:
        print('Такая полка уже есть')
    else:
        directories[number_shelf] = []
    print(directories)                                

                   



operation = input('Введите команду: (p – people, l - list, s – shelf), a – add, d - delete, m - moving: ')

if operation == 'p':
    num = input('Введите номер документа: ')
    print(name(num))

if operation == 'l':
    print(passport())

if operation == 's':
    num = input('Введите номер документа: ')
    print(shelf(num))

if operation == 'a':
    adding()
    print(directories) 

if operation == 'd':
    number = input('Введите номер документа: ')
    delete(number)
    print(directories)
    print(documents) 

if operation == 'm':
    moving() 
    print(directories)

if operation == 'as':
    add_shelf() 
           
   




