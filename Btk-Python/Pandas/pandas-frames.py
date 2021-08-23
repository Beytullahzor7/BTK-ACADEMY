import pandas as pd
from pandas.core.frame import DataFrame

data = [["Ahmet", 50],["Ali", 60], ["Yağmur", 70], ["Çınar", 85]]
dict = {"Name": ["Ahmet","Ali","Yağmur","Çınar"], "Grade": [50,60,70,85]}

df = pd.DataFrame(dict, index=[211,222,233,234])
print(df)

# df = DataFrame(data, columns= ["Name", "Grade"], index=[1,2,3,4], dtype=float)
# print(df)

# s1 = pd.Series([3,2,1,0])
# s2 = pd.Series([0,3,7,2])

# data = dict(apples = s1, orange = s2)

# df = pd.DataFrame(data)

# print(df)