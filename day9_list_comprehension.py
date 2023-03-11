# [____ for ____ in ____ ]  syntax

#
# numbers = [1, 2, 3, 4, 5]
# doubled_numbers = []
#
# for num in numbers:
#     doubled_number = num * 2
#     doubled_numbers.append(doubled_number)
#
# print(doubled_numbers) # [2, 4, 6, 8, 10]


# ***************Comprehension#################
# numbers = [1, 2, 3, 4, 5]
# # [____ for ____ in ____ ]  syntax
# doubled_numbers = [num * 2 for num in numbers]
#
# print(doubled_numbers) # [2, 4, 6, 8, 10]


################## examples

# friends = ['ashley', 'matt', 'michael']
# list1 = [friend[0].upper() for friend in friends] # ['Ashley', 'Matt', 'Michael']
# list2 = [friend.capitalize() for friend in friends] # ['Ashley', 'Matt', 'Michael']
#
# print(list1)
# print(list2)

# [bool(val) for val in [0, [], '']] # [False, False, False]
# numbers = [1, 2, 3, 4, 5]
# string_list = [str(num) for num in numbers]
# print(string_list) # ['1', '2', '3', '4', '5']

# LC with condition
# [____ for ____ in ____ if condition ]  syntax for filtering
#
numbers = [1, 2, 3, 4, 5, 6]
# evens = [num for num in numbers if num % 2 == 0]
# odds = [num for num in numbers if num % 2 != 0]
#
# print(evens)
# print(odds)

# [operation if condition else operation for ____ in __iterable/collection__  ]  syntax for filtering

list1 = [num*2 if num % 2 == 0 else num**2 for num in numbers]
print(list1)
# [num*2 for num in numbers if num % 2 == 0 else num**2 ]  ---- incorect syntax


# with_vowels = "This is so much fun!"
# ''.join(char for char in with_vowels if char not in "aeiou")
# "Ths s s mch fn!"
