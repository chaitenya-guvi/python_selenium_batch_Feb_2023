# Sets
#
# Sets are like formal mathematical sets.
# Sets do not have duplicate values --- important
# Elements in sets aren't ordered.
# You cannot access items in a set by index.
# Sets can be useful if you need to keep track of a
# collection of elements, but don't care about ordering,
# keys or values and duplicates


# # Sets cannot have duplictes
# s = set({1, 2, 3, 4, 5, 5, 5}) # {1, 2, 3, 4, 5}
#
# # Creating a new set
# s = set({1, 4, 5})
#
# # Creates a set with the same values as above
# s = {1, 4, 5}

# 4 in s
# # True
#
# 8 in s
# # False
#reference :  https://www.w3schools.com/python/python_ref_set.asp
# Set Methods
#
s = set([1, 2, 3])
s.add(4)
s.add(3)
print(s)
s.discard(5)
print(s)
# if you need to avoid KeyErrors use .discard()
# s # {1, 2, 3, 4}
# s.add(4)
# s # {1, 2, 3, 4}
# comprehension :
{x**2 for x in range(10)}

# {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}