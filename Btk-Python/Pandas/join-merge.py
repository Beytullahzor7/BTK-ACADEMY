import pandas as pd
import numpy as np

# customers = {

#     'CustomerId': [1,2,3,4],
#     'FirstName': ["Ahmet","Elif","Veli","Merve"],
#     'LastName': ["Yılmaz","Aydın","Demir","Toprak"],
# }

# orders = {

#     'OrderId': [10,11,12,13],
#     'CustomerId': [1,2,3,7],
#     'OrderDate': ["2021-8-20","2021-8-13","2021-8-14","2021-8-15"]
# }


# df_customers = pd.DataFrame(customers, columns=['CustomerId', 'FirstName', 'LastName'])
# df_orders = pd.DataFrame(orders, columns=['OrderId', 'CustomerId', 'OrderDate']) 

# print(df_customers)
# print(df_orders)

# result = pd.merge(df_customers,df_orders,how="inner") #2 dataframe arasında birleştirme işlemi yapar
# result = pd.merge(df_customers,df_orders,how="left") #siparişi olmayan kullanıcıları da Nan olarak gösterir
# result = pd.merge(df_customers,df_orders,how="right")
# result = pd.merge(df_customers,df_orders,how="outer")

customersA = {
    'CustomerId': [1,2,3,4],
    'FirstName': ["Ahmet","Elif","Veli","Merve"],
    'LastName': ["Yılmaz","Aydın","Demir","Toprak"],
}

customersB = {
    'CustomerId': [1,2,3,4],
    'FirstName': ["Yagmur","Cengiz","Can","Çınar"],
    'LastName': ["Doğa","Yılmaz","Bal","Turan"],
}


df_customersA = pd.DataFrame(customersA, columns=['CustomerId', 'FirstName', 'LastName'])
df_customersB = pd.DataFrame(customersB, columns=['CustomerId', 'FirstName', 'LastName'])

result = pd.concat([df_customersA,df_customersB]) #Dataframeler arası toplama işlemi yapar
result = pd.concat([df_customersA,df_customersB],axis=1) #Axis=1 iken kolonlar yanyana getirilir


print(result)