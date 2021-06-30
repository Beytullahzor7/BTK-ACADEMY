def toplama(a,b):
    return a+b
def cıkarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b

def islem(f1,f2,f3,f4,islem_adı):
    if islem_adı == "toplama":
        print(f1(3,4))
    elif islem_adı == "cıkarma":
        print(f2(6,2))
    elif islem_adı == "carpma":
        print(f3(8,4))
    elif islem_adı == "bolme":
        print(f4(16,4))
    else:
        print("Geçersiz İşlem")

islem(toplama, cıkarma, carpma, bolme, "carpma")