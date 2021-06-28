numbers = [2,3,4,6,7,9,10]

check = lambda num: num % 2 == 0
result = list(filter(check, numbers))

print(result)