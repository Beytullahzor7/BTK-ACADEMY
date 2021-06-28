"""def changeName(n):
    n = 'ada'

name = 'yigit'

changeName(name)
print(name)

def change(n):
    n[0] = 'istanbul'

sehirler = ['izmir','ankara']

change(sehirler)
print(sehirler)"""

"""def add(*params):
    return sum((params))

print(add(20,30,10))"""

def displayUsers(**args):
    for key, value in args.items():
        print('{} is {}'.format(key,value))
    
displayUsers(name = "ali", age = 21, city = "izmir")
displayUsers(name = "ayse", age = 24, city = "istanbul")
displayUsers(name = "mehmet", age = 22, city = "ankara")

