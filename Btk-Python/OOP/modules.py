import random

result = random.random()
result2 = random.randint(1,10)

#print(result2)

names = ["ali","ahmet","fatma","ayse"]

result3 = names[random.randint(0,len(names)-1)]
result4 = random.choice(names)
result5 = random.sample(names, 2)

print(result5)

liste = list(range(10))
random.shuffle(liste)
print(liste)