import os

result = dir(os)
result = os.name
result = os.getcwd()

print(result)

# #dizin değiştirme
# os.chdir('C:\\')
# os.chdir('../..')


# klasör oluşturma

# os.mkdir("newdirectory") yeni klasör oluşturabilir
# os.makedirs("newdirectoy/yeniklasör") içiçe yeni klasörler olusturabilir

#listeleme

# result = os.listdir() genel listeleme
# result = os.listdir('C') belli bir klasör altında listeleme
# for dosya in os.listdir():
#     if dosya.endswith('.py') filtremele yöntemi
#     print(dosya)


#os.system("notepad.exe") dosya calıstırma

#path belirtme
# result = os.path.abspath("OsModule.py")
# print(result)
