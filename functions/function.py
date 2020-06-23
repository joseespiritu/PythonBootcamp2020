# Input Method
# In Python 2 the method input return number
# In python 3 the method input return string

"""x = input("Write the first value: ")
y = input("Write the second value: ")
z = int(x) + int(y)

print(z)"""

"""c = input("Enter the temperature in celcious: ")
c = int(c)
f = (9/5)*c + 32
print(int(f))

m = input("Enter the number of minutes: ")
s = input("Enter the number of seconds: ")
h = int(m)/60 + int(s)/3600

print(h)"""

"""def add(x, y):
    z = x + y
    return print(z)


a = input("Enter the first value: ")
b = input("Enter the second value: ")
a = int(a)
b = int(b)
add(a, b)"""


def temp(c):
    f = (9 / 5) * c + 32
    return print(f)


c = input("Write the temperature in cel: ")
c = int(c)
temp(c)


def leng(m, s=0):
    h = m / 60 + s / 3600
    return print(h)


m = input("Write the numbers of minutes: ")
m = int(m)
s = input("Write the numbers of seconds: ")
s = int(s)
leng(m, s)
