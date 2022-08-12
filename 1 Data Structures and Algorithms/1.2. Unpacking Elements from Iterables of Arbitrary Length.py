def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

user_record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = user_record
print(name)
print(email)

print('--------')
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)
[10, 8, 7, 1, 9, 5, 10]
print(current)

print('--------')
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]
def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

print('--------')
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(sh)
print(fields)


print('--------')
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
print(year)


print('--------')
items = [1, 10, 7, 4, 5, 9]
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head
print(sum(items))