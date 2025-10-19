a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
print(a, b, c)




Values = input('Enter space separated values: ').split()
a, b, c = map(int, 
              Values)
print(a, b, c)