string1  = "preshit"
# list1 = list(string1)
# print(list1)
# print(list1[1])
# print(list1[1:])
# print(list1[:4])
# print("xxx"*15)
# print("xxx"*15)
#  # [ start(inclusive) : stop [exclusive] : skip\step ]
# #  how to reverse a string
# print(string1[1]) # r
# print(string1[1:]) # "reshit"
# print(string1[:4]) # "p"   non inclusive of stop
print(string1[-1]) # the last alphabet
print(string1[::2]) # positive
print(string1[::-1]) # negative
# anagrams : racecar ,
anagram_string = "racecar"
non_anagram_string = "whole"
def is_anagram(string1) :
    """
    checking whwether string passed to function is an angram or not
    :param string1: string for anagram checking
    :return: True or False
    """
    return string1 == string1[::-1]

print(is_anagram(anagram_string))
print(is_anagram(non_anagram_string))

list_of_100 = [i for i in range(0,101,2)]
print(list_of_100)
