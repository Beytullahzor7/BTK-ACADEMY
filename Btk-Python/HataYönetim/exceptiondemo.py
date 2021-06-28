"""liste = ["1","2","5a","10b","abc"]

#1 Liste elemanları içindeki sayısal değerleri bulun

for i in liste:
    try:  
        result = int(i)
        print(result)
    except ValueError:
        continue
    
#2 Kullanıcı 'q' değerine girmedikce aldıgınız her inputun sayı olup olmadıgını kontrol et 

while True:
    sayi = input("Sayı : ")
    if sayi == 'q':
        print("Program Sonlandırıldı!")
        break

    try:
        result = float(sayi)
        print('Girdiğiniz sayı ',result)
    except ValueError:
        print('Gecersiz Sayı')
        continue

#3 Girilen parola içinde türkçe karakter hatası veriniz



def checkPassword(parola):
    turkce_karakterler = 'şçğüöİ'
    
    for i in parola:
        if i in turkce_karakterler:
            raise TypeError('Parola türkçe karakter içeremez')
        else:
            pass

    print('Geçerli Parola')

parola = input('Parola : ')

try:
    checkPassword(parola)
except TypeError as err:
    print(err)"""

#4 Faktoriyel fonk olusturup fonksiyona gelen değer için hata mesajları üret

def faktoriyel(x):
    x = int(x)
    
    if x < 0:
        raise ValueError('Negatif Değer')

    result = 1
    for i in range(1, x+1):
        result*=i

    return result

for x in [3, 4, 5, -3, '10a']:
    try:
        y = faktoriyel(x)
    except ValueError as error:
        print(error)
        continue
    print(y)