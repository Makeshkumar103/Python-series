# print('Hello Python')
import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '1234567890'
symbols = '[]{}()*/;,_-'
all = lower+upper+numbers+symbols
length = 16
password ="".join(random.sample(all,length))
a = 5
b = 2
c = a / b
d = a // b
x = 6
if x!=1:
    print("How are You")
else:
    print("hi you")

print(password)
print(c)
print(d)