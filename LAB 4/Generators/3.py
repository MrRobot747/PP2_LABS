def divisible(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
div = divisible(n)
print(*div, sep = ", ")

#0, 12, 24, 36, 48