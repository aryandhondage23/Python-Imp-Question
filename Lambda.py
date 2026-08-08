# A lambda function is a small anonymous (nameless) function that can have any number of arguments but only one expression.

# Syntax
lambda arguments : expression

add=lambda x,y: x+y
print(add(5,6)) # Output: 11


square= lambda x: x*x
print(square(5)) # Output: 25


even= lambda x: x%2==0
print(even(4)) # Output: True
