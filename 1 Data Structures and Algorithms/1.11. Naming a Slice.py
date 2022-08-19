#1.11. Naming a Slice

# Problem
# Your program has become an unreadable mess of hardcoded slice indices and you want
# to clean it up.
# Solution
# Suppose you have some code that is pulling specific data fields out of a record string
# with fixed fields (e.g., from a flat file or similar format):

# Проблема
# Ваша программа превратилась в нечитаемый беспорядок из жестко запрограммированных индексов слайсов, и вы хотите
#  очистить его.
# Решение
# Предположим, у вас есть код, который извлекает определенные поля данных из строки записи.
# с фиксированными полями (например, из плоского файла или аналогичного формата):

###### 0123456789012345678901234567890123456789012345678901234567890'
record = '....................100            .......513.25          ..........'
#cost = int(record[20:32]) * float(record[40:48])

# Instead of doing that, why not name the slices like this?

SHARES = slice(20,32)
PRICE = slice(40,48)
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)