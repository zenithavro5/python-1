# Everything You Need to Know About Python Decorators

## What is a Decorator?

A decorator is a design pattern in Python that allows you to modify or enhance functions or classes without permanently modifying their structure. Decorators wrap a function or class, modifying its behavior.

Think of decorators as gift wrappers: the gift (original function) stays the same, but you add extra layers (decorators) around it to enhance presentation or functionality.

## Basic Concept

In Python, functions are first-class objects, meaning they can be:
- Passed as arguments to other functions
- Returned from other functions
- Assigned to variables
- Stored in data structures

This is the foundation that makes decorators possible.

## Simple Function Example

```python
def greet(name):
    return f"Hello, {name}!"

# Functions can be assigned to variables
say_hello = greet
print(say_hello("Alice"))  # Hello, Alice!

# Functions can be passed as arguments
def call_function(func, name):
    return func(name)

print(call_function(greet, "Bob"))  # Hello, Bob!
```

## Creating Your First Decorator

### Basic Decorator Structure

```python
def my_decorator(func):
    def wrapper():
        print("Something before the function")
        func()
        print("Something after the function")
    return wrapper

def say_hello():
    print("Hello!")

# Apply decorator manually
decorated_hello = my_decorator(say_hello)
decorated_hello()
# Output:
# Something before the function
# Hello!
# Something after the function
```

### Using @ Syntax

The `@` symbol is syntactic sugar for applying decorators:

```python
def my_decorator(func):
    def wrapper():
        print("Something before")
        func()
        print("Something after")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Something before
# Hello!
# Something after
```

This is equivalent to: `say_hello = my_decorator(say_hello)`

## Decorators with Arguments

### Handling Function Arguments

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

add(5, 3)
# Output:
# Arguments: (5, 3), {}
# Result: 8
```

### Preserving Function Metadata

Use `functools.wraps` to preserve original function's metadata:

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function"""
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def my_function():
    """Original function"""
    pass

print(my_function.__name__)  # my_function (not wrapper)
print(my_function.__doc__)   # Original function (not Wrapper function)
```

## Common Decorator Patterns

### 1. Timing Decorator

```python
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done!"

slow_function()  # slow_function took 1.0001 seconds
```

### 2. Logging Decorator

```python
from functools import wraps
import logging

logging.basicConfig(level=logging.INFO)

def log_function_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_function_call
def add(a, b):
    return a + b

add(3, 5)
# INFO:root:Calling add with args=(3, 5), kwargs={}
# INFO:root:add returned 8
```

### 3. Caching/Memoization Decorator

```python
from functools import wraps

def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
            print(f"Calculating {func.__name__}{args}")
        else:
            print(f"Using cached result for {func.__name__}{args}")
        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))  # Calculates and caches
print(fibonacci(5))  # Uses cache
```

### 4. Authentication/Authorization Decorator

```python
from functools import wraps

def require_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Simulating authentication check
        authenticated = True  # In real app, check session/token
        if not authenticated:
            raise PermissionError("Authentication required")
        return func(*args, **kwargs)
    return wrapper

@require_auth
def sensitive_operation():
    return "Access granted to sensitive data"

sensitive_operation()
```

### 5. Retry Decorator

```python
from functools import wraps
import time

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Attempt {attempt + 1} failed: {e}. Retrying...")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=2)
def unreliable_function():
    import random
    if random.random() < 0.7:
        raise Exception("Random failure")
    return "Success!"
```

## Decorators with Arguments (Decorator Factories)

When you want to pass arguments to decorators, you need an extra layer of functions:

```python
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# Output:
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!
```

### Another Example with Arguments

```python
def validate_range(min_val, max_val):
    def decorator(func):
        @wraps(func)
        def wrapper(value):
            if not min_val <= value <= max_val:
                raise ValueError(f"Value must be between {min_val} and {max_val}")
            return func(value)
        return wrapper
    return decorator

@validate_range(0, 100)
def set_percentage(value):
    return f"Percentage set to {value}%"

print(set_percentage(50))   # Works
# print(set_percentage(150))  # Raises ValueError
```

