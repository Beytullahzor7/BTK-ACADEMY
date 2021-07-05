#dict

import json

person_string = '{"name":"Ali", "languages":["python","C#"]}'

#JSON String to dict
#result = json.loads(person_string)

# with open("person.json") as f:
#     data = json.load(f)
#     print(data)

#JSON dict to string
person_dict = {
     "Name":"Ali",
     "Languages" : ["Python","C#"]
}

# result = json.dumps(person_dict)
# print(result)

# with open("person.json","w") as f:
#     json.dump(person_dict, f)

