import mysql.connector

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

    # sql = "Select * From Products"
    # sql = "Select * From Categories" #kategori bilgileri gelir
    # sql = "Select * From Products inner join Categories on Categories.id=Products.Categoryid" #inner join 2 tablonun kesişen kayıtlarını verir
    # sql = "Select Products.name,Products.price,Categories.name From Products inner join Categories on Categories.id=Products.Categoryid"
    # sql = "Select Products.name,Products.price,Categories.name From Products inner join Categories on Categories.id=Products.Categoryid where Categories.name='Bilgisayar'"
    # sql = "Select Products.name,Products.price,Categories.name From Products inner join Categories on Categories.id=Products.Categoryid where products.name='samsung2'"
    sql = "Select p.name,p.price,c.name From Products as p inner join Categories as c on c.id=p.Categoryid where p.name='Samsung s8'"
    #products ve categories tablo adlarını kısaltma yaparak p ve c olarak ayarladık

    
    cursor.execute(sql)

    try:
        result = cursor.fetchall()    
        for product in result:
            print(product)

    except mysql.connector.Error as err:
        print('hata:', err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')

def getProductById(id):
    connection = mysql.connector.connect(host="localhost", user = "root", password="1234", database="note-app")
    cursor = connection.cursor()

    sql = "Select * From Products Where id=%s"
    params = (id,)

    cursor.execute(sql,params)

    result = cursor.fetchone()    

    print(f'id: {result[0]} name: {result[1]} price: {result[2]}')

def updateProduct(id, name, price):
    connection = mysql.connector.connect(host="localhost", user = "root", password="mysql1234", database="node_app")
    cursor = connection.cursor()

    sql = "Update products Set name= %s, price= %s where id= %s"
    values = (name, price, id)
    cursor.execute(sql, values)

    try:
        connection.commit()   
        print(f'{cursor.rowcount} tane kayıt güncellendi')
    except mysql.connector.Error as err:
        print('hata:', err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')

getProducts()