# Задача №55. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной


# 1. Создание файла. ++++
# ---------------------------
# 2. Добавление новой записи. ++++
#   * забрать ввод пользователя
#   * открытие файла на дозапись
#   * записать в файл
# ------------------------------
# 3 Вывод на экран
# * открыть файл на чтение
#   * считывание данных
#   * вывод на экран
# ------------------------------
# 4 Поиск контакта
#   * выбрать вариант поиска
#   * забрать ввод пользователя
#   * открытие файла на чтение
#   * считать данные
#   * осуществить поиск
#   * вывести результат поиска
# ------------------------------
# 5 Создание интерфейса ++++

def id_contacts():
    global id_contact

    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_str = file.read()

    contacts_list = contacts_str.rstrip().split('\n\n')
    contact_last = contacts_list[-1].replace('\n', ' ').split(' ')
    id_contact = int(contact_last[0][0]) + 1

    return id_contact

def name_input():
    return input('Введите имя: ').title()


def surname_input():
    return input('Введите фамилию: ').title()


def patronymic_input():
    return input('Введите отчество: ').title()


def phone_input():
    return input('Введите номер: ')


def address_input():
    return input('Введите адрес: ').title()


def create_contact():
    '''Add an entry'''

    next_id_contact = id_contacts()
    surname = surname_input()
    name = name_input()
    patronymic = patronymic_input()
    phone = phone_input()
    address = address_input()

    return f'{next_id_contact}. {surname} {name} {patronymic} {phone}\n{address}\n\n'


def write_contact():
    contact = create_contact()
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        file.write(contact)
        print('\nКонтакт записан!\n')


def print_contacts():
    '''List all entries'''
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        print('------------НАЧАЛО------------')
        print(file.read())
        print('------------КОНЕЦ------------')

    # 2
    # with open('phonebook.txt', 'r', encoding='utf-8') as file:
    #     contacts_list = file.read().rstrip().split('\n\n')
    #     for nn, contact in enumerate(contacts_list, 1):
    #         print(f'{nn}. {contact}\n')


    # with open('phonebook.txt', 'r', encoding='utf-8') as file:
    #     contacts_list = file.read().rstrip().split('\n\n')
    #     for nn, contact in enumerate(contacts_list, 1):
    #         print(f'{nn}. {contact}\n')


def search_contact(field=''):
    ''''''
    print(
        'Возможные варианты поиска:\n'
        '1. по фамилии\n'
        '2. по имени\n'
        '3. по отчеству\n'
        '4. по номеру\n'
        '5. по городу\n'
    )

    index_var = int(input('Введите вариант поиска: '))

    search = input('Введите данные для поиска: ')

    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_str = file.read()

    # print([data_str])
    contacts_list = contacts_str.rstrip().split('\n\n')
    # print(contacts_list)

    for contact_str in contacts_list:
        contact_list = contact_str.replace('\n', ' ').split(' ')
        if search in contact_list[index_var]:
            print(f'\n{contact_str}\n')


def favorit_contacts():

    # Простой вариант
    # print(
    #     'Возможные варианты поиска контакта для добавления в избранное:\n'
    #     '1. по фамилии\n'
    #     '2. по имени\n'
    #     '3. по отчеству\n'
    #     '4. по номеру\n'
    #     '5. по городу\n'
    # )
    #
    # index_var = int(input('Введите вариант поиска: ')) - 1
    #
    # search = input('Введите данные контакта для добавления: ')
    #
    # with open('phonebook.txt', 'r', encoding='utf-8') as file:
    #     contacts_str = file.read()
    #
    # contacts_list = contacts_str.rstrip().split('\n\n')
    #
    #
    # for contact_str in contacts_list:
    #     contact_list = contact_str.replace('\n', ' ').split(' ')
    #     if search in contact_list[index_var]:
    #         with open('favorite_contacts.txt', 'a', encoding='utf-8') as file:
    #             file.write(contact_str)
    #             print('\nКонтакт записан!\n')



    print_contacts()

    index_var = (input('Введите номер контакта для добавления в избранное: '))

    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_str = file.read()

    contacts_list = contacts_str.rstrip().split('\n\n')

    for contact_str in contacts_list:
        contact_list = contact_str.replace('\n', ' ').split(' ')
        if index_var in contact_list[0]:
            with open('favorite_contacts.txt', 'a', encoding='utf-8') as file:
                file.write(contact_str)
                file.write('\n')
                print('\nКонтакт записан!\n')



def interface():
    with open('phonebook.txt', 'a'):
        pass

    user_input = None
    while user_input != '5':
        print(
            'Возможные варианты действия:\n'
            '1. Добавить контакт\n'
            '2. Вывод списка контактов\n'
            '3. Поиск контакта\n'
            '4. Добавить контакт в избранное\n'
            '5. Выход из программы\n'
        )

        user_input = input('Введите вариант: ')

        while user_input not in ('1', '2', '3', '4', '5'):
            print('Некорректный ввод.')
            user_input = input('Введите вариант: ')

        print()

        match user_input:
            case '1':
                write_contact()
            case '2':
                print_contacts()
            case '3':
                search_contact()
            case '4':
                favorit_contacts()





if __name__ == '__main__':
    interface()

# Задача 38:  Дополнить телефонный справочник возможностью изменения
# и удаления данных(по выбору).
# Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал для изменения и удаления данных.

