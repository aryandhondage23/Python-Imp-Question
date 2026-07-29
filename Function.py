# 17)with Parameter and without parameter
# Function Without Parameters
# A function that does not take any input.

def greet():
    print("Hello! Welcome to the program.")
greet()  # Output: Hello! Welcome to the program.


# Function With Parameters
# A function that takes input values (parameters).

def greet(name):
    print("Hello", name)

greet("Aryan")


#18)multiple value we can store in function by args (*)

# ans= Yes. In Python, *args allows a function to accept multiple values (variable number of arguments).

def num(*args):
    print("The numbers are:", args)
num(1, 2, 3, 4, 5)  # Output: The numbers are: (1, 2, 3, 4, 5)


# 19)multiple value store by kwargs (**)

# ans= Yes. **kwargs is used to pass multiple keyword arguments to a function. The values are stored as a dictionary.
def display(**kwargs):
    print(kwargs)

display(name="Aryan", age=20, city="Pune")