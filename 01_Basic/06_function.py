# Function in in python 

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
print(greet("Bob"))

print("\n" + "=" * 60)
print("2. POSITIONAL ARGUMENTS")
print("=" * 60)

def add(a, b):
    return a + b

def subtract(a, b, c):
    return a - b - c

print(f"add(5, 3) = {add(5, 3)}")
print(f"subtract(10, 2, 1) = {subtract(10, 2, 1)}")

print("\n" + "=" * 60)
print("3. DEFAULT ARGUMENTS")
print("=" * 60)

def greet_custom(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet_custom("Alice"))                    # Uses default
print(greet_custom("Bob", "Hi"))                # Custom greeting
print(greet_custom("Charlie", greeting="Hey"))  # Named argument

print("4. KEYWORD ARGUMENTS")
print("=" * 60)

def describe_person(name, age, city):
    return f"{name} is {age} years old and lives in {city}"

# Can call with keywords in any order
print(describe_person(name="Alice", age=30, city="NYC"))
print(describe_person(city="LA", name="Bob", age=25))
print(describe_person("Charlie", city="Chicago", age=35))  # Mixed

print("\n" + "=" * 60)
print("5. *args - VARIABLE POSITIONAL ARGUMENTS")
print("=" * 60)

def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(f"sum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
print(f"sum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")
print(f"sum_all(10) = {sum_all(10)}")

def print_items(*items):
    for i, item in enumerate(items, 1):
        print(f"  Item {i}: {item}")

print("print_items('apple', 'banana', 'cherry'):")
print_items('apple', 'banana', 'cherry')

print("\n" + "=" * 60)
print("6. **kwargs - VARIABLE KEYWORD ARGUMENTS")
print("=" * 60)

def display_info(**info):
    for key, value in info.items():
        print(f"  {key}: {value}")

print("display_info(name='Alice', age=30, city='NYC'):")
display_info(name='Alice', age=30, city='NYC')

print("\ndisplay_info(product='Laptop', price=999, brand='TechCo'):")
display_info(product='Laptop', price=999, brand='TechCo')

print("\n" + "=" * 60)
print("7. COMBINING ALL ARGUMENT TYPES")
print("=" * 60)

def complex_function(a, b, c=10, *args, **kwargs):
    print(f"  a={a}, b={b}, c={c}")
    print(f"  args={args}")
    print(f"  kwargs={kwargs}")

print("complex_function(1, 2):")
complex_function(1, 2)

print("\ncomplex_function(1, 2, 3, 4, 5, x=100, y=200):")
complex_function(1, 2, 3, 4, 5, x=100, y=200)

print("\n" + "=" * 60)
print("8. RETURN VALUES")
print("=" * 60)

# Single return
def square(x):
    return x ** 2

print(f"square(5) = {square(5)}")

# Multiple returns (returns as tuple)
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

min_val, max_val, total = get_stats([1, 2, 3, 4, 5])
print(f"get_stats([1,2,3,4,5]) = min:{min_val}, max:{max_val}, sum:{total}")

# No explicit return (returns None)
def print_message(msg):
    print(f"  Message: {msg}")

result = print_message("Hello")
print(f"Function with no return gives: {result}")

print("\n" + "=" * 60)
print("9. SCOPE - LOCAL vs GLOBAL")
print("=" * 60)

global_var = "I'm global"

def test_scope():
    local_var = "I'm local"
    print(f"  Inside function: {global_var}")
    print(f"  Inside function: {local_var}")

test_scope()
print(f"Outside function: {global_var}")
# print(local_var)  # This would cause an error

# Modifying global variables
counter = 0

def increment():
    global counter
    counter += 1
    return counter

print(f"increment() = {increment()}")
print(f"increment() = {increment()}")
print(f"Global counter = {counter}")

print("\n" + "=" * 60)
print("10. LAMBDA FUNCTIONS (Anonymous)")
print("=" * 60)

square = lambda x: x ** 2
add = lambda a, b: a + b
multiply = lambda x, y, z: x * y * z

print(f"square(5) = {square(5)}")
print(f"add(3, 7) = {add(3, 7)}")
print(f"multiply(2, 3, 4) = {multiply(2, 3, 4)}")

# Lambda with map, filter
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(f"Squared: {squared}")
print(f"Evens: {evens}")

print("\n" + "=" * 60)
print("11. DOCSTRINGS")
print("=" * 60)

def calculate_area(radius):
    """
    Calculate the area of a circle given its radius.
    
    Args:
        radius (float): The radius of the circle
    
    Returns:
        float: The area of the circle
    """
    return 3.14159 * radius ** 2

print(f"calculate_area(5) = {calculate_area(5)}")
print(f"\nDocstring: {calculate_area.__doc__}")

print("\n" + "=" * 60)
print("12. TYPE HINTS (Python 3.5+)")
print("=" * 60)

def add_typed(a: int, b: int) -> int:
    return a + b

def greet_typed(name: str, times: int = 1) -> str:
    return (name + "! ") * times

print(f"add_typed(5, 3) = {add_typed(5, 3)}")
print(f"greet_typed('Hello', 3) = {greet_typed('Hello', 3)}")

print("\n" + "=" * 60)
print("13. NESTED FUNCTIONS")
print("=" * 60)

def outer(x):
    def inner(y):
        return x + y
    return inner

add_5 = outer(5)
print(f"add_5(10) = {add_5(10)}")
print(f"add_5(20) = {add_5(20)}")

print("\n" + "=" * 60)
print("14. FUNCTIONS AS FIRST-CLASS OBJECTS")
print("=" * 60)

def apply_operation(func, x, y):
    return func(x, y)

def multiply(a, b):
    return a * b

result = apply_operation(multiply, 5, 3)
print(f"apply_operation(multiply, 5, 3) = {result}")

result = apply_operation(lambda a, b: a - b, 10, 3)
print(f"apply_operation(lambda, 10, 3) = {result}")

print("\n" + "=" * 60)
print("15. UNPACKING IN FUNCTION CALLS")
print("=" * 60)

def show_coordinates(x, y, z):
    return f"x={x}, y={y}, z={z}"

coords = [10, 20, 30]
print(f"show_coordinates(*coords) = {show_coordinates(*coords)}")

person = {'name': 'Alice', 'age': 30, 'city': 'NYC'}
print(f"describe_person(**person) = {describe_person(**person)}")

print("\n" + "=" * 60)
print("16. MUTABLE DEFAULT ARGUMENTS (GOTCHA!)")
print("=" * 60)

# WRONG WAY - mutable default argument
def add_item_wrong(item, items=[]):
    items.append(item)
    return items

print(f"add_item_wrong('a') = {add_item_wrong('a')}")
print(f"add_item_wrong('b') = {add_item_wrong('b')}")  # Unexpected!

# RIGHT WAY - use None as default
def add_item_right(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(f"add_item_right('a') = {add_item_right('a')}")
print(f"add_item_right('b') = {add_item_right('b')}")  # Correct!
