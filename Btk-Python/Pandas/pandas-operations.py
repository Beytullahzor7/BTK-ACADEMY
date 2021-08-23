import pandas as pd
import numpy as np

data = {

    "Column1": [1,2,3,4,5],
    "Column2": [10,20,13,45,25],
    "Column3": ["abc","bca","ade","ca","dba"]

}

df = pd.DataFrame(data)

def kareal(x):
    return x  *x

kareal2 = lambda x: x * x


result = df
result = df["Column2"].unique() #tcolumn2 ye ait ekrarlamayan elemanları ekrana verir yani her eleman sadece 1 kere verilir
result = df["Column2"].nunique() #kaç adet tekil bilginin mevcut olduğunun numarasını verir
result = df["Column2"].value_counts() #hangi elemanın kac tane oldugu bilgisi
result = df["Column1"] * 2
result = df["Column1"].apply(kareal2)
result = df["Column2"].apply(lambda x: x * x) #herhangi bir referans almadan methodun kendisini apply ediyoruz
result = df["Column3"].apply(len)
df["Column4"] = df["Column3"].apply(len)
result = df.columns
result = len(df.columns)
result = df.index
result = len(df.index)
result = df.info
result = df.sort_values("Column2") #column2 içerisinde büyüklüğe göre sıralama yapar
result = df.sort_values("Column3") #column3 string yapısında olduğu için alfabeye göre sıralama yapar
result = df.sort_values("Column3", ascending= False) #ascending = increase


print(result)