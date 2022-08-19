# 5.1. Reading and Writing Text Data

# Problem
# You need to read or write text data, possibly in different text encodings such as ASCII,
# UTF-8, or UTF-16.

# Solution
# Use the open() function with mode rt to read a text file. For example:

# Read the entire file as a single string
with open('somefile.txt', 'rt') as f:
    data = f.read()

# Iterate over the lines of the file
with open('somefile.txt', 'rt') as f:
    for line in f:
        print(line)
        # process line

# Write chunks of text data
text1 = 'text1'
with open('somefile.txt', 'wt') as f:
    f.write(text1)