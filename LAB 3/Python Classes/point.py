import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

p1 = Point(1, 2)
p2 = Point(4, 6)

p1.show()  # (1, 2)
p1.move(3, 3)
p1.show()  # (3, 3)

print(p1.dist(p2))  # Вычислит расстояние между точками
