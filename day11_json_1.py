# https://jsonlint.com/  - read about json
import json

# with open('data/friends_json.txt', 'r') as fileobj:
#     file_contents = json.load(fileobj)  # reads file and turns it to dictionary , deserialialization
#
# print(file_contents)
# print(type(file_contents))
#
# print(file_contents['friends'][0]['name'])
#
#
# cars = [
#     {"make": 'Ford', 'model': 'Fiesta'},
#     {'make': 'Ford', 'model': 'Focus'}
# ]
# #
# with open('data/cars_json.txt', 'w') as file:
#     json.dump(cars, file)
# #
#
my_json_string = '[{"name": "Alfa Romeo", "released": 1950}]'
#
incorrect_car = json.loads(my_json_string)

print(type(incorrect_car))
print(incorrect_car[0]['name'])
