# example_json = {
#     "title": "1Q84",
#     "author": "Haruki Murakami",
#     "year": 2009,
#     "read": true
# }

# example_json_array = [
#     {
#         "title": "1Q84",
#         "author": "Haruki Murakami",
#         "year": 2009,
#         "read": 'true'
#     },
#     {
#         "title": "The Picture of Dorian Gray",
#         "author": "Oscar Wilde",
#         "year": 1890,
#         "read": 'false'
#     }
# ]


import requests
from json import dump

api_or_url = "https://reqres.in/api/users/2"

a = requests.get(api_or_url)
print("The status code is " + str(a.status_code))
print(type(a.json()))
print(a.json())


# with open('data/reqres.txt','w') as fileobj :
#     dump(a, fileobj)
#  The first is that all strings, which includes key names, must use double quotes (").
#  Single quotes (') are not valid in JSON.

#  The first is that all strings, which includes
#  key names, must use double quotes ("). Single quotes (') are not valid in JSON.