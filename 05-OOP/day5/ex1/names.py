with open('./names.txt', 'a+') as names:
    names.seek(0)
    names_list = names.readlines()
    print(names_list)
    # Read the file line by line
    for name in names_list:
        print(name.strip())

    # Read only the 5th line of the file
    names.seek(0)
    print(names_list[4])

    # Read only the 5 first characters of the file
    names.seek(0)
    print(names[0:5])

    # Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file
    names.seek(0)
    luke = 0
    darth = 0
    lea = 0
    for name in names_list:
        if name == 'Luke':
            luke += 1
        elif name == 'Darth':
            darth += 1
        elif name == 'Lea':
            lea += 1

    print('Luke', luke, 'Leia', lea, 'Darth', darth)

    # Append your first name at the end of the file
    names.seek(0)
    names.write('Jeffery')

    # Append "SkyWalker" next to each first name "Luke"
    skywalker_list = []
    for name in names_list:
        if name == 'Luke':
            skywalker_list.append('Luke Skywalker')
        else:
            skywalker_list.append(name)

    for name in skywalker_list:
        names.write(name)

# import json

# my_family = {
#     'parents':['Beth', 'Jerry'],
#     "children":['Summer', 'Morty']
# }

# json_file = "my_file.json"

# with open(json_file, 'w') as file_obj:
#     json.dump(my_family, file_obj)

# json_my_family = json.dumps(my_family)
# print(json_my_family)