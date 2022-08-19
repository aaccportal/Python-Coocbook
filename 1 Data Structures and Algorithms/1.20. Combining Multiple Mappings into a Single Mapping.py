# 1.20. Combining Multiple Mappings into a Single Mapping

# Problem
# You have multiple dictionaries or mappings that you want to logically combine into a
# single mapping to perform certain operations, such as looking up values or checking
# for the existence of keys.

# Solution
# Suppose you have two dictionaries:

# Проблема
# У вас есть несколько словарей или отображений, которые вы хотите логически объединить в
# одно сопоставление для выполнения определенных операций, таких как поиск значений или проверка
# на наличие ключей.

# Решение
# Предположим, у вас есть два словаря:

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

# Now suppose you want to perform lookups where you have to check both dictionaries
# (e.g., first checking in a and then in b if not found). An easy way to do this is to use the
# ChainMap class from the collections module. For example:

# Теперь предположим, что вы хотите выполнить поиск, в котором вам нужно проверить оба словаря.
# (например, сначала проверить a, а затем b, если не найдено). Простой способ сделать это — использовать
# Класс ChainMap из модуля collections. Например:

from collections import ChainMap
c = ChainMap(a,b)
print(c['x']) # Outputs 1 (from a)
print(c['y']) # Outputs 2 (from b)
print(c['z']) # Outputs 3 (from a)