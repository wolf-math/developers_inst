# my_dictionary = {
#     "person1": {
#         "first_name": 'Rick', 
#         "last_name": 'Sanchez'
#     },
#     "person2": {
#         "first_name": "lara",
#         "last_name": "sandwich"
#     }
# }

# print("My last name is:", my_dictionary["person2"]["last_name"])

# access the value of history

# sample_dict = { 
#    "class": { 
#       "student": { 
#          "name":"Mike",
#          "marks": { 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }

# sample_dict["class"]["student"]["marks"]["physics"] = 98
# sample_dict["class"]["student"]["marks"]["coding"] = 87

# del sample_dict["class"]["student"]["marks"]["history"]

# sample_dict["class"]["student"]["name"] = "Bobby"

# print(sample_dict.items())

# sample_dict = {
#   "name": "Kelly",
#   "age": 25,
#   "salary": 8000,
#   "city": "New york"
# }

# keys_to_remove = ["name", "salary"]

# for i in keys_to_remove:
#     del sample_dict[i]

# print(sample_dict)

# for i in range(1, 3):
#     print(i)

# print('The for loop is over')

# for letter in 'Leonardo':
#     if letter == 'a':
#         break
#     print(letter, end='')


my_list = [(i*j) for i in [2, 3, 4] for j in [100, 200, 300]]
print(my_list)