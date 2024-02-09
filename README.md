## Contents

- [Python Decorators](#python-decorators)
- [Magic Methods](#magic-methods)
- [Python Generators](#python-generators)

## Tutorials

#### NeuralNine
- https://www.youtube.com/watch?v=KSiRzuSx120&list=PL7yh-TELLS1FuqLSjl5bgiQIEH25VEmIc&index=2

#### Tech With Tim
- https://www.youtube.com/watch?v=mclfteWlT2Q&list=PLzMcBGfZo4-kwmIcMDdXSuy_wSqtU-xDP&index=1

#### FreeCodeCamp
- https://www.youtube.com/watch?v=HGOBQPFzWKo&t=3178s

#### Patrick Loeber 
- https://www.youtube.com/watch?v=HGOBQPFzWKo&t=3178s

#### ITVDN 
- https://www.youtube.com/watch?v=UohnrnZZ0w0&list=PLvItDmb0sZw-j1dHo76Yhhb5aD48DmUZu

#### w3schools
- https://www.w3schools.com/python/

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

- **Source**: https://www.geeksforgeeks.org/decorators-in-python/

## Magic Methods

Magic methods, also known as dunder methods (short for "double underscore"), are special methods in Python that have double underscores (__) at the beginning and end of their names. These methods enable you to customize the behavior of objects in various ways, such as arithmetic operations, comparisons, object creation, and string representation.

```python
class MyClass:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return MyClass(self.value + other.value)
    
    def __str__(self):
        return f"MyClass(value={self.value})"

obj1 = MyClass(5)
obj2 = MyClass(10)

result = obj1 + obj2
print("Result of addition:", result)
print("String representation:", obj1)  
```

1. `__init__(self, ...)`: Initialize an object.
2. `__repr__(self)`: Compute the "official" string representation of an object. If possible, eval(repr(obj)) should return a new object with the same value.
3. `__str__(self)`: Compute the "informal" or nicely printable string representation of an object. This is called by the `str()` built-in function and by the `print()` function to compute the "informal" string representation of an object.
4. `__add__(self, other)`: Define behavior for the `+` operator.
5. `__sub__(self, other)`: Define behavior for the `-` operator.
6. `__mul__(self, other)`: Define behavior for the `*` operator.
7. `__truediv__(self, other)`: Define behavior for the `/` operator.
8. `__floordiv__(self, other)`: Define behavior for the `//` operator.
9. `__mod__(self, other)`: Define behavior for the `%` operator.
10. `__pow__(self, other[, modulo])`: Define behavior for the `**` operator.
11. `__lt__(self, other)`: Define behavior for the `<` operator.
12. `__le__(self, other)`: Define behavior for the `<=` operator.
13. `__eq__(self, other)`: Define behavior for the `==` operator.
14. `__ne__(self, other)`: Define behavior for the `!=` operator.
15. `__gt__(self, other)`: Define behavior for the `>` operator.
16. `__ge__(self, other)`: Define behavior for the `>=` operator.
17. `__len__(self)`: Return the length of the object.
18. `__getitem__(self, key)`: Define behavior for indexing, like `obj[key]`.
19. `__setitem__(self, key, value)`: Define behavior for assigning to an indexed item, like `obj[key] = value`.
20. `__delitem__(self, key)`: Define behavior for deleting an indexed item, like `del obj[key]`.
21. `__iter__(self)`: Return an iterator object.
22. `__next__(self)`: Return the next item from the iterator.
23. `__contains__(self, item)`: Define behavior for membership tests using `in`.
24. `__call__(self[, args...])`: Allow the instance of the class to be called as a function.
25. `__enter__(self)`: Define behavior when entering a `with` statement.
26. `__exit__(self, exc_type, exc_value, traceback)`: Define behavior when exiting a `with` statement.
27. `__hash__(self)`: Return a unique hash value for the object.
28. `__getattr__(self, name)`: Define behavior for when a non-existent attribute is accessed.
29. `__setattr__(self, name, value)`: Define behavior for when an attribute is set.
30. `__delattr__(self, name)`: Define behavior for when an attribute is deleted.
31. `__dir__(self)`: Return the list of valid attributes for the object.

- **Source**: https://realpython.com/python-magic-methods/

## Python Generators

## License

Check out [license file](LICENSE)