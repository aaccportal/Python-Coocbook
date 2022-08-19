# Problem
# You want to eliminate the duplicate values in a sequence, but preserve the order of the
# remaining items.
# Solution
# If the values in the sequence are hashable, the problem can be easily solved using a set
# and a generator. For example:

# Проблема
# Вы хотите удалить повторяющиеся значения в последовательности, но сохранить порядок
# оставшиеся элементов.
# Решение
# Если значения в последовательности можно хэшировать, проблема может быть легко решена с помощью набора
# и генератора. Например:

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
list(dedupe(a))

# This only works if the items in the sequence are hashable. If you are trying to eliminate
# duplicates in a sequence of unhashable types (such as dicts), you can make a slight
# change to this recipe, as follows:

# Это работает только в том случае, если элементы в последовательности являются хэшируемыми. Если вы пытаетесь устранить
# дубликатов в последовательности нехэшируемых типов (например, dicts), вы можете сделать небольшое
# изменить на этот рецепт следующим образом:

def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)