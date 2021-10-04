# Task 1

a = 0

b = 0.0

c = 101

d = 1000.0

e = 1.0 * (10 ** 3)

f = 1
g = -1
h = 0

i = c + (d - f)
j = (c ** (g - g)) / d
k = j - ((d - i) * i)

q = 11.2
w = 20.11
t = 0.9
y = 12.91

p = q * w - (t + y)
n = ((w/t)**t)+y
m = ((w+q)*(t+y))-((t+q)*(w+y))

v = p * (f - c)
u = (n-m) * (c+y)
s = u*v/c

ab = float(10) / 5

del(a, b, s)  # I'll use them later
# Task 2

a = int("123")

b = float(123)

c = int(12.345)

# Task 3

number_str = input("Type card number in format: \"1234 5678 9876 5432\"\n")
number = int(number_str[15:19])
print(number)

number2 = int(input("Input a 3 digit number: "))
s = 0
s += int(number2 / 100)
s += int((number2 / 10) % 10)
s += int(number2 % 10)
print(s)
