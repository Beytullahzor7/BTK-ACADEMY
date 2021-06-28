AhmetHesap = {

    'ad' : 'Ahmet',
    'hesapNo' : '12345',
    'bakiye' : 3000,
    'ekHesap' : 2000
}

BerkcanHesap = {

    'ad' : 'Berkcan',
    'hesapNo' : '56789',
    'bakiye' : 3000,
    'ekHesap' : 2000
}


def paraYatır(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")
    bakiyeSorgula(hesap)

    yer = input("Para ana hesaba yatırılsın mı (e/h) : ")
    
    if yer == 'e':
        print(f"{hesap['hesapNo']} nolu hesabınıza {miktar} TL yatırılmıştır")
        hesap['bakiye'] += miktar

    else:
        print(f"Ek hesabınıza {miktar} TL yatırılmıştır")
        hesap['bakiye'] += miktar


def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print("Paranızı Alabilirsiniz")
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if (toplam >= miktar):
            ekHesapKullanımı = input("Ek Hesap Kullanılsın mı (e/h) : ")

            if ekHesapKullanımı == 'e':
                ekHesapKullanılacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanılacakMiktar
                print('Paranızı Alabilirsiniz')
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabıbızda {hesap['bakiye']} bulunmaktadır")
        
        else:
            print('Üzgünüz bakiyeniz yetersiz')
            bakiyeSorgula(hesap)

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesabınızda ise {hesap['ekHesap']} vardır")

paraCek(BerkcanHesap,3000)
print('**********')
paraYatır(BerkcanHesap,6000)
