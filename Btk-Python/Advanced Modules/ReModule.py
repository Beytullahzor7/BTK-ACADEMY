import re

# result = dir(re)



# # re module

# str = "Python Kursu : Python Programlama Rehberiniz | 40 saat"

# #re.findall()

# result = re.findall("Python",str)
# result = len(result)


#re.sub()
str = "Python Kursu : Python Programlama Rehberiniz | 40 saat"
result = re.sub(" ", "-",str)





print(result)