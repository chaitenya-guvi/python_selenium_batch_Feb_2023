import json

file_to_read = 'data/csvtojson_file.csv'

with open(file_to_read, 'r') as file_obj:
    variable1 = file_obj.read()
variable1 = variable1.splitlines()
print(variable1)
#
list1 = []
#
for itt in range(len(variable1)):
    print(variable1[itt].split(','))
    dict1 = dict(
        club=variable1[itt].split(',')[0],
        city=variable1[itt].split(',')[1],
        country=variable1[itt].split(',')[2]
    )
#
    list1.append(dict1)
#
file_to_write = 'data/json_file.txt'
with open(file_to_write, 'w') as file_obj:
    json.dump(list1, file_obj)
#
