import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data, columns=["Columns1","Columns2","Columns3","Columns4","Columns5"])

result = df
result = df.columns #dataframe içerisinde bulunan columnları ekrana verir
result = df.head() #ilk 5 satırı verir
result = df.head(10) #ilk 10 satırı verir 
result = df.tail() #son 5 satırı verir
result = df["Columns1"].head() #column1 sütununda yer alan ilk 5 satırı verir
result = df.Columns1.head() #column1 sütununda yer alan ilk 5 satırı verir
result = df[["Columns1","Columns2"]].head()
result = df[["Columns1","Columns2"]].tail()
result = df[5:15][["Columns1","Columns2"]].head() #aralıgı 5-15. satırlar olarak belirleyip bu aralık içinden ilk 5 satırı aldık
result = df[5:15][["Columns1","Columns2"]].tail() #aralıgı 5-15. satırlar olarak belirleyip bu aralık içinden son 5 satırı aldık

result = df > 50 #dataframe içerisinde >50 olan değerleri true olarak <50 leri ise false olarak dönüt verir
result = df[df > 50] #true veya false yerine değerlerin kendisini verir
result = df[df % 2 == 0]
result = df["Columns1"] > 50 #Sadece columns1 deki değerlere bakar ve 50 den büyük olanları bize getirir
result = df[df["Columns1"] > 50][["Columns1","Columns2"]]
result = df[(df["Columns1"] > 50) & (df["Columns1"] <= 70)]
result = df[(df["Columns1"] > 50) | (df["Columns1"] <= 70)][["Columns1","Columns2"]]
result = df.query("Columns1 >= 50 & Columns2 % 2 == 0 ")
result = df.query("Columns1 >= 50 & Columns2 % 2 == 0 ")[["Columns1","Columns2"]] #gelen kayıtlar içerisinden kolon filtrelemesi
result = df.query("Columns1 >= 50 | Columns2 % 2 == 0 ")[["Columns1","Columns2"]]


print(result)