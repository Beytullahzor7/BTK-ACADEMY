#class

class Person:
    #class attributes
    address = 'no information'
    #constructor
    def __init__(self ,name, year):

        #attribute
        self.name = name
        self.year = year
  
    #instance methods
    def intro(self):
        print('Hello There. I am '+ self.name)   

    #instance methods
    def calculateAge(self):
        return 2021 - self.year

#object(instance)
p1 = Person(name = 'ali', year = 1998)
p2 = Person(name = 'fatma', year = 1990)
p1.intro()
p2.intro()

#accessing object attributes
print(f'adım : {p1.name} ve yaşım : {p1.calculateAge()}')
print(f'adım : {p2.name} ve yaşım : {p2.calculateAge()}')