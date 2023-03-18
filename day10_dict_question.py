# Q1 : remove the list of keys from dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]
# Solution :
sample_dict.pop("name")
sample_dict.pop("salary")
print(sample_dict)
# output : {'age': 25, 'city': 'New york'}


# Q2 :rename a key -- city to  location in the following dictionary.
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

# expected :{'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}
# Solution : sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
#
sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)
