# This code demonstrates the use of a decorator in Python to modify the behavior of functions.
# It includes both a manual application of the decorator and the use of the @ syntax.
# The decorator pattern is used when you want to add functionality to existing functions without modifying their code.
# We can add pre-processing and post-processing steps around the function call. We can't change the inner logic of the function itself.
#  The return value of the function can be modified or logged, but the core logic remains intact.
# the return value must be defined in some way so your decorator can process it.


def myDecorator(funcObject):
    def innerFunction(*args, **kwargs):
        print("Before calling the function")
        print(f"Arguments passed: {args}, {kwargs}")
        result = funcObject(*args, **kwargs)
        print("After calling the function")
        print(f"Result returned: {result}")
        return result
    return innerFunction

def myFunction(a,b,c):
    print("Inside myFunction")
    print(f"a: {a}, b: {b}, c: {c}")
    rs1 = a + b
    rs2 = b + c
    rs3 = rs1 + rs2
    return rs3

myFunction = myDecorator(myFunction)  # this is normal function of decorator without special syntax
myFunction(1, c=3,  b=2)  # calling the decorated function with kwargs

print()
print()

myFunction2 = myDecorator(lambda a, b, c: a + b + c)  # applying the decorator to a lambda with 3 args
myFunction2(1, 2, 3)  # calling the decorated lambda function

print()
print()


# With special syntax using @
@myDecorator
def anotherFunction(x, y):
    print("Inside anotherFunction")
    print(f"x: {x}, y: {y}")
    return x * y
anotherFunction(4, 5)  # calling the decorated function with @ syntax

print()
print()

class MyClass:
    @myDecorator
    def method(self, x, y):
        print("Inside MyClass.method")
        print(f"x: {x}, y: {y}")
        return x - y
    
my_instance = MyClass()
my_instance.method(10, 3)  # calling the decorated method of the class instance

print()
print()

# Yes, you can add decorators to classes as well.
# Class decorators receive the class object and can modify or replace it.

def classDecorator(cls):
    print(f"Decorating class: {cls.__name__}")
    cls.decorated = True  # Add an attribute to the class
    return cls

@classDecorator
class DecoratedClass:
    def greet(self):
        print("Hello from DecoratedClass!")

instance = DecoratedClass()
instance.greet()
print(f"Is class decorated? {DecoratedClass.decorated}")


print()
print()
# You can also decorate static methods using the @staticmethod decorator along with your custom decorator.

class StaticDemo:
    @staticmethod
    @myDecorator
    def static_method(x, y):
        print("Inside StaticDemo.static_method")
        return x / y

StaticDemo.static_method(10, 2)

print()
print()

# Applying multiple decorators: The decorators are applied from the closest to the function outward (bottom to top).

def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Decorator 1: Before function")
        result = func(*args, **kwargs)
        print("Decorator 1: After function")
        return result
    return wrapper

def decorator2(func):
    def wrapper(*args, **kwargs):
        print("Decorator 2: Before function")
        result = func(*args, **kwargs)
        print("Decorator 2: After function")
        return result
    return wrapper

@decorator1
@decorator2
def multi_decorated(x, y):
    print(f"Inside multi_decorated: x={x}, y={y}")
    return x + y

multi_decorated(5, 7)