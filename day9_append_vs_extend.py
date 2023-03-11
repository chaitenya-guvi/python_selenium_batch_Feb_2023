# # list
#
# first_list = [1, 2, 3, 4]
# # first_list.append(5)
#
# #
# # first_list.append(5, 6, 7, 8) # does not work!
# # print(first_list)
# first_list.append([5, 6, 7, 8])
# #
# print(first_list) # [1, 2, 3, 4,  [5, 6, 7, 8]]
# #
# correct_list = [1, 2, 3, 4]
# #
# correct_list.extend("name")
#
# #
# print(correct_list) # [1, 2, 3, 4, 5, 6, 7, 8]
# correct_list.append("name2")
# print(correct_list) # [1, 2, 3, 4, 5, 6, 7, 8]

#
# # insert
# first_list = [1, 2, 3, 4]
# #
# first_list.insert(len(first_list), 'Hi!')   # insert at a specific position
# #
# print(first_list) # [1, 2, 'Hi!', 3, 4]
#
# first_list.insert(-1, 'The end!')
#
# print(first_list) # [1, 2, 'Hi!', 3, 'The end!', 4]
#

# # pop
# Remove the item at the given position in the list, and return it.
# If no index is specified, removes & returns last item in the list.
# first_list = [1, 2, 3, 4,5]
# a= first_list.pop() # 5
# print(a)
#
# # b = first_list.pop(1) # 2
# print(first_list.pop(1))
# print(first_list)
# #
#
# remove
#Remove the first item from the list whose value is x.
# Throws a ValueError if the item is not found.

# first_list = [1, 2,4, 3, 4, 4, 4]
# # first_name = list("chaitenya")
# # first_name.remove('t')
# # print(first_name)
# first_list.remove(2)
# print(first_list) # [1, 3, 4, 4, 4]
# first_list.remove(4)
# #
# print(first_list) # [1, 3, 4, 4]
#
#
# index
# returns the index of the specified item in the list

# numbers = [5, 6, 7, 8, 9, 10]
#
# print(numbers.index(6)) # 1
# numbers.index(9) # 4
#
# first_name = list("chaitenya")
# print(first_name.index('t'))
# #
#
# # # can specify start and stop
# numbers = [5, 5, 6, 7, 5, 8,'a', 8, 9, 10]
# print(numbers.index('a')) # 0
# # print(numbers.index(5, 1)) # 1
# # print(numbers.index(5, 2)) # 4
# print(numbers[6:8])
# print(numbers.index('b', 6, 8)) # 6)
# # print(numbers[6:9])
# # print(numbers.index(10, 6, 9)) # )
#
# # reverse - reverses in place
# # first_list = [1, 2, 3, 4]
# # print(first_list[::-1])
# # print(first_list)
# # first_list.reverse()  # reverses in place
# # print(first_list) # [4, 3, 2, 1]

# join method
# technically a String method that takes an iterable argument
# concatenates (combines) a copy of the base string between each item of the iterable
# returns a new string
words = ['Coding', 'Is', 'Fun!','i' , 'wnat to learn']

print(' '.join(words)) # 'Coding is Fun!'
print(' # '.join(words)) # 'Coding is Fun!'
print(''.join(words)) # 'Coding is Fun!'