a=10
b=10

if b>a:
    print ("B is Greater than A")

if a>b:
    print ("A is Greater than B")

if b>a:
    print ("B is Greater than A")

else:
    print ("A is Greater than B")

c=30
if (a>b) & (a>c):
    print("A is greatest")
if (b>a) & (b>c):
    print ("B is Greatest")
else:
    print ("C is Greatest")

print("Tuples")
tup1 =("a",'b','c')
if 'a' in tup1:
    print("a is present in tup1")
else:
    print ("a is not present in tup1")

print("List") 
                                                                                       
l1= ['a','b','c']
if l1[0]=='a':
    l1[0]=100
print (l1)

d1={'k1':10, 'k2':20, 'k3':30}
if d1["k1"]==10:
    d1['k1']=d1["k1"]+100
print(d1)