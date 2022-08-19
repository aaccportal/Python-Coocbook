#1.6. Mapping Keys to Multiple Values in a Dictionary
# Problem
# You want to make a dictionary that maps keys to more than one value (a so-called
# “multidict”).
# Solution
# A dictionary is a mapping where each key is mapped to a single value. If you want to
# map keys to multiple values, you need to store the multiple values in another container
# such as a list or set. For example, you might make dictionaries like this:

# Проблема
# Вы хотите создать словарь, который сопоставляет ключи более чем одному значению (так называемый словарь).
# «многословие»).
# Решение
# Словарь — это сопоставление, в котором каждый ключ сопоставляется с одним значением. Если ты хочешь
# сопоставьте ключи с несколькими значениями, вам нужно сохранить несколько значений в другом контейнере
# например, список или набор. Например, вы можете создать такие словари:

d = {
    'a' : [1, 2, 3],
    'b' : [4, 5]
    }
e = {
    'a' : {1, 2, 3},
    'b' : {4, 5}
}