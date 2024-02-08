""" Magic Methods or Double Underscore Methods (Dunder Methods) """


class Comparison:
    def __init__(self, num):
        self.num = num

    def __lt__(self, other):
        return self.num < other.num

    def __gt__(self, other):
        return self.num > other.num

    def __le__(self, other):
        return self.num <= other.num

    def __ge__(self, other):
        return self.num >= other.num

    def __eq__(self, other):
        return self.num == other.num

    def __ne__(self, other):
        return self.num != other.num


if __name__ == "__main__":
    a = Comparison(5)
    b = Comparison(3)

    print(f"{a.num} lower than {b.num}:", a < b)
    print(f"{a.num} greater than {b.num}:", a > b)
    print(f"{a.num} lower than or equal to {b.num}:", a <= b)
    print(f"{a.num} greater than or equal to {b.num}:", a >= b)
    print(f"{a.num} equal to {b.num}:", a == b)
    print(f"{a.num} not equal to {b.num}", a != b)

    # Output:
    # 5 lower than 3: False
    # 5 greater than 3: True
    # 5 lower than or equal to 3: False
    # 5 greater than or equal to 3: True
    # 5 equal to 3: False
    # 5 not equal to 3 True
