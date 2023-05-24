def add_contact(f):
    input_name = input('Введите Имя: ')
    input_last_name = input('Введите Фамилию: ')
    input_phone = input('Введите номер телефона: ')
    data = f'{input_last_name}; {input_name}; {input_phone}'
    with open(f, 'a', encoding='utf-8') as fd:
        fd.write(f'{data}\n')
    print(f'Запись {data} добавлена')


def read_all(f):
    with open(f, 'r', encoding='utf-8') as fd:
        file_list = fd.readlines()
        return file_list


def print_all(f):
    adr_book = read_all(f)
    for line in adr_book:
        line = line.replace(';', '')
        line = line.replace('\n', '')
        print(line)


def search_contact(f):
    last_name = input('Введите фамилию для поиска: ')
    adr_book = read_all(f)
    print(len(adr_book))
    for i in range(len(adr_book)):
        print(i, adr_book[i])
    idx = int(input('Введи индекс для замены: '))
    last_name, name, _ = adr_book[idx].split('; ')
    phone = input('новый номер: ')
    new_record = f'{last_name}; {name}; {phone}'
    adr_book[idx] = new_record
    with open(f, 'w', encoding='utf-8') as fd:
        fd.writelines(adr_book)
    # for line in adr_book:
    #     if last_name in line:
    #         print(line)


def correct_contact(f):
    search = input('Введите имя или фамилию для поиска: ')
    adr_book = read_all(f)
    required_cont = 0

    for i in range(len(adr_book)):
        if search.lower() in adr_book[i].lower():
            print(f'Индекс: {i} --- {adr_book[i]}')
            required_cont+=1

    if required_cont == 0:
        print("Контактов, удовлетворяющих поиску, не найдено")
        return

    idx = int(input('Введите индекс строки для редактирования: '))

    choice = input('1 - изменить Имя \n2 - изменить Фамилию \n'
                   '3 - изменить Номер \n4 - удалить Запись: ')
    
    input_name, input_last_name, input_phone = adr_book[idx].split('; ')

    if choice == '1':
        input_name = input('Введите новое Имя: ')
    elif choice == '2':
        input_last_name = input('Введите новую Фамилию: ')
    elif choice == '3':
        input_phone = input('Введите новый Номер: ')
    elif choice == '4':
        adr_book.pop(idx)

    if choice != '4':
        new_record = f'{input_name}; {input_last_name}; {input_phone}'
        adr_book[idx] = new_record

    with open(f, 'w', encoding='utf-8') as fd:
        fd.writelines(adr_book)
        print("Справочник был изменен \n")


def main():
    file = 'address_book.txt'
    while True:
        user_choice = input('1 - добавить запись \n2 - прочитать всю тел.книгу \n'
                            '3 - найти запись \n4 - корректировать запись \nz - для выхода: ')
        if user_choice == '1':
            add_contact(file)
        elif user_choice == '2':
            print_all(file)
        elif user_choice == '3':
            search_contact(file)
        elif user_choice == '4':
            correct_contact(file)
        elif user_choice == 'z':
            print('Всего хорошего')
            break


if __name__ == '__main__':
    main()
