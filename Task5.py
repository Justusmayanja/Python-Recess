#display shoe size 
x = 'All "Data Scientists" are cool!'

print(x)
#change brand 
x = 'All "Data Scientists" are cool!'

print(x)
#add type 
Shoes["type"] = "sneakers"

print(Shoes)
#return keys 
print(Shoes.keys())
#return values
print(Shoes.values())
#check if size exists 
print("size" in Shoes)
#loop through the dictionary
for key, value in Shoes.items():
    print(key, value)
#remove colour 
Shoes.pop("color")

print(Shoes)
#empty dictonary 
Shoes.pop("color")

print(Shoes)
#copy dictonary 
student = {
    "name": "Justus",
    "age": 21
}

student_copy = student.copy()

print(student_copy)
#nested dictionary
students = {
    "student1": {
        "name": "John",
        "age": 20
    },
    "student2": {
        "name": "Mary",
        "age": 22
    }
}

print(students)
