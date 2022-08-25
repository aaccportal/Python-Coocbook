#1.13. Sorting a List of Dictionaries by a Common Key

# Problem
# You have a list of dictionaries and you would like to sort the entries according to one
# or more of the dictionary values.

# Solution
# Sorting this type of structure is easy using the operator module’s itemgetter function.
# Let’s say you’ve queried a database table to get a listing of the members on your website,
# and you receive the following data structure in return:

# Проблема
# У вас есть список словарей, и вы хотите отсортировать записи по одному из них.
# или более значений словаря.

# Решение
# Сортировать структуру такого типа легко с помощью функции получения данных модуля оператора.
# Допустим, вы запросили таблицу базы данных, чтобы получить список участников на вашем веб-сайте,
# и вы получите взамен следующую структуру данных:

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

# It’s fairly easy to output these rows ordered by any of the fields common to all of the
# dictionaries. For example:

from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print('\n--------------------\n')
print(rows_by_uid)
print('\n--------------------\n')
# The preceding code would output the following:
# Предыдущий код выведет следующее:

[{'fname': 'Big', 'uid': 1004, 'lname': 'Jones'},
{'fname': 'Brian', 'uid': 1003, 'lname': 'Jones'},
{'fname': 'David', 'uid': 1002, 'lname': 'Beazley'},
{'fname': 'John', 'uid': 1001, 'lname': 'Cleese'}]

[{'fname': 'John', 'uid': 1001, 'lname': 'Cleese'},
{'fname': 'David', 'uid': 1002, 'lname': 'Beazley'},
{'fname': 'Brian', 'uid': 1003, 'lname': 'Jones'},
{'fname': 'Big', 'uid': 1004, 'lname': 'Jones'}]

# The itemgetter() function can also accept multiple keys. For example, this code
# Функция itemgetter() также может принимать несколько ключей. Например, в этом коде

rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))
print(rows_by_lfname)

# Produces output like this:
# Производит вывод следующим образом:

[{'fname': 'David', 'uid': 1002, 'lname': 'Beazley'},
{'fname': 'John', 'uid': 1001, 'lname': 'Cleese'},
{'fname': 'Big', 'uid': 1004, 'lname': 'Jones'},
{'fname': 'Brian', 'uid': 1003, 'lname': 'Jones'}]