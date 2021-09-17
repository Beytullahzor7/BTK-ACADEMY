import re
import mysql.connector
from mysql.connector.fabric import connect

def insertProduct(name, price, imageUrl, description):
    connection = mysql.connector.connect(host="localhost", user = "root", password="mysql1234", database="node_app")
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)" 
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
    connection = mysql.connector.connect(host="localhost", user = "root", password="mysql1234", database="node_app")
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)" 
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

    cursor.execute("Select * From Products Where name LIKE 'Samsung%' and price=3000")

    result = cursor.fetchall() ##koşula uyan bütün kayıtları getir   
    # result = cursor.fetchone() #koşula uyan ilk kaydı getir 

    for product in result:
        print(f'id: {product[0]} name: {product[1]} price: {product[2]}')
     

def getProductById(id):
    connection = mysql.connector.connect(host="localhost", user = "root", password="1234", database="note-app")
    cursor = connection.cursor()

    sql = "Select * From Products Where id=%s" # %s diyerek placeholder oluşturduk
    params = (id,) #gönderdiğimiz id bilgisi yukarıdaki %s yerine geçecek

    cursor.execute(sql,params)

    result = cursor.fetchone()    

    print(f'id: {result[0]} name: {result[1]} price: {result[2]}')

def getProductByPrice(price):
    connection = mysql.connector.connect(host="localhost", user = "root", password = "1234", database = "note-app")
    cursor = connection.cursor()

    sql = "Select * From Products Where price=%s"
    params = (price,)

    cursor.execute(sql, params)

    result = cursor.fetchone()

    print(f' price: {result[2]} name: {result[1]}')

