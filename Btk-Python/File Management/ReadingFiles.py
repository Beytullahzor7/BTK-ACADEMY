# try:

#     file = open("newfile.txt","r")
#     print(file)
# except FileNotFoundError:
#    print("Dosya okuma hatası")
# finally:
#     print("dosya kapandı")
#     file.close() 

file = open("newfile.txt","r",encoding="utf-8")

# for i in file:
#     print(i, end="")

content = file.read()
print(content)
file.close  