#1.12. Determining the Most Frequently Occurring Items ina Sequence

# Problem
# You have a sequence of items, and you’d like to determine the most frequently occurring
# items in the sequence.

# Solution
# The collections.Counter class is designed for just such a problem. It even comes with
# a handy most_common() method that will give you the answer.
# To illustrate, let’s say you have a list of words and you want to find out which words
# occur most often. Here’s how you would do it:

# Проблема
# У вас есть последовательность элементов, и вы хотите определить наиболее часто встречающиеся
# элементы в последовательности.

# Решение
# Класс collections.Counter предназначен именно для такой задачи. Это даже идет с
# удобный метод most_common(), который даст вам ответ.
# Для иллюстрации предположим, что у вас есть список слов, и вы хотите выяснить, какие слова
# встречаются чаще всего. Вот как это сделать:

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)