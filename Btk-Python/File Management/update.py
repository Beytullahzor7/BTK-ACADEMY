# with open("newfile.txt","r+",encoding="utf-8") as file:
#     file.seek(40)
#     file.write("python")

# with open("newfile.txt","r+",encoding="utf-8") as file:

# ***********SAYFA SONUNA GÜNCELLEME ************

# with open("newfile.txt","a",encoding="utf-8") as file:
#     file.write("\nbeytullah zor")

# ***********SAYFA BASINDA GÜNCELLEME ************

# with open("newfile.txt","r+",encoding="utf-8") as file:
#     content = file.read()
#     content = "baslık\n" + content
#     file.seek(0)
#     file.write(content)
#     print(content)

# ***********SAYFA ORTASINDA GÜNCELLEME ************

with open("newfile.txt","r+",encoding="utf-8") as file:
    list = file.readlines()
    list.insert(1,"Ali2\n")
    file.seek(0) #eklenmek istenen indeksin konum bilgisi
    file.writelines(list)

with open("newfile.txt","r+",encoding="utf-8") as file:
    print(file.read())
