import pandas as pd
from numpy.random import rand

df = pd.DataFrame(rand(3,3), index=["A","B","C"], columns=["Column1","Column2","Column3"])

result = df
result = df["Column1"]
result = type(df["Column1"])
result = df[["Column1","Column2"]]
result = df.iloc[2]
result = df.loc["A"]
result = df.loc[:,"Column1"]
result = df.loc[:,["Column1","Column2"]]
result = df.loc[:,"Column1":"Column2"] #column1-2 arasındakileri getir
result = df.loc[:,:"Column2"] #başlangıç belirtmeden 2. sütüna kadar git
result = df.loc["A":"B",:"Column2"] #A ve B satırları ile baslangıctan itibaren 2. sütuna kadar getir
result = df.loc[:"B",:"Column2"]
result = df.loc["A","Column2"] #belirli bir değeri almak
result = df.loc[["A","B"],["Column1","Column2"]]


df["Column4"] = pd.Series(rand(3), index=["A","B","C"]) #yeni bir sütun eklemek
df["Column5"] = df["Column1"] + df["Column3"]

print(df.drop("Column5", axis=1)) #1 y ekseninden itibaren 0 ise x ekseninde itibaren silmeyi ifade eder


print(df)   


