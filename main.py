import functions


def main():
    transactions = functions.load_transactions('data\\operations.json')
    sorted_transactions = functions.sort_of_transactions(transactions)
    last_operations = functions.get_five_last_transactions(sorted_transactions)
    for oper in last_operations:
        row_first, row_second, row_third = functions.make_up_date_to_print(oper)
        print(f'{row_first}\n{row_second}\n{row_third}\n')


if __name__ == '__main__':
    main()
