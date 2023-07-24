# Python doctrings are the string literals that appear right after the definition of a function, method, class, or module.

def square(n):
    ''' Takes in a number n, returns the square of n'''
    print(n**2)
square(5)

# prints the docstring
print(square.__doc__) # __.doc__ attribute

# Docstrings are used right above the function definition, method, class, or module (like in Example above). They are used to document our code.
# We can access these doctrings using the doc attribute.

def square(n):
    print(n)
    ''' Takes in a number n, returns the square of n'''
    print(n**2)
square(5)

# prints the docstring as None because doctrings always come right after the function definition
print(square.__doc__) # __.doc__ attribute

# PEP-8 (Python Enhancement Proposal)
# It is a document which tells how to write a proper and maintainable code in Python

# Zen of Python, by Tim Peters is a poem written by him. You can read it by writing "import this" on console
