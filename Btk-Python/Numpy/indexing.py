import numpy as np

numbers = np.array([[0,5,10],[15,20,25],[50,75,85]])

result = numbers[:,0:2]
result2 = numbers[-1,:]
result3 = numbers[:3,:3]
result4 = numbers[:2,:2]

#print(result4)

arr1 = np.arange(0,10)
arr2 = arr1 #referans

arr2[0] = 20

print(arr1)
print(arr2)