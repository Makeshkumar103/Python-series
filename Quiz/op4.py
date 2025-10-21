rows = int(input("enter number of rows:"))

for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j, end="")
        print(i, end="")
    print() 
# output
# enter number of rows:5    