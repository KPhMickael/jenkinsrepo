# test_pylint.py

def greet(name):
    # This function greets the person passed in as parameter
    print('Hello, ' + name)

def calculate_sum(a, b):
    """Calculate the sum of two numbers."""
    return a + b

# Mixing styles can lead to style warnings
def mixed_style():
    a = 1
    b = 2
    return a + b

# Unused variable
unused = 10

greet("World")
print(calculate_sum(5,3))

# This function is defined but never called
def unused_function():
    pass

# Long line to exceed max line length
this_is_a_really_long_variable_name_that_will_probably_exceed_the_80_character_limit_set_by_most_style_guidelines = "Long string"

# Missing docstring for a module
