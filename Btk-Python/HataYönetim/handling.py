try:
    x = int(input('x : '))
    y = int(input('y : '))

    print(x/y)

except ZeroDivisionError:
    print('Y için 0 girilemez')
except ValueError:
    print('X ve Y için sayısal değer girmelisiniz ')
