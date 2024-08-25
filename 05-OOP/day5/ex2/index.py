import json

with open('file.json', 'r') as file:
    family = json.load(file)


for child in family['children']:
    print(f"Name: {child['firstName']}, Age: {child['age']}")

family['children'][0]['favoriteColor'] = 'blue'
family['children'][1]['favoriteColor'] = 'green'

with open('file.json', 'w') as file:
    json.dump(family, file, indent=2, sort_keys=True)