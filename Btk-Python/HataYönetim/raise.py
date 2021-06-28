
def check_password(psw):
    import re
    if len(psw) < 8:
        raise Exception("Parola en az 7 karakter olmalıdır.")
    elif not re.search("[a-z]", psw):
        raise Exception("Parola küçük harf içermelidir.")
    elif not re.search("[A-Z]", psw):
        raise Exception("Parola büyük harf içermelidir.")
    elif not re.search("[0-9]", psw):
        raise Exception("Parola rakam harf içermelidir.")
    elif re.search("\s", psw):
        raise Exception("Parola boşluk içermemelidir.")
    else:
        print("Geçerli Parola")

password = "AVsad5668"

try:
    check_password(password)
except Exception as ex:
    print(ex)
else:
    print("Geçerli Parola")
finally:
    print("Validation Tamamlandı")