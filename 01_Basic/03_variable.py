# private variable 

#* Python is a object oriented programming language. In the object oriented programming, one of the key concept is encapsulation. If we want to implement the private variable in python, we have to use the ecapsulation concept.

# In python, a private variable is a variable that is only accessible within the class in which it is defined. To create a private variable in python, we need to prefix the variable name with double underscore __.

class Car:
    def __init__(self, name, year):
        self.name = name          # public variable
        self.__year = year        # private variable

    def display(self):
        print("Car Name: ", self.name)
        print("Car Year: ", self.__year)  # accessing private variable within the class


car1 = Car("Toyota", 2020)
car1.display()


# another example 

class MyClass:
    def __init__(self):
        self.__private_var = "I am Private"

    def show_private(self):
        return self.__private_var

obj = MyClass()
# print(obj.__private_var)   # ✗ AttributeError
print(obj.show_private())    # ✓ Access through method