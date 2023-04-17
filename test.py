class geeks:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
 
# creating list
list = []
 
# appending instances to list
list.append(geeks('Akash', 2))
list.append(geeks('Deependra', 40))
list.append(geeks('Reaper', 44))
list.append(geeks('veer', 67))
 
# Accessing object value using a for loop
for obj in list:
    print(obj.name, obj.roll, sep=' ')
 
print("")
# Accessing individual elements
print(list)