list_1 = [[1, 2, 3], ["a", "b", 'c'], ["num1", "num2"]] # list of lists
# list_2 = [1, 2, 3, 'a', 'b', 'c', "num1", "num2"] # flatten a list using for loop
# list_1 = [[1, 2, 3], ["a", "b", 'c'], ["num1", "num2"]] # list of lists
list_2 = []


for item1 in list_1 :
    for item2 in item1:
        list_2.append(item2)

print(list_2)