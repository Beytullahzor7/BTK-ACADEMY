def not_hesapla(satır):
    satır = satır[:-1]
    liste = satır.split(':')
    
    ogrenciAdı = liste[0]
    Notlar = liste[1].split(',')

    not1 = int(Notlar[0])
    not2 = int(Notlar[1])
    not3 = int(Notlar[2])
    
    ortalama = (not1+not2+not3) / 3

    if ortalama >= 85 and ortalama <= 100:
        harf = "AA"

    elif ortalama >= 75 and ortalama <= 84:
        harf = "BA"

    elif ortalama >= 65 and ortalama <= 74:
        harf = "BB"

    elif ortalama >= 55 and ortalama <= 64:
        harf = "CB"
    
    elif ortalama >= 45 and ortalama <= 54:
        harf = "CC"
    
    else:
        harf = "FF"

    return ogrenciAdı + ": " + harf + "\n"
    

def ortalamaları_oku():
    with open('sinav_notları.txt','r',encoding='utf-8') as file:
        for satır in file:
            print(not_hesapla(satır))


def not_gir():
    ad = input('Öğrenci Adı : ')
    soyad = input('Öğrenci Soyadı : ')
    not1 = input('Not1 : ')
    not2 = input('Not2 : ')
    not3 = input('Not3 : ')

    with open('sinav_notları.txt',"a",encoding='utf-8') as file:
        file.write(ad+' '+soyad+ ':'+not1+','+not2+','+not3+'\n')


def notları_kayıtet():
    with open('sinav_notları.txt',"r",encoding='utf-8') as file:
        liste = []

        for i in file:
            liste.append(not_hesapla(i))
        
        with open("sonuclar.txt","w",encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)


while True:
    islem = input('1- Notları Oku\n2- Not Gir\n3- Notları Kayıt Et\n4- Çıkış\n')

    if islem == '1':
        ortalamaları_oku()

    elif islem =='2':
        not_gir()
        
    elif islem =='3':
        notları_kayıtet()

    else:
        print('Uygulamadan Çıkış Yapıldı')
        break