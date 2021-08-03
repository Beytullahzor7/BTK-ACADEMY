import numpy as np
from numpy.core.fromnumeric import size
from numpy.lib.function_base import average

result1 = np.array([1,3,5,7,9])
result2 = np.arange(1,10) #verilen aralıklarla liste olusturma
result3 = np.arange(10,100,3) # artma aralıgını belirtmek
result4 = np.zeros(10) #Sadece 0 lardan olusan liste
result5 = np.ones(5) #Sadece 1 lardan olusan liste
result6 = np.linspace(0,100,5) #baslangıc ve bitiş değerini 5 eşit aralıga böler
result7 = np.random.randint(0,10) # baslangıc ve bitis degerini veririz random sayı üretir
result8 = np.random.randint(20) #sadece bitiş değerini veririz en yüksek sayı 20 olacak sekilde rasgele bir sayı üretir
result9 = np.random.randint(50, size=5) #max değeri 50 olan 5 tane sayı üret
result10 = np.random.rand(5) #0-1 aralıgında 5 sayı üretimi

np_array = np.arange(50)
np_multi = np_array.reshape(5,10)

rnd_numbers = np.random.randint(1,100,10)
print(rnd_numbers)
max_numbers = rnd_numbers.max()
min_numbers = rnd_numbers.min()
average = rnd_numbers.mean()
indexnumber = rnd_numbers.argmax() #üretilen en büyük sayının index numarasını verir
indexnumber2 = rnd_numbers.argmin()
print(indexnumber2) #üretilen en küçük sayının index numarasını verir
