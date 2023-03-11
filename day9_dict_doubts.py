instructor = {
    "name": "Chaitenya",
    "owns_dog": True,
    "num_courses": 7,
    "favorite_language": ["Python","english"] ,
    "is_teacher": False,
    44: "my favorite number!"
}

# key value pairs

# ["Chaiteya",1,"ds",False]

# syntax --{key:value}
# keys are generally numbers, strings , or tuple - immutable data structures
# value can be anything

# how to create a dictionary

dictonary1 = dict(a=9,b=10,c=11)
print(dictonary1)

# how to access specific value from a dictionary
print(dictonary1['a'])
print(dictonary1['b'])
print(dictonary1['c'])

# values method for dictionary
print(list(dictonary1.values()))
# keys method for dictionary
print(list(dictonary1.keys()))

# items method

print(list(dictonary1.items()))

for key,value in instructor.items() :
    print(f"The key is : {key} and the value is : {value}")


# in operator
# check whether key is presnt in a dictionary , by default checks the keys

print('a' in dictonary1)
print('z' in dictonary1)

# checking whether value is presnt
print(10 in dictonary1.values())
print(3 in dictonary1.values())




