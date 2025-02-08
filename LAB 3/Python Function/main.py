# main.py

from my_functions import has_33, spy_game, sphere_volume, is_palindrome, guess_number

# Проверка has_33
print(has_33([1, 3, 3]))  # True
print(has_33([1, 3, 1, 3]))  # False

# Проверка spy_game
print(spy_game([1,2,4,0,0,7,5]))  # True
print(spy_game([1,0,2,4,0,5,7]))  # True

# Вычисление объёма сферы
print(sphere_volume(3))  # 113.097

# Проверка на палиндром
print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False

# Запуск игры "Угадай число"
# guess_number()  # Раскомментировать для игры
