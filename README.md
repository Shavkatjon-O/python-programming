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

Resource: https://www.geeksforgeeks.org/decorators-in-python/

## Tutorials

### Youtube
- https://www.youtube.com/watch?v=KSiRzuSx120&list=PL7yh-TELLS1FuqLSjl5bgiQIEH25VEmIc&index=2

### w3schools
- https://www.w3schools.com/python/