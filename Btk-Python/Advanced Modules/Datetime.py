from datetime import datetime


simdi = datetime.today()

result1 = datetime.ctime(simdi)
result2 = datetime.strftime(simdi,'%A')
result3 = datetime.strftime(simdi,'%D')
result4 = datetime.strftime(simdi,'%Y')
result5 = datetime.strftime(simdi,'%Y %B %A')


# print(result1)
# print(result2)
# print(result3)
# print(result4)
# print(result5)


# t = '3 Temmuz 2021'
# gun, ay, yil = t.split()

# print(gun)
# print(ay)
# print(yil)

t = '15 April 2021 hour 12:50:42'
dt = datetime.strptime(t,'%d %B %Y hour %H:%M:%S')
print(dt)