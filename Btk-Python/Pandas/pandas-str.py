import pandas as pd
import numpy as np

data = pd.read_csv("Pandas/nba.csv")

data.dropna(inplace = True) #Nan alanlar kayıtlar içerisinden silinir


# data["Name"] = data["Name"].str.upper()
# data["Name"] = data["Name"].str.lower()

# data["index"] = data["Name"].str.find("a") #index adında bir kolon oluşturup name kolonu içerisindeki 'a' karakterinin kacıncı eleman oldugunu belirtir
# data = data.Name.str.contains("Jordan") #jordanı buldugu kayıtı true olarak döner
# data = data[data.Name.str.contains('Jordan')] #Dataframe içerisinde name kolonunda jordan isminin geçtiği kayıtları döner
# data = data.Team.str.replace(' ', '-') #team kolonu içerisindeki (.) ları (-) ile yer değiştiririz
data[["FirstName","LastName"]] = data["Name"].loc[data["Name"].str.split().str.len() == 2].str.split(expand=True)
#name kolonunu ad ve soyad olarak 2 ayrı kolon seklinde ifade etmek istedik bunun için de boşluğa göre parçalama işleminde
#uzunlugun 2 ye eşit olup olmadığı kontrolünü yaptık ve koşul sağlandıgında expand diyerek genişlettik

print(data.head(10))