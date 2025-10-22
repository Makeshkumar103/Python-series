r = 6
for i in range(1, r+1):
    print("*" * i)
print('----------------------')
for i in range(1, r+1):
    print("*" * r)  
print('----------------------')

s = 5 
for i in range(s):
    if i==0 or i==s-1:
        print("*" * s)
    else:
        print("*" + " " * (s-2) + "*")
print('------------------------')


s = 5 
for i in range(s):
    if i==0 or i==s-1:
        print("*" * s)
    else:
        print("*" + " " * (s-2) + "*")
print('------------------------')

t = 5
for i in range(t, 0,-1):
    print("*" * i)
print('------------------------')

u = 5
#upper part
for i in range(1, u+1):
    print(" " * (u + 1)+ " * " * i)
    