""" Python Decorators """


# function implementation of decorator
def function_logged(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)

        # stores result of the function in txt file
        with open("f_logs.txt", "a") as file:
            file.write(f"This function returned: {result}\n")

    return wrapper


@function_logged
def f_add(a, b):
    return a + b


# class implementation of decorator
class ClassLogged:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        result = self.function(*args, **kwargs)

        # stores result of the function in txt file
        with open("c_logs.txt", "a") as file:
            file.write(f"This function returned: {result}\n")


@ClassLogged
def c_add(a, b):
    return a + b


if __name__ == "__main__":
    f_add(1, 2)
    f_add(3, 5)

    c_add(2, 3)
    c_add(5, 6)
