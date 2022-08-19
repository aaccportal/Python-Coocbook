#1.8. Calculating with Dictionaries

# Problem
# You want to perform various calculations (e.g., minimum value, maximum value, sorting,
# etc.) on a dictionary of data.

# Solution
# Consider a dictionary that maps stock names to prices:
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# In order to perform useful calculations on the dictionary contents, it is often useful to
# invert the keys and values of the dictionary using zip(). For example, here is how to
# find the minimum and maximum price and stock name:

min_price = min(zip(prices.values(), prices.keys()))
# min_price is (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys()))
# max_price is (612.78, 'AAPL')