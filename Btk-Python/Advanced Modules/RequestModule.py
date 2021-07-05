import requests
import json

result = requests.get("https://jsonplaceholder.typicode.com/todos")
result = json.loads(result.text) #json veritipini python dictinoary yapısına dönüştürdük


for i in result:
    if i["userId"] == 1: 
        print(i["title"])
# #print(result[0]["title"])
# print(result)
