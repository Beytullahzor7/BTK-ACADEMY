import re
from types import resolve_bases
import mysql.connector
from datetime import datetime

from mysql.connector import cursor
from connection import connection


class Student:
    connection = connection
    mycursor = connection.cursor()

    def __init__(self,studentNumber,name,surname,birthdate,gender):
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    def saveStudent(self): #instanceMethod
        sql = "INSERT INTO student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES(%s,%s,%s,%s,%s)"
        value = (self.studentNumber,self.name,self.surname,self.birthdate,self.gender)
        Student.mycursor.execute(sql,value)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt eklendi. ')

        except mysql.connector.Error as err:
            print('Hata', err)

        finally:
            Student.connection.close()

    @staticmethod #artık instance method olmadıgı static method oldugu için self parametresi vermeyecegiz
    def saveStudents(students):
        sql = "INSERT INTO student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES(%s,%s,%s,%s,%s)"
        values = students
        Student.mycursor.executemany(sql,values)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt eklendi. ')

        except mysql.connector.Error as err:
            print('Hata', err)

        finally:
            Student.connection.close()


# ahmet = Student("202","ahmet","yılmaz",datetime(2000, 3, 17),"E")
# ahmet.saveStudent()
                            #datetime(year,month,day)               
# ogrenciler = [
#     ("401","Ahmet","Yılmaz",datetime(2005, 5, 17),"E"),
#     ("402","Ali","Can",datetime(2005, 6, 17),"E"),
#     ("403","Canan","Tan",datetime(2005, 7, 7),"K"),
#     ("404","Ayşe","Taner",datetime(2005, 9, 23),"K"),
#     ("405","Bahadır","Toksöz",datetime(2004, 7, 27),"E"),
#     ("406","Ali","Cenk",datetime(2003, 8, 25),"E")
# ]
    
    @staticmethod
    def studentInfo():

        #sql = "select * from student"
        sql = "select * from student LIMIT 5"
        #sql = "select StudentNumber,Name,Surname from student"
        # sql = "select Name,Surname from student Where gender = 'K'"
        #sql = "select Name,Surname from student Where YEAR(birthdate) = 2000"
        #sql = "select * from student where name like '%an%' or surname like '%an%'" #ad yada soyad içerisinde "an" bulunan
        #sql = "select COUNT(*) from student where gender = 'E'"
        #sql = "select COUNT(id) from student where gender = 'E'"
        #sql = "select name,surname from student where gender = 'K' Order By name,surname"

        Student.mycursor.execute(sql)

        try:
            result = Student.mycursor.fetchall()
            for i in result:
                print(i)
        
        except mysql.connector.Error as err:
            print("Hata", err)
        
        finally:
            Student.connection.close()


Student.studentInfo()