"""
List methods  :
1. append -  adding to an existing
2. extend  -
what is the difference b/w extend and append method

"""

list1 = list(range(1,6))
print(list1)

# add the number 6 to it , at the end of the list

# list1.append(6)
# print(list1)
# print(len(list1))

list2  = ['str','2','3']

list1.extend(list2)
print(list1)
print("The length after extend is : "+ str(len(list1)))

list1.append(list2)
print(list1)
print("The length after append is : "+ str(len(list1)))


