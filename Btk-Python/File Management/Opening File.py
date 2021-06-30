#Dosya acmak için open() fonk kullanılır
#kullanımı = open(dosya_adi,dosya_erişme_modu)
#w = write = dosyayı konumda olusturur
#a = append = dosya konumda yoksa olusturur
#x = create = dosya zaten varsa hata verir
#r = read = okuma

file = open("newfile.txt","a",encoding='utf-8')
file.write("\ndeneme dosyası6")
file.close