import pandas as pd
import numpy as np


#Her bir liste içerisindeki veri aynı tipte olmak zorunda değildir
#data
numbers = [20,30,40,50]
letters = ['a','b','c',20]
scalar = 5
dict = {'a':10, 'b':20, 'c':30, 'd':40}
random_numbers = np.random.randint(10,100,6)

# pandas_series = pd.Series(numbers)
# pandas_series = pd.Series(5, [0,1,2,3])
# pandas_series = pd.Series(numbers, ['a','b','c','d']) #2. kısım index numaralarını istedigimiz gibii değiştirmemizi sağlar
# pandas_series = pd.Series(dict)
# pandas_series = pd.Series(random_numbers)


pandas_series = pd.Series([20,30,40,50], ['a','b','c','d'])
result = pandas_series[0]
result2 = pandas_series[-1] #En sağdan başlar yani sonuncu elemanı verir
result3 = pandas_series[:2] #ilk 2 eleman
result4 = pandas_series[-2:] #Son 2 eleman
result5 = pandas_series['a']
result6 = pandas_series[['a','c']]
result7 = pandas_series.ndim #kac boyutlu oldugu bilgisini verir
result8 = pandas_series.dtype
result9 = pandas_series.shape
result10 = pandas_series.sum()
result11 = np.sqrt(pandas_series)
result12 = pandas_series >= 50
result13 = pandas_series % 2 == 0

print(pandas_series)
print(pandas_series[pandas_series % 3 == 0])
print(result13)

opel2018 = pd.Series([20,30,40,10],["astra","corsa","mokka","insignia"])
opel2019 = pd.Series([40,80,20,10],["astra","corsa","Grandland","insignia"])

total = opel2018 + opel2019
print(total["corsa"])