import numpy as np

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)

#print(numbers1)
#print(numbers2)

# result1 = numbers1 + numbers2
# result2 = numbers1 * numbers2   
# print(result2)


result3 = np.sin(numbers1)
result4 = np.sqrt(numbers1)
result5 = np.log(numbers1)
# print(result5)


multi_numbers1 = numbers1.reshape(2,3)
multi_numbers2 = numbers2.reshape(2,3)

print(multi_numbers1)
print(multi_numbers2)

result6 = np.vstack((multi_numbers1, multi_numbers2))
result7 = np.hstack((multi_numbers1, multi_numbers2))
print(result7)

result8  = numbers1 >= 50
result9 = numbers1 % 2 == 0

print(numbers1)
print(numbers1[result9])
