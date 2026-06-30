#display second item 
x = ("samsung", "iphone", "tecno", "redmi")
print(x[1])
#display the second last item 
print(x[-2])
# change iphone to itel
phones = list(x)

phones[1] = "itel"

x = tuple(phones)

print(x)
#add huawei 
x = x + ("Huawei",)

print(x)
#loop through the tuple 
for phone in x:
    print(phone)
#remove the first item 
x = x[1:]

print(x)
#create tuple of cities 
cities = ("Kampala", "Gulu", "Mbarara", "Jinja")
# unpack the tuple
a, b, c, d = cities

print(a)
print(b)
print(c)
print(d)
# display items 2 to 3 
print(cities[1:4])
#join tuples 
first = ("Justus",)
second = ("Mayanja",)

print(first + second)
#multiply tuples by 3 
colors = ("red", "blue", "green")

print(colors * 3)
#count by 8 seconds 
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

print(thistuple.count(8))

