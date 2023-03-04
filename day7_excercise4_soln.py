# excercise 4 :
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]


def is_unique(list1):
    unique_list = []
    for number in list1:
        if number not in unique_list:
            unique_list.append(number)
    return unique_list

list1 = [1,2,3,3,3,3,4,5]
list2 = [1,6,8,2,3,3,3,3,4,5]

print(is_unique(list1))