def cube():
    for i in range(6):
        yield i ** 3 #yield ile değer bellekte saklanmaz 


generator = cube()
iterator = iter(generator)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break


# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


