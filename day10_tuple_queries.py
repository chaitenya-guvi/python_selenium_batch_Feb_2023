# tuple - immutable
# ordered collection
# Tuples are faster than lists
# Some methods return them to you - like .items() when working with dictionaries
# Valid keys in a dictionary


x = (1,2,3)
# x_list = [1,2,3]
#
# x_list[0] = 4
# print(x_list)
# x[0] = "change me!" # TypeError: 'tuple' object does not support item assignment
# print(3 in x) # True

first_tuple = (1, 2, 'aa', 3, 3)
# first_tuple[1] // 2
# first_tuple[2] // 3
print(first_tuple[-1] // 3)
#
# second_tuple = tuple(5, 1, 2)
#
# second_tuple[0] # 5
# second_tuple[-1] # 2

print(first_tuple.index('aa'))