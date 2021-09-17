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
        

name = input("Ürün Adı : ")
price = float(input("Ürün Fiyatı: "))
imageUrl = input("Ürün Resmi : ")
description = input("Ürün Açıklaması: ")

insertProduct(name, price, imageUrl, description)