# excercise 4 :
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]
# even list  : [2,4]



def is_even_num(list1):
    even_num = []
    for number in list1:
        if number % 2 == 0:
            even_num.append(number)
    return even_num


list1 = [1,2,3,3,3,3,4,5]
list2 = [1,6,8,2,3,3,3,3,4,5]

print(is_even_num(list2))