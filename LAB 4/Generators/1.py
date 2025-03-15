def gen_square(N):
    for n in range(1, N + 1):
        yield n ** 2

N = int(input())
squares = gen_square(N)

for square in squares:
    print(square)

    '''1
4
9
16'''