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
           
   