## Stacking Multiple Decorators

You can apply multiple decorators to a single function:

```python
def decorator_one(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorator 1 - Before")
        result = func(*args, **kwargs)
        print("Decorator 1 - After")
        return result
    return wrapper

def decorator_two(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorator 2 - Before")
        result = func(*args, **kwargs)
        print("Decorator 2 - After")
        return result
    return wrapper

@decorator_one
@decorator_two
def my_function():
    print("Original function")

my_function()
# Output:
# Decorator 1 - Before
# Decorator 2 - Before
# Original function
# Decorator 2 - After
# Decorator 1 - After
```

Decorators are applied bottom-to-top (inner to outer).

## Class-Based Decorators

Decorators can also be implemented as classes:

```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call {self.count} of {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("Hello!")

say_hello()  # Call 1 of say_hello
say_hello()  # Call 2 of say_hello
say_hello()  # Call 3 of say_hello
```

## Decorating Classes

Decorators can also be applied to classes:

```python
def singleton(cls):
    instances = {}
    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Database:
    def __init__(self):
        print("Database initialized")

db1 = Database()  # Database initialized
db2 = Database()  # No output - returns same instance
print(db1 is db2)  # True
```

### Adding Methods to Classes

```python
def add_repr(cls):
    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"
    cls.__repr__ = __repr__
    return cls

@add_repr
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)
print(person)  # Person({'name': 'Alice', 'age': 30})
```

## Built-in Decorators

Python provides several built-in decorators:

### @property

Converts a method into a getter for a read-only attribute:

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
    @property
    def area(self):
        return 3.14159 * self._radius ** 2

circle = Circle(5)
print(circle.radius)  # 5
print(circle.area)    # 78.53975
circle.radius = 10    # Uses setter
```

### @staticmethod

Defines a method that doesn't receive the instance (self) or class (cls) as first argument:

```python
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

print(MathOperations.add(5, 3))  # 8
```

### @classmethod

Defines a method that receives the class as first argument:

```python
class Person:
    population = 0
    
    def __init__(self, name):
        self.name = name
        Person.population += 1
    
    @classmethod
    def get_population(cls):
        return cls.population

person1 = Person("Alice")
person2 = Person("Bob")
print(Person.get_population())  # 2
```

### @dataclass (Python 3.7+)

Automatically generates special methods:

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

point = Point(1.0, 2.0)
print(point)  # Point(x=1.0, y=2.0)
```

### @lru_cache (functools)

Caches function results:

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(100))  # Fast due to caching
```

## Advanced Patterns

### Decorator with Optional Arguments

```python
from functools import wraps

def optional_decorator(func=None, *, prefix=""):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            print(f"{prefix}Calling {f.__name__}")
            return f(*args, **kwargs)
        return wrapper
    
    if func is None:
        # Called with arguments
        return decorator
    else:
        # Called without arguments
        return decorator(func)

# Both of these work:
@optional_decorator
def func1():
    pass

@optional_decorator(prefix=">>> ")
def func2():
    pass

func1()  # Calling func1
func2()  # >>> Calling func2
```

### Context Manager Decorator


from contextlib import contextmanager

@contextmanager
def temporary_change(obj, attr, value):
    original = getattr(obj, attr)
    setattr(obj, attr, value)
    try:
        yield
    finally:
        setattr(obj, attr, original)

class Config:
    debug = False

config = Config()
print(config.debug)  # False

with temporary_change(config, 'debug', True):
    print(config.debug)  # True

print(config.debug)  # False
```

## Common Use Cases


### 1. Forgetting to return the result

```python
# Wrong
def bad_decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)  # Missing return!
    return wrapper

# Correct
def good_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def decorator(func):
    def wrapper():
        return func()
    return wrapper

@decorator
def my_func():
    """My docstring"""
    pass

print(my_func.__name__)  # wrapper (wrong!)
```

### 3. Decorator vs Decorator Factory confusion

```python
# This won't work
@repeat(3)  # Missing parentheses if repeat is not a factory
def greet():
    print("Hello")