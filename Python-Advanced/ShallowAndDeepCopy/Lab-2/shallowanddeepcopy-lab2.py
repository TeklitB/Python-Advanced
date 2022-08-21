import copy

class Delicacy:
    def __init__(self, name, price, weight):
        self.warehouse = [{'name': name, 'price': price, 'weight': weight}]
    
    def __str__(self):
        return f"{self.warehouse[0]}"


candy1 = Delicacy('Lolly Pop', 0.4, 133)

print("Original Candy")
print(candy1)

candy2 = copy.copy(candy1)
candy2.warehouse[0]["weight"] = 240

print("Shallow copy")
print("Candy-1: ", candy1)
print("Candy-1: ", id(candy1))
print("Candy-2: ", candy2)
print("Candy-2: ", id(candy2))


candy3 = copy.deepcopy(candy1)
candy3.warehouse[0]["weight"] = 140

print("Shallow copy")
print("Candy-1: ", candy1)
print("Candy-1: ", id(candy1))
print("Candy-3: ", candy3)
print("Candy-3: ", id(candy3))