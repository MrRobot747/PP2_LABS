def even(n):
    for i in range (0, n + 1):
        if i % 2 == 0:
            yield i

n = int(input())
print(*even(n), sep = ", ")

#0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54