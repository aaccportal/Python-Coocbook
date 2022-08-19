# 1.18. Mapping Names to Sequence Elements

# Problem
# You have code that accesses list or tuple elements by position, but this makes the code
# somewhat difficult to read at times. You’d also like to be less dependent on position in
# the structure, by accessing the elements by name.

# Solution
# collections.namedtuple() provides these benefits, while adding minimal overhead
# over using a normal tuple object. collections.namedtuple() is actually a factory
# method that returns a subclass of the standard Python tuple type. You feed it a type
# name, and the fields it should have, and it returns a class that you can instantiate, passing
# in values for the fields you’ve defined, and so on. For example:

# Проблема
# У вас есть код, который обращается к элементам списка или кортежа по положению, но это делает код
# иногда трудно читать. Вы также хотели бы меньше зависеть от положения в
# структуру, обращаясь к элементам по имени.

# Решение
# collections.namedtuple() обеспечивает эти преимущества, добавляя минимальные накладные расходы
# вместо использования обычного объекта кортежа. collections.namedtuple() на самом деле является фабрикой
# метод, который возвращает подкласс стандартного типа кортежа Python. Вы кормите его типом
# имя и поля, которые у него должны быть, и он возвращает класс, который вы можете создать, передав
# в значения для полей, которые вы определили, и так далее. Например: