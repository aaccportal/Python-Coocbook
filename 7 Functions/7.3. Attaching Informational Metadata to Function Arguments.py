# 7.3. Attaching Informational Metadata to Function Arguments
# 7.3. Прикрепление информационных метаданных к аргументам функции

# Problem
# You’ve written a function, but would like to attach some additional information to the
# arguments so that others know more about how a function is supposed to be used.

# Solution
# Function argument annotations can be a useful way to give programmers hints about
# how a function is supposed to be used. For example, consider the following annotated
# function:

# Проблема
# Вы написали функцию, но хотели бы добавить дополнительную информацию к
# аргументы, чтобы другие знали больше о том, как предполагается использовать функцию.

# Решение
# Аннотации аргументов функций могут быть полезным способом дать программистам подсказки о
# как предполагается использовать функцию. Например, рассмотрим следующий аннотированный
# функция:

def add(x:int, y:int) -> int:
    return x + y

# print('111')

# The Python interpreter does not attach any semantic meaning to the attached annotations.
# They are not type checks, nor do they make Python behave any differently than
# it did before. However, they might give useful hints to others reading the source code
# about what you had in mind. Third-party tools and frameworks might also attach semantic
# meaning to the annotations. They also appear in documentation:

# Интерпретатор Python не придает никакого семантического значения прикрепленным аннотациям.
# Они не являются проверками типов и не заставляют Python вести себя иначе, чем
# это было раньше. Однако они могут дать полезные подсказки другим, читающим исходный код.
# о том, что вы имели в виду. Сторонние инструменты и платформы также могут добавлять семантические
# смысл в аннотациях. Они также появляются в документации:

print(help(add))