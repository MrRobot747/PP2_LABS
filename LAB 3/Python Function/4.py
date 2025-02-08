def filter_prime(numbers):
    return [n for n in numbers if n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))]


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Prime numbers:", filter_prime(numbers))
