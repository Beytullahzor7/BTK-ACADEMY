#gönderilen bir kelimeyi belirtilen kez ekranda gösteren bir fonk yaz

def yazdir(kelime,adet):
    print(kelime*adet)

yazdir("merhaba\t", 10)

#kendine gönderilen sınırsız sayıdaki parametreyi bir listeye ceviren fonk yaz

def cevirliste(*params):
    liste = []

    for i in params:
        liste.append(i)
    return liste

result = cevirliste(10,12,14,32,23,"merhaba")
print(result)

#Gönderilen 2 sayı arasındaki tüm asal sayıları bulun

"""def asalBul(sayi1,sayi2):
    for sayi in range(sayi1, sayi2+1):
        if sayi > 1:
            for i in range(2, sayi):
                if sayi % i == 0:
                    break
            else:
                print(sayi)

sayi1 = int(input('sayi1: '))
sayi2 = int(input('sayi2: '))

asalBul(sayi1, sayi2)"""


#kendisine gönderilen bir sayının tam bölenlerini liste seklinde döndüren bir fonk yaz

def tambolen(x):
    bolenler = []
    for i in range(2,x):
        if x % i == 0:
            bolenler.append(i)
    return bolenler
print(tambolen(10))
