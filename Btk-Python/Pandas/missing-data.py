import pandas as pd
import numpy as np
from pandas.core.algorithms import value_counts

data = np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data, index=["a","c","e","f","h"], columns=["column1","column2","column3"])

df = df.reindex(["a","b","c","d","e","f","g","h"])

newColumn = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["Column4"] = newColumn

result = df

result = df.drop("column2", axis = 1)
result = df.drop(["column1","column2"], axis = 1)
result = df.drop("a", axis = 0)
result = df.drop(["a","c"], axis = 0)
result = df.isnull() #Nan olan alanlar true değer içeren alanlar false olarak verilir
result = df.notnull()
result = df.isnull().sum() #Nan olanların toplam kac deger oldugu bilgisini verir
result = df["column1"].isnull().sum()
result = df[df["column1"].isnull()]
result = df[df["column1"].isnull()]["column1"]
result = df[df["column1"].notnull()]["column1"]

result = df.dropna() #axis = 0 varsayılan değerdir, satırda Nan olan bir değer varsa o satırı getirmez
result = df.dropna(axis = 1) #axis = 1 olarak ayarladık sütuna göre Nan sorgulaması yapılır
result = df.dropna(how = 'any') #satırda herhangi bir Nan varsa ekrana gelmez
result = df.dropna(how = 'all') #tüm satır Nan ise ekrana gelmez
result = df.dropna(subset = ["column1","column2"], how = "all")  #belirtilen kolonda Nan arama yapar. Kolon1 ve Kolon2yi kapsayan satırların i
                                                                 #ikiside Nan ise ekrana vermez
result = df.dropna(subset = ["column1","column2"], how = "any") #kolon1 veya kolon2 yi kapsayan satıların herhangi birinde nan varsa o satırı vermez
result = df.dropna(thresh = 2) #en az 2 veri olan satırı silmez
result = df.dropna(thresh = 4)
result = df.fillna(value = 'No input') #Nan olan alanları doldurur

result = df.sum() #herbir kolonun ayrı ayrı toplamını verir
result = df.sum().sum() #tüm kolonların toplamını verir
result = df.size #dataframe içerisinde yer alan toplam eleman sayısını verir
result = df.isnull().sum() #kolonlardaki null olan alanlar
result = df.isnull().sum().sum() #toplam null alan sayısı



#Boş olan tüm Nan alanlarını dataframenin ortalaması ile doldurmak
def ortalama(df):
    toplam = df.sum().sum()
    adet = df.size - df.isnull().sum().sum()
    
    return (toplam / adet)

result = df.fillna(value = ortalama(df))

print(result)