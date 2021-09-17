import re
import mysql.connector

def insertProduct(name, price, imageUrl, description):
    connection = mysql.connector.connect(host="localhost", user = "root", password="1234", database="note-app")
    cursor = connection.cursor()

    sql = "INSERT INTO products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)" 
    values = (name,price,imageUrl,description)

    cursor.execute(sql,values)

    try:
        connection.commit()   
        print(f'{cursor.rowcount} tane kayıt eklendi')
        print(f'son eklenen kaydın id: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print('hata:', err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')

def insertProducts(list):
    connection = mysql.connector.connect(host="localhost", user = "root", password="1234", database="note-app")
    cursor = connection.cursor()

    sql = "INSERT INTO products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)" 
    values = list

    cursor.executemany(sql,values)

    try:
        connection.commit()   
        print(f'{cursor.rowcount} tane kayıt eklendi')
        print(f'son eklenen kaydın id: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print('hata:', err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')

def getProducts():
    connection = mysql.connector.connect(host="localhost", user = "root", password="1234", database="note-app")
    cursor = connection.cursor()

    # cursor.execute('Select * From Products') #products tablosundaki bütün kolonları seç demektir
    cursor.execute('Select name,price From Products') #tüm kolonları degil de sadece belirli kolonları seçmek

    # result = cursor.fetchall() #birden fazla kayıt almak istediğimizi belirtir 
    result = cursor.fetchone() #tüm kayıtlar yerine bulduğu ilk kayıdı bana getirir
    #print(result)
    
    print(f'name: {result[0]} price: {result[1]}')

    # for product in result:
    #     #print(f'name: {product[1]} price: {product[2]}') #select* from için
    #     print(f'name: {product[0]} price: {product[1]}') #select name,price için


getProducts()
