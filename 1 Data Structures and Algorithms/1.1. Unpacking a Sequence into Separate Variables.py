# 1.1. Unpacking a Sequence into Separate Variables
p = (4, 5)
x, y = p
print(x)
print(y)


print('--------')
data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, date = data
print(name)
print(shares)
print(price)
print(date)

print('--------')
name, shares, price, (year, mon, day) = data
print(name)
print(year)
print(mon)
print(day)