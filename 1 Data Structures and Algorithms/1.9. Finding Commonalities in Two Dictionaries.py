#1.9. Finding Commonalities in Two Dictionaries

# Problem
# You have two dictionaries and want to find out what they might have in common (same
# keys, same values, etc.).
# Solution
# Consider two dictionaries:

a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}
b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}

# To find out what the two dictionaries have in common, simply perform common set
# operations using the keys() or items() methods. For example:

# Find keys in common
a.keys() & b.keys() # { 'x', 'y' }

# Find keys in a that are not in b
a.keys() - b.keys() # { 'z' }

# Find (key,value) pairs in common
a.items() & b.items() # { ('y', 2) }

# These kinds of operations can also be used to alter or filter dictionary contents. For
# example, suppose you want to make a new dictionary with selected keys removed. Here
# is some sample code using a dictionary comprehension:

# Make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
# c is {'x': 1, 'y': 2}