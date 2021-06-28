class Person:
    def __init__(self, name, year):
        if len(name) > 10:
            raise Exception("Name alanı fazla karakter içeriyor")
        else:
            self.name = name
        
p = Person("Aliiiiiiiiiiiiii",1998)