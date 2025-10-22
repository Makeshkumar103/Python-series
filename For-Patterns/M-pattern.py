#upper part
rows = 5
for i in range(1, rows + 1):
    print('#' * i + ' ' * (2 * (rows - i)) + '*' * i)
#lower part
for i in range(rows, 0, -1):
    print('#' * i + ' ' * (2 * (rows- i)) + '*' * i )
print('------------------------')

r = 6
for i in range(1, r+1):
    for j in range(1, r+1):
        if (j==1 or j==r) or (i==j and i<=r//2+1) or (i+j==r+1 and i<=r//2+1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()