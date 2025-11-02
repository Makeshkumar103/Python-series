#name= input("whats your name:")
#print("hello " + name)
height = input("Whats your height: ")
print(type(height))
print ("you are " + height + "cm")
inch = int(height)/2.54
print(" you are " + str(inch) + " inches tall")

""" Anothe example """
height = float(input("Whats your height: "))
height_inches = "{:.2f}".format(height/2.54)
print(type(height))
print ("you are " + str(height) + "cm")
print(" you are " + height_inches + " inches tall")
