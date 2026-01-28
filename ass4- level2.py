class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False


# Creating objects
p1 = Point(2, 3)
p2 = Point(2, 3)
p3 = Point(4, 5)

# Comparing points
print(p1 == p2)   # True
print(p1 == p3)   # False
