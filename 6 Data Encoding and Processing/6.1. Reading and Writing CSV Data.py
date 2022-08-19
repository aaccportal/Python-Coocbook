# 6.1. Reading and Writing CSV Data

# Problem
# You want to read or write data encoded as a CSV file.

# Solution
# For most kinds of CSV data, use the csv library. For example, suppose you have some
# stock market data in a file named stocks.csv like this:

# Проблема
# Вы хотите прочитать или записать данные, закодированные в файл CSV.

# Решение
# Для большинства типов данных CSV используйте библиотеку csv. Например, предположим, что у вас есть несколько
# данные фондового рынка в файле с именем stocks.csv примерно так:

import csv
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        print(row)