movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

# 1. Проверяет, превышает ли рейтинг IMDB 5.5
def is_highly_rated(movie):
    print("\n")
    return movie["imdb"] > 5.5

# 2. Возвращает список фильмов с рейтингом выше 5.5
def get_high_rated_movies(movies):
    print("\n")
    return [movie for movie in movies if movie["imdb"] > 5.5]

# 3. Возвращает список фильмов в указанной категории
def get_movies_by_category(movies, category):
    print("\n")
    return [movie for movie in movies if movie["category"].lower() == category.lower()]

# 4. Вычисляет средний рейтинг списка фильмов
def get_average_imdb(movies):
    print("\n")
    if not movies:
        return 0
    return sum(movie["imdb"] for movie in movies) / len(movies)

# 5. Вычисляет средний рейтинг фильмов в указанной категории
def get_average_imdb_by_category(movies, category):
    print("\n")
    category_movies = get_movies_by_category(movies, category)
    return get_average_imdb(category_movies)

# Примеры вызова функций
print(is_highly_rated(movies[0]))  # True
print(get_high_rated_movies(movies))  # Список фильмов с IMDB > 5.5
print(get_movies_by_category(movies, "Romance"))  # Список фильмов в категории "Romance"
print(get_average_imdb(movies))  # Средний рейтинг всех фильмов
print(get_average_imdb_by_category(movies, "Romance"))  # Средний рейтинг фильмов в категории "Romance"
