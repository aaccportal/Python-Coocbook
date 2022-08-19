# 1.15. Grouping Records Together Based on a Field

# Problem
# You have a sequence of dictionaries or instances and you want to iterate over the data
# in groups based on the value of a particular field, such as date.

# Solution
# The itertools.groupby() function is particularly useful for grouping data together
# like this. To illustrate, suppose you have the following list of dictionaries:

# Проблема
# У вас есть последовательность словарей или экземпляров, и вы хотите перебрать данные
# в группах на основе значения определенного поля, например даты.

# Решение
# Функция itertools.groupby() особенно полезна для группировки данных.
# как это. Для иллюстрации предположим, что у вас есть следующий список словарей:

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

# Now suppose you want to iterate over the data in chunks grouped by date. To do it, first
# sort by the desired field (in this case, date) and then use itertools.groupby():

# Теперь предположим, что вы хотите перебрать данные в блоках, сгруппированных по дате. Чтобы сделать это, сначала
# отсортируйте по нужному полю (в данном случае по дате), а затем используйте itertools.groupby():

from operator import itemgetter
from itertools import groupby
# Sort by the desired field first
rows.sort(key=itemgetter('date'))
# Iterate in groups
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)