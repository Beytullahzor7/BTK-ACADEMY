import mysql.connector

mydb = mysql.connector.connect( #server baglantısı

    host = "localhost",
    user = "root",
    password = "1234",
    database = "mydatabase" #servera baglandıktan sonra hangi database ile işlem yapacağımızı belirttik
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))") #sql scripti çalıştırma

# # mycursor.execute("CREATE DATABASE mydatabase") # boş bir database oluşturmak

# mycursor.execute("SHOW DATABASES") #ilgili servera bağlanıp bütün databaseleri ekrana verecek
# for i in mycursor:
#     print(i)