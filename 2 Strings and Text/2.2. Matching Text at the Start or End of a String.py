# 2.2. ! Matching Text at the Start or End of a String
# Совпадение текста в начале или конце строки

# Problem
# You need to check the start or end of a string for specific text patterns, such as filename
# extensions, URL schemes, and so on.

# Solution
# A simple way to check the beginning or end of a string is to use the str.starts
# with() or str.endswith() methods. For example:

# Проблема
# Вам нужно проверить начало или конец строки на наличие определенных текстовых шаблонов, таких как имя файла
# расширения, схемы URL и так далее.
# Решение
# Простой способ проверить начало или конец строки — использовать функцию str.starts.
# методы with() или str.endswith(). Например:

filename = 'spam.txt'
es = filename.endswith('.txt')
print(es)
#True

sw1 = filename.startswith('file:')
print(sw1)

#False

url = 'http://www.python.org'
sw2 = url.startswith('http:')
print(sw2)
#True