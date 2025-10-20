# swap 2 variables in Python
a, b = 5, 10
a, b = b, a
print("a =", a)  # Output: a = 10
print("b =", b)  # Output: b = 5

# swap 2 variables get input from user
x = int(input("Enter first variable x: "))  
y = int(input("Enter second variable y: "))
x, y = y, x 
print("x =", x)
print("y =", y)

# to swap 2 variables without a temporary variable
x = 15  
y = 25
x = x + y
y = x - y
x = x - y
print("x =", x)  # Output: x = 25
print("y =", y)  # Output: y = 15


# to swap 2 variables using XOR bitwise operation
m = 7
n = 12
m = m ^ n
n = m ^ n
m = m ^ n
print("m =", m)  # Output: m = 12
print("n =", n)  # Output: n = 7
# to swap 2 variables using a temporary variable
temp = a
a = b
b = temp    
print("a =", a)  # Output: a = 5
print("b =", b)  # Output: b = 10


