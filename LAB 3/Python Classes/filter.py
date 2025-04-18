def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [10, 15, 3, 7, 19, 21, 23]
primes = list(filter(lambda x: is_prime(x), numbers))
print(primes)  # Выведет [3, 7, 19, 23]
