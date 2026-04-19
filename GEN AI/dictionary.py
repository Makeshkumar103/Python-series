fruit = {"Mangoes": 5, "Apples": 3, "Bananas": 7, "Oranges": 2}
print(type(fruit))
print(fruit.keys())
print(fruit.values())
print(fruit["Mangoes"])
print(fruit.get("Apples"))
fruit["Grapes"] = 4
print(fruit)
fruit1= {"Pineapple": 6, "Watermelon": 8}
fruit2 = {"Strawberry": 10, "Blueberry": 12}
fruit2.update(fruit1)
print(fruit2)
fruit.pop("Oranges")
print(fruit)
fruit.clear()
print(fruit)
