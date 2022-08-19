# 4.1. Manually Consuming an Iterator

# Problem
# You need to process items in an iterable, but for whatever reason, you can’t or don’t want
# to use a for loop.

# Solution
# To manually consume an iterable, use the next() function and write your code to catch
# the StopIteration exception. For example, this example manually reads lines from a
# file:

# Проблема
# Вам нужно обработать элементы в итерации, но по какой-то причине вы не можете или не хотите
# использовать цикл for.

# Решение
# Чтобы вручную использовать итерируемый объект, используйте функцию next() и напишите свой код для перехвата
# исключение StopIteration. Например, в этом примере вручную считываются строки из
# файл:

with open('/etc/passwd') as f:
    try:
        while True:
            line = next(f)
            print(line, end='')
    except StopIteration:
        pass