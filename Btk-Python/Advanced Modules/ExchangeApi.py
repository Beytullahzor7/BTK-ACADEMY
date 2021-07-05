import requests
import json

url = "http://api.exchangeratesapi.io/v1/latest?access_key=cc31322101c6588a556c8a43544b2f20&format=1"

bozulan_doviz = input("Bozulan Döviz Türü : ")
alınan_doviz = input("Alınan Döviz Türü : ")
miktar = int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz : "))


result = requests.get(url + bozulan_doviz)
result = json.loads(result.text)

print("1 {0} = {1} {2} ".format(bozulan_doviz, result["rates"][alınan_doviz], alınan_doviz))
print("{0} {1} = {2} {3}".format(miktar, bozulan_doviz, miktar * result["rates"][alınan_doviz], alınan_doviz))

