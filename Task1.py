#list of 5 people and access the second 
people = ["John", "Peter", "Mary", "Sarah", "David"]
print(people[1])
#Change the first item
people[0] = "James"
print(people)
# change the 6Th item 
people.append("Brian")
print(people)
#add the third person 
people.insert(2, "Bathel")
print(people)
#remove the forth item 
people.insert(2, "Bathel")
print(people)
#display the last item 
print(people[-1])
#display items from 3 to 5 
items = ["A", "B", "C", "D", "E", "F", "G"]
print(items[2:5])
#coppy a list 
countries = ["Uganda", "Kenya", "Tanzania"]
countries_copy = countries.copy()
print(countries_copy)
#loop through the list 
for country in countries:
    print(country)
    #sort the list 
    animals = ["cat", "dog", "zebra", "ant"]

animals.sort()
print(animals)

animals.sort(reverse=True)
print(animals)
#output animals containing a 
for animal in animals:
    if "a" in animal:
        print(animal)
# join two items 
first = ["Justus"]
second = ["Mayanja"]

names = first + second
print(names)
