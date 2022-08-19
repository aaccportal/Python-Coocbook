# 2.19. Writing a Simple Recursive Descent Parser

# Problem
# You need to parse text according to a set of grammar rules and perform actions or build
# an abstract syntax tree representing the input. The grammar is small, so you’d prefer to
# just write the parser yourself as opposed to using some kind of framework.
# Solution
# In this problem, we’re focused on the problem of parsing text according to a particular
# grammar. In order to do this, you should probably start by having a formal specification
# of the grammar in the form of a BNF or EBNF. For example, a grammar for simple
# arithmetic expressions might look like this:

# Проблема
# Вам нужно разобрать текст в соответствии с набором правил грамматики и выполнить действия или построить
# абстрактное синтаксическое дерево, представляющее ввод. Грамматика небольшая, поэтому вы предпочитаете
# просто напишите парсер самостоятельно, а не используйте какой-то фреймворк.
# Решение
# В этой задаче мы сосредоточены на проблеме разбора текста в соответствии с определенным
# грамматика. Для этого вам, вероятно, следует начать с формальной спецификации.
# грамматики в виде BNF (Backus-Naur Form*) или EBNF (Extended Backus–Naur Form). Например, грамматика для простого
# арифметические выражения могут выглядеть так:

# *
# Расширенная форма Бэкуса — Наура (расширенная Бэкус — Наурова форма (РБНФ)) 
# (англ. Extended Backus–Naur Form (EBNF)) — формальная система определения синтаксиса, 
# в которой одни синтаксические категории последовательно определяются через другие. 
# Используется для описания контекстно-свободных формальных грамматик. 
# Предложена Никлаусом Виртом. Является расширенной переработкой форм Бэкуса — Наура, 
# отличается от БНФ более «ёмкими» конструкциями, 
# позволяющими при той же выразительной способности упростить и сократить в объёме описание.