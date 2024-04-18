import json
import datetime
import os

def load_transactions(file_name):
    '''
    Функция открывает файл с данными по операциям
    и возвращает в виде списка словарей
    '''
    path_to_root = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(path_to_root, rf'data\{file_name}')
    with open(path, 'r', encoding="utf-8") as file:
        transactions = json.load(file)
        return transactions

def sort_of_transactions(transactions):
    '''
    Функция отфильтровывает пустые элементы словаря,
    операции со статусом 'CANCELED' и сортирует элементы по дате
    '''
    trans = list()
    for item in transactions:
        if item and item['state'] == "EXECUTED":
            trans.append(item)
    transactions = sorted(trans, key=lambda item: datetime.datetime.fromisoformat(item['date']))
    return transactions

def get_five_last_transactions(transactions):
    '''
    Функция получает из списка операций последние 5 в обратном порядке
    '''
    operations = transactions[-1:-6:-1]
    return operations

def make_up_data_to_print(oper):
    '''
    Функция формирует и возвращает три строки для вывода данных по операции
    '''
    row_first, row_second, row_third  = '', '', ''
    #Получим дату из строки формата ISO и отсечем время
    if check_key_is_exist(oper, 'date'):
        #Конвертируем дату из формата ISO строки в объект datetime и отсекаем время
        date = datetime.datetime.fromisoformat(oper['date']).date()
        date = date.strftime("%d.%m.%Y")
    else:
        date = 'Нет данных'
    #Проверяем наличие данных в операции и формируем первую строку для вывода
    if check_key_is_exist(oper, 'description'):
        row_first = f'{date} {oper['description']}'
    if check_key_is_exist(oper, 'from'): #Проверим наличие поля "откуда" в операции и вставим в строку
        row_second = make_up_string(oper, 'from')
    else:
        row_second = 'Нет данных'
    row_second = row_second + ' -> '
    if check_key_is_exist(oper, 'to'): #Проверяем наличие поля "куда" в операции м вставляем в строку
        to_string = make_up_string(oper, 'to')
        row_second = row_second + to_string
    else:
        to_string = 'Нет данных'
        row_second = row_second + to_string
    if check_key_is_exist(oper, 'operationAmount'): #Проверим наличие поля "сумма" и сформируем строку для вывода
        oper_amount = oper['operationAmount']
        if check_key_is_exist(oper_amount, 'amount'):
            row_third = oper_amount['amount']
        if check_key_is_exist(oper_amount, 'currency'):
            row_third = row_third + ' ' + oper_amount['currency']['name']
    return row_first, row_second, row_third

def make_up_string(oper, direction):
    '''
    Функция формирует строку с данными счета или карты,
    проверяя наличие подстроки 'Счет' в данных из операции
    '''
    from_to_item = oper[direction]
    if from_to_item.find('Счет') >= 0: #Проверяем, являются ли данные счетом или картой
        count_string = make_up_count_string(from_to_item)
        return count_string
    else:
        card_string = make_up_card_string(from_to_item)
        return card_string


def make_up_count_string(count_string):
    '''
    Функция формирует строку с данными банковского счёта
    '''
    count_string = count_string[:4] + ' **' + count_string[-4:]
    return count_string

def make_up_card_string(card_string):
    '''
    Функция формирует строку с данными банковской карты
    '''
    card_list = card_string.split(' ')
    card_number = card_list[-1]
    start = card_string.find(card_number)
    card_number = card_number[:4] + ' ' + card_number[4:6] + '** **** ' + card_number[-4:]
    card_string = card_string[:start] + card_number
    return card_string

def check_key_is_exist(oper, key):
    '''
    Функция проверяет наличие ключа в словаре
    '''
    return key in oper
