#create a set 
beverages = {"Tea", "Coffee", "Juice"}

print(beverages)
#add more beverages 
beverages.update(["Soda", "Water"])

print(beverages)
#check if microwave exists 
mySet = {"oven", "kettle", "microwave", "refrigerator"}

print("microwave" in mySet)
#remove kettle 
mySet.remove("kettle")

print(mySet)
#loop through the set 
for item in mySet:
    print(item)
#join sets 
ages = {20, 21}

names = {"Justus", "Mayanja"}

print(ages.union(names))
#