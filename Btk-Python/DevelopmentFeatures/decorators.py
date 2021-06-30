# def my_decorator(func):
#     def wrapper(name):
#         print("fonksiyondan önceki islemler")
#         func(name)
#         print("fonksiyondan sonraki islemler")
#     return wrapper

# @my_decorator
# def sayHello(name):
#     print("Hello", name)

# sayHello("Ali")

import math
import time

def calculate_time(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish = time.time()
        print("Fonksiyon "+ func.__name__ + ' ' +str(finish-start) + " saniye sürdü" )

    return wrapper

@calculate_time
def usalma(a,b):
    print(math.pow(a,b))

@calculate_time   
def faktoriyel(number):
    print(math.factorial(number))
    
usalma(3,2)
faktoriyel(6)