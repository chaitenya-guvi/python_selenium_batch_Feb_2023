# Q1 : Get the marks for subject history  :
# sampleDict = {"class": {"student": {"name": "Mike",
#                                     "marks": {
#                                         "physics": 70,
#                                         "history": 80
#                                     }
#                                     }
#                         }
#               }
#
# print(sampleDict["class"]["student"]["name"])
# history_marks = sampleDict["class"]["student"]["marks"]["history"]
# print(f"marks of history is  : {history_marks}")
# """
# # expected output : marks of history is  : 80


# Get the key of a minimum value from the following dictionary
# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }


# expected output : Math
# 1. first access all values
# 2. get the minimum of values
# 3. print the key corresponding to min value

#
# # printing original dictionary
# print("The original dictionary is : " + str(sample_dict))
# print(sample_dict.values())
# # Using min() + list comprehension + values()
# # Finding min value keys in dictionary
# temp = min(sample_dict.values())
# print(temp)
# # res = [subject for subject in sample_dict.keys() if sample_dict[subject] == temp]
# for subject in sample_dict.keys():
#     if sample_dict[subject] == temp:
#         res = subject
#
# print(res)
#
# # printing result
# print("Keys with minimum value is : " + str(res))


# ,clear
# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
# print("The original dictionary is : " + str(sample_dict))
# # Clears all the keys and values in a dictionary:
#
# sample_dict.clear()
# print(sample_dict)
#
# # Creates key-value pairs from comma separated values:
# print({}.fromkeys("a", "b"))
# print({}.fromkeys("abcd", "1"))
#
# dict_month = {}.fromkeys(["Jan", "Feb", "Dec"], 30)
# print(dict_month)
# dict_month['Feb']=28
# print(dict_month)
# print({}.fromkeys(["email"], 'unknown'))
# # {}.fromkeys("a",[1,2,3,4,5]) # {'a': [1, 2, 3, 4, 5]}"""


# Retrieves a key in an object and return None instead of a KeyError if the key does not exist:
# d = dict(a=1,b=2,c=3)
# # print(d['e'])
# # print(d['e'])
# print(d.get('e'))
# # d['b'] # 2
# # d.get('b') # 2
# # d['no_key'] # KeyError
# # d.get('no_key') # None

# Takes a single argument corresponding to a key and removes that key-value pair from the dictionary. Returns the value corresponding to the key that was removed.
# d = dict(a=1,b=2,c=3)
# # d.pop() # TypeError: pop expected at least 1 arguments, got 0
# popped_value  = d.pop('a') # 1
# print(popped_value)
# print(d)
# # {'c': 3, 'b': 2}
# # d.pop('e') # KeyError


# Update keys and values in a dictionary with another set of key value pairs.
# first = dict(a=1,b=2,c=3,d=4,e=5)
# second = {}
#
# # second.update(first)
# # second = first.copy()
# print(second)
# second['a'] =22
# print(first)
# print(second)

# second # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
#
# # let's overwrite an existng key
# second['a'] = "AMAZING"
#
# # if we update again
# second.update(first) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
#
# # the update overrides our values
# second # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}


# Comprehension
""" the syntax

{ ____:____ for ___ in ____}

- iterates over keys by default

- to iterate over keys and values using .items() """
# numbers = dict(first=1, second=2, third=3)
# squared_numbers = {literal: numerical ** 2 for literal,numerical in numbers.items()}
# print(squared_numbers)
# print(squared_numbers) # {'first': 1, 'second': 4, 'third': 9}
# str1 = "ABC"
# str2 = "123"
# combo = {str1[i]: str2[i] for i in range(0,len(str1))}
# print(combo) # # {'A': '1', 'B': '2', 'C': '3'}
# print({num: num ** 2 for num in [1, 2, 3, 4, 5]})
# print({num: num ** 2 for num in range(1, 6)})

# conditional logic with dictionaries
print({num: ("even" if num % 2 == 0 else "odd") for num in range(1, 10)})
# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}

# Assignement :
# # convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
#
# expected : {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
