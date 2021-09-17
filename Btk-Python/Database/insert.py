from typing import Text
import mysql.connector

def insertProduct(name, price, imageUrl, description):
    
    connection = mysql.connector.connect(host = "localhost", user = "root", password = "1234", database = "note-app")
    cursor = connection.cursor()

    sql = "INSERT INTO products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)" #kayıt eklemek için sql cümleciği oluşturduk
    #values = ("Samsung S5", 1000, "3.jpg", "güzel telefon" ) #bilgileri hazır vermek istedimizde bu satırı yorum satırından çıkarırız
    values = (name, price, imageUrl, description) #bilgileri kullanıcıdan almak için bu satırı aktif ederiz

    cursor.execute(sql,values)

    try: #commit databaseye gönderildiğinde hata ihtimaline karşın try-except hata bloğu kullandık
        connection.commit() #hazırlanan sorguyu databaseye commit ile göndeririz
        print(f'{cursor.rowcount} tane kayıt eklendi')
        print(f'son eklenen kaydın id: {cursor.lastrowid}')

    except mysql.connector.Error as err:
        print("Hata:" , err)

    finally:
        connection.close()
        print("Database bağlantısı kapandı")



def insertProducts(list):
    
    connection = mysql.connector.connect(host = "localhost", user = "root", password = "1234", database = "note-app")
    cursor = connection.cursor()

    sql = "INSERT INTO products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    #values = ("Samsung S5", 1000, "3.jpg", "güzel telefon" ) #bilgileri hazır vermek
    values = list #bilgileri kullanıcıdan almak

    cursor.executemany(sql,values) #çoğul kayıt işlemi yaptığımızı belirttik

    try:
        connection.commit() #hazırlanan sorguyu databaseye commit ile göndeririz
        print(f'{cursor.rowcount} tane kayıt eklendi')
        print(f'son eklenen kaydın id: {cursor.lastrowid}')

    except mysql.connector.Error as err:
        print("Hata:" , err)

    finally:
        connection.close()
        print("Database bağlantısı kapandı")


list = []
while True: #birden fazla ürün eklemek için while true döngüsü oluşturduk
    name = input("Ürün adı: ")
    price = float(input("Ürün fiyatı: "))
    imageUrl = input("Ürün Resim Adı: ")
    description = input("Ürün Açıklaması: ")

    list.append((name, price, imageUrl, description)) #kullanıcının girdiği her kaydı append ile bir tuple listesi şeklinde ekleyeceğiz

    result = input("Devam etmek istiyor musunuz? (e/h)")

    if result == 'h':
        print("Kayıtlarınız Veritabanına Aktarılıyor")
        print(list)
        insertProducts(list)
        break
    

#insertProduct(name, price, imageUrl, description)     