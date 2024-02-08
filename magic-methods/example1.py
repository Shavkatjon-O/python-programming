""" Magic Methods or Double Underscore Methods (Dunder Methods) """


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


if __name__ == "__main__":
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)

    print("v1:", v1)
    print("v2:", v2)
    print("v1 + v2:", v1 + v2)
    print("v1 - v2:", v1 - v2)
    print("v1 * v2:", v1 * v2)
    print("v1 == v2:", v1 == v2)

    # Output:
    # v1: (1, 2)
    # v2: (3, 4)
    # v1 + v2: (4, 6)
    # v1 - v2: (-2, -2)
    # v1 * v2: (3, 8)
    # v1 == v2: False
