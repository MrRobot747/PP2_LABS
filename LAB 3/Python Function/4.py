def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [n for n in numbers if is_prime(n)]

# Ввод данных
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Фильтрация простых чисел
prime_numbers = filter_prime(numbers)

# Вывод результата
print("Prime numbers:", " ".join(map(str, prime_numbers)) if prime_numbers else "No prime numbers found.")


