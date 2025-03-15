def square(a, b):
    for i in range(a, b + 1):
        i = i ** 2
        yield i 

a = int(input("Enter a: "))
b = int(input("Enter b: "))

squares = square(a, b)
print(*squares, sep = ", ")

#25, 36, 49, 64