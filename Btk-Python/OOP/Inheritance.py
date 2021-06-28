class Person():
    def __init__(self,fName,lName):

        self.fName = fName
        self.lName = lName

        print('Person Created\n')

    def who_am_i(self):
        print(f"I am a person and my name is {self.fName}")

    def eat(self):
        print("I am eating")

class Student(Person): #Kalıtım yoluyla person classının sahip oldugu tüm özelliklerin student için de geçerli olmasını sağladık
    def __init__(self,fName,lName,number):
        Person.__init__(self,fName,lName)
        self.number = number

        print('Student Created')
    
    #override
    def who_am_i(self):
        print(f"I am a student and my name is {self.fName}")

class Teacher(Person):
    def __init__(self, fName, lName, branch):
        super().__init__(fName, lName)
        self.branch = branch
            
    def who_am_i(self):
        print(f"I am a {self.branch} teacher")

p1 = Person("Ali", " Akman")
s1 = Student("Çınar"," Yılmaz ",1235)
t1 = Teacher("Serkan", " Yılmaz", " Math")

print(p1.fName + p1.lName)
print(s1.fName + s1.lName + str(s1.number))
print(t1.fName + t1.lName + t1.branch)

t1.who_am_i()
p1.who_am_i()
p1.eat()
s1.who_am_i()