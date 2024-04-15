import functions


def main():
    transactions = functions.load_transactions('operations.json') #загружаем из файла список словарей
    sorted_transactions = functions.sort_of_transactions(transactions) #сортируем транзакции
    last_operations = functions.get_five_last_transactions(sorted_transactions) #получаем 5 последних
    print('Список из 5 последних успешных операций по счету\n')
    for oper in last_operations: #Пройдемся циклом по операциям и сформируем стркои для вывода
        row_first, row_second, row_third = functions.make_up_data_to_print(oper)
        print(f'{row_first}\n{row_second}\n{row_third}\n')


if __name__ == '__main__':
    main()
