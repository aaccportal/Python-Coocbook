# 2.17. Handling HTML and XML Entities in Text
# 2.17. Обработка объектов HTML и XML в тексте

# Problem
# You want to replace HTML or XML entities such as &entity; or &#code; with their
# corresponding text. Alternatively, you need to produce text, but escape certain characters
# (e.g., <, >, or &).

# Solution
# If you are producing text, replacing special characters such as < or > is relatively easy if
# you use the html.escape() function. For example:

# Проблема
# Вы хотите заменить объекты HTML или XML, такие как &entity; или &#code; с их
# соответствующим текстом. В качестве альтернативы вам нужно создать текст, но экранировать определенные символы
# (например, <, > или &).
# Решение
# Если вы создаете текст, замена специальных символов, таких как < или >, относительно проста, если
# вы используете функцию html.escape(). Например: