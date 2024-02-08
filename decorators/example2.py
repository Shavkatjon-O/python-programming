""" Python Decorators """

import time


def timed(function):
    def wrapper(*args, **kwargs):
        # function execution
        start_time = time.time()
        function(*args, **kwargs)
        end_time = time.time()

        execution_time = end_time - start_time

        print(f"Execution time of {function.__name__}: {execution_time} seconds")

    return wrapper


@timed
def iterate():
    x = 0
    for i in range(10000000):
        x += i**2
    print(x)


if __name__ == "__main__":
    iterate()

    # Output
    # 333333283333335000000
    # Execution time of iterate: 0.7291839122772217 seconds
