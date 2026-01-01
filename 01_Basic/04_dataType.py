#* Data type in python 
# Python Data Types - Complete Examples

print("=" * 50)
print("NUMERIC TYPES")
print("=" * 50)

# Integer
x = 5
print(f"int: {x}, type: {type(x)}")

# Float
y = 3.14
print(f"float: {y}, type: {type(y)}")

# Complex
z = 2 + 3j
print(f"complex: {z}, type: {type(z)}")

print("\n" + "=" * 50)
print("BOOLEAN TYPE")
print("=" * 50)

# Boolean
is_valid = True
print(f"bool: {is_valid}, type: {type(is_valid)}")

print("\n" + "=" * 50)
print("SEQUENCE TYPES")
print("=" * 50)

# String
text = "Hello, Python!"
print(f"str: {text}, type: {type(text)}")

# List
numbers = [1, 2, 3, 4, 5]
print(f"list: {numbers}, type: {type(numbers)}")

# Tuple
coords = (10, 20, 30)
print(f"tuple: {coords}, type: {type(coords)}")

# Range
letters = range(5)
print(f"range: {letters}, list(range): {list(letters)}, type: {type(letters)}")

print("\n" + "=" * 50)
print("SET TYPES")
print("=" * 50)

# Set
unique = {1, 2, 3, 3, 4}  # Duplicates automatically removed
print(f"set: {unique}, type: {type(unique)}")

# Frozenset
frozen = frozenset([1, 2, 3])
print(f"frozenset: {frozen}, type: {type(frozen)}")

print("\n" + "=" * 50)
print("MAPPING TYPE")
print("=" * 50)

# Dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
print(f"dict: {person}, type: {type(person)}")

print("\n" + "=" * 50)
print("BINARY TYPES")
print("=" * 50)

# Bytes
b = b"Hello"
print(f"bytes: {b}, type: {type(b)}")

# Bytearray
ba = bytearray(b"Hi")
print(f"bytearray: {ba}, type: {type(ba)}")

# Memoryview
mv = memoryview(b"Test")
print(f"memoryview: {mv}, type: {type(mv)}")

print("\n" + "=" * 50)
print("NONE TYPE")
print("=" * 50)

# None
nothing = None
print(f"NoneType: {nothing}, type: {type(nothing)}")

print("\n" + "=" * 50)
print("TYPE CONVERSION EXAMPLES")
print("=" * 50)

# Converting between types
print(f"int to float: {float(5)}")
print(f"float to int: {int(3.14)}")
print(f"int to str: {str(100)}")
print(f"str to list: {list('hello')}")
print(f"list to tuple: {tuple([1, 2, 3])}")
print(f"list to set: {set([1, 2, 2, 3])}")

