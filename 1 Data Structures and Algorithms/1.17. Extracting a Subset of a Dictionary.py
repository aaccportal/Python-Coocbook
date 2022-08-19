# 1.17. Extracting a Subset of a Dictionary

# Problem
# You want to make a dictionary that is a subset of another dictionary.

# Solution
# This is easily accomplished using a dictionary comprehension. For example:

# Проблема
# Вы хотите создать словарь, являющийся подмножеством другого словаря.

# Решение
# Это легко сделать с помощью понимания словаря. Например:

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# Make a dictionary of all prices over 200
p1 = { key:value for key, value in prices.items() if value > 200 }
print(p1)