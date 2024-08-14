import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


json_dict = json.loads(sampleJson)

print('salary', json_dict["company"]["employee"]["payable"]["salary"])

json_dict["company"]["employee"]["birth_date"] = 'june 21'

json_string = json.dumps(json_dict)

print(json_string)