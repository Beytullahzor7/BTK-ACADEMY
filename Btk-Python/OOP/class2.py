class Circle:
    #Class Object attribute
    pi = 3.14

    def __init__(self, yaricap = 1): #belirtirlemedi takdirde default olarak yarıcap=1

        self.yaricap = yaricap
        
    #Methods
    def cevreHesapla(self): #class içersindeki bilgilere ulaşmak için self parametresi verdik
        return 2*self.pi*self.yaricap
    
    def alanHesapla(self):
        return self.pi*(self.yaricap**2)

c1 = Circle(5)

print(f"c1 : cevre = {c1.cevreHesapla()} alan = {c1.alanHesapla()}")