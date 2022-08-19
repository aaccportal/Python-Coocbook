# 1.19. Transforming and Reducing Data at the Same Time

# Problem
# You need to execute a reduction function (e.g., sum(), min(), max()), but first need to
# transform or filter the data.

# Solution
# A very elegant way to combine a data reduction and a transformation is to use a
# generator-expression argument. For example, if you want to calculate the sum of
# squares, do the following:

# Проблема
# Вам нужно выполнить функцию сокращения (например, sum(), min(), max()), но сначала нужно
# преобразовать или отфильтровать данные.

# Решение
# Очень элегантный способ совместить сокращение данных и преобразование состоит в использовании
# аргумент выражения-генератора. Например, если вы хотите вычислить сумму
# квадратов, сделайте следующее:

nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
print(s)

# Here are a few other examples:
# Вот еще несколько примеров:

# Determine if any .py files exist in a directory
import os
files = os.listdir('dirname')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')

# Output a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))
# Data reduction across fields of a data structure
portfolio = [
    {'name':'GOOG', 'shares': 50},
    {'name':'YHOO', 'shares': 75},
    {'name':'AOL', 'shares': 20},
    {'name':'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)