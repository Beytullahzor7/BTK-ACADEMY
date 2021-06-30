with open("newfile.txt","r",encoding="utf-8") as file:
    content = file.read()
    print(content)

    file.seek(10)
    print(file.tell())
