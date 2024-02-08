""" Python Decorators """


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


# Decorator
def add_area_method(cls):
    def calculate_area(self):
        return self.width * self.height

    cls.calculate_area = calculate_area
    return cls


@add_area_method
class RectangleWithArea(Rectangle):
    pass


if __name__ == "__main__":
    rectangle = RectangleWithArea(4, 5)

    area = rectangle.calculate_area()  # type: ignore

    print(f"Area: {area}")

    # Output
    # Area: 20
