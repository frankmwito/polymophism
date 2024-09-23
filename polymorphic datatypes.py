# Polymorphic Function for Different Data Types

def add_elements(a, b):
    return a + b

# Testing with two integers
result_int = add_elements(5, 3)
print(f"Adding integers: {result_int}")  # Output: 8

# Testing with two strings
result_str = add_elements("Hello, ", "world!")
print(f"Adding strings: {result_str}")  # Output: Hello, world!

# Testing with two lists
result_list = add_elements([1, 2, 3], [4, 5, 6])
print(f"Adding lists: {result_list}")  # Output: [1, 2, 3, 4, 5, 6]
