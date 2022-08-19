# 1.14. Sorting Objects Without Native Comparison Support

# Problem
# You want to sort objects of the same class, but they don’t natively support comparison
# operations.
# Solution

# The built-in sorted() function takes a key argument that can be passed a callable that
# will return some value in the object that sorted will use to compare the objects. For
# example, if you have a sequence of User instances in your application, and you want to
# sort them by their user_id attribute, you would supply a callable that takes a User
# instance as input and returns the user_id. For example:

# Проблема
# Вы хотите отсортировать объекты одного класса, но они изначально не поддерживают сравнение
# операции.

# Решение
# Встроенная функция sorted() принимает ключевой аргумент, который может быть передан вызываемому объекту, который
# вернет некоторое значение в объекте, который sorted будет использовать для сравнения объектов. За
# например, если у вас есть последовательность экземпляров User в вашем приложении, и вы хотите
# отсортируйте их по их атрибуту user_id, вы бы предоставили вызываемый объект, который принимает User
# instance в качестве входных данных и возвращает user_id. Например: