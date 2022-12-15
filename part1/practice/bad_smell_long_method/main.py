# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users_list(csv):
    # Чтение данных из строки
    data = [{'name': line.split(';')[0], 'age': int(line.split(';')[1])} for line in csv.split('\n')]

    # Сортировка по возрасту по возрастанию
    sorted_data = sorted(data, key=(lambda x: x["age"]))

    # Фильтрация
    result_data = [person for person in sorted_data if person['age'] >= 10]

    return result_data

if __name__ == '__main__':
    print(get_users_list(csv))
