"""
first_task = "Install Python"
second_task = "Learn Python"
third_task = "Take a break"


ordered collection
creating a list ,reading lists ,  updting lists ,operations
"""

# []  - empty list , the paranthesis , block paranthesis
# each item is separated by a comma


list1 = [1,2,3,4,45236] # ist of inytegers
list2 = ['a','b','c','d','e'] # list of strings
list3 = [1, 'absdsds','b',2]  # mixed list

# creating a list using range function
range_of_number  = list(range(0,51,2))
print(range_of_number)

# accessing \ reading a list

print(list3[2])
print(list3[::-1])  # reversing a list
print(list3[1:3])  # slicing a list , does not impact the original list

# accessing \ reading a list using for loop
for character in list2 :
    print(character)

# checking whether a vvalue is present in a list using in operator
print('a' in list2 )
print('aaa' in list2 )

# length of a list

# print(len(list1))



