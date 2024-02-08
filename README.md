## Contents

- [Python Decorators](#python-decorators)
- [Magic Methods](#magic-methods)

## Python Decorators

Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of a function or class. Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it. But before diving deep into decorators let us understand some concepts that will come in handy in learning the decorators.

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function is called")
        result = func(*args, **kwargs)
        print("After the function is called")
        return result
    return wrapper

@my_decorator
def my_function(x, y):
    return x + y

# Calling the decorated function
print(my_function(3, 5))
```

1. Syntax: Decorators use the @decorator_name syntax to modify functions or methods. This is a syntactic sugar for wrapping the decorated function with another function.

2. Functions as First-Class Objects: In Python, functions are first-class objects, which means they can be passed around and used as arguments just like any other object.

3. Higher-Order Functions: A decorator is essentially a higher-order function that takes a function as an argument and returns another function.

4. Inner Functions: Decorators usually involve defining an inner function (often named wrapper) inside the decorator function. This inner function performs the additional functionality before or after calling the original function.

5. Returning Functions: Decorators typically return the inner function (wrapper function) which replaces the original function or method.

6. Multiple Decorators: You can apply multiple decorators to a single function or method by stacking them on top of each other using the @ syntax.

7. Common Use Cases: Decorators are commonly used for:
- **Logging:** Adding logging statements before and/or after function calls.
- **Memoization:** Caching function results for improved performance.
- **Authentication and Authorization:** Enforcing access control rules.
- **Timing:** Measuring the execution time of functions.
- **Validation:** Checking the validity of function arguments.
- **Error Handling:** Wrapping functions with try-except blocks for error handling.
- **Method Wrapping:** Modifying the behavior of methods in classes.

8. Preserving Metadata: When using decorators, metadata such as function name, docstring, and signature may be lost. To preserve this metadata, you can use functools.wraps decorator from the functools module.

9. Decorating Classes: Decorators can also be applied to classes and class methods, although the syntax may vary slightly.

10. Debugging Decorators: Debugging code that uses decorators can sometimes be tricky, especially when multiple decorators are involved. Understanding the order of execution of decorators and how they interact with each other is crucial for effective debugging.

11. Decorators and Generators: Decorators can also be applied to generator functions, allowing you to modify the behavior of generators as well.

12. Decorators in Libraries and Frameworks: Many Python libraries and frameworks extensively use decorators to provide extensibility and customization options. Examples include Flask, Django, and SQLAlchemy.

13. Custom Decorators: You can create your own decorators to encapsulate reusable functionality and apply it across your codebase.

Source: https://www.geeksforgeeks.org/decorators-in-python/

## Magic Methods

## Tutorials

### Youtube
- https://www.youtube.com/watch?v=KSiRzuSx120&list=PL7yh-TELLS1FuqLSjl5bgiQIEH25VEmIc&index=2
- https://www.youtube.com/watch?v=mclfteWlT2Q&list=PLzMcBGfZo4-kwmIcMDdXSuy_wSqtU-xDP&index=1

### w3schools
- https://www.w3schools.com/python/