import matplotlib.pyplot as plt
import numpy as np

#Example 1

# x = [1,2,3,4]
# y = [1,4,9,16]


# plt.plot(x,y,"o--y")
# plt.axis([0,6,0,20]) #X 0-6 arası, Y 0-20 arası olsun demektir

# plt.title("Grafik Baslıgı")
# plt.xlabel("X grafigi")
# plt.ylabel("Y grafigi")
# plt.show()

#Example 2

x = np.linspace(0,2,100) #0-2 arasında ve 100 eşit parçaya bölünmüş

plt.plot(x, x, label = "linear", color = "red")
plt.plot(x, x**2, label = "quadric", color = "yellow")
plt.plot(x, x**3, label = "cubic", color = "green")

plt.xlabel("X Label")
plt.ylabel("Y Label")

plt.title("Simple Plot")
plt.legend() #grafigin içerisinde labelları ve renklerini gösterir

plt.show()

#Example 3

x = [1,2,3,4]
y = [1,4,9,16]


#fmt = '[marker][line][color]' = "o:r" =  o markerdir, -- stili ifade eder, r rengi ifade eder bir alttaki örnek için
plt.plot(x,y,"o:r", linewidth = 3)
plt.axis([0,6,0,20]) #x ve ye nin hangi aralıkta oluştugudur. X 0-6 arası Y 0-20 arasıdır

plt.title("Kare Almak")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()