# 2.1. Splitting Strings on Any of Multiple Delimiters

# Problem
# You need to split a string into fields, but the delimiters (and spacing around them) aren’t
# consistent throughout the string.

# Solution
# The split() method of string objects is really meant for very simple cases, and does
# not allow for multiple delimiters or account for possible whitespace around the delimiters.
# In cases when you need a bit more flexibility, use the re.split() method:

# Проблема
# Вам нужно разбить строку на поля, но разделители (и интервал вокруг них) не
# последовательно по всей строке.

# Решение
# Метод split() строковых объектов действительно предназначен для очень простых случаев и не
# не разрешать использовать несколько разделителей или учитывать возможные пробелы вокруг разделителей.
# В тех случаях, когда вам нужно немного больше гибкости, используйте метод re.split():