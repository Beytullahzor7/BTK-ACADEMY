from kütüphane import * #kütüphane.py dosyasında yazdıgımız 2 class ı bu dosya içerisinde aynen kullanmak için yaptık

print("""********************

Kütüphane Programına Hoşgeldiniz...

İşlemler;

1.Kitapları Göster

2.Kitap Sorgulama 

3.Kitap Ekle

4.Kitap Sil

5.Baskı Yükselt

*********************""")

kütüphane = Kütüphane()


while True:

    işlem=input("Yapacagınız İşlem:")

    if (işlem=="q"):
        print("Programdan Cıkılıyor....")
        print("Yine Bekleriz...")
        break

    elif (işlem == "1"):
        kütüphane.kitapları_goster()

    elif (işlem == "2"):
        isim = input("Hangi Kitabı İstiyorsunuz?")
        print("Kitap Sorgulanıyor...")
        time.sleep(2)

        kütüphane.kitap_sorgula(isim)

    elif (işlem == "3"):
        isim = input("İsim:")
        yazar = input("Yazar:")
        yayınevi = input("Yayınevi:")
        tür = input("Tür:")
        baskı = int(input("Baskı:"))

        yeni_kitap = Kitap(isim,yazar,yayınevi,tür,baskı)

        print("Kitap ekleniyor...")
        time.sleep(2)

        kütüphane.kitap_ekle(yeni_kitap)
        print("Kitap eklendi...")

    elif (işlem == "4"):
        isim = input("Hangi Kitabı Silmek istiyorsunuz?:")

        cevap = input("Emin misiniz ? (E/H)")

        if (cevap=="E"):
            print("Kitap Siliniyor...")
            time.sleep(2)
            kütüphane.kitap_sil(isim)
            print("Kitap Silindi")

        else:
            print("Silme işleminden vazgeçildi")

    elif (işlem == "5"):
        isim = input("Hangi kitabın baskısını yükseltmek istiyorsunuz?:")
        print("Baskı yükseltiliyor...")
        time.sleep(2)
        kütüphane.baskı_yükselt(isim)
        print("Baskı yükseltildi...")

    

    else:
        print("Gecersiz İşlem")

