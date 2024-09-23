# Polymorphism with Method Overloading Using *args

class Calculator:
    def calculate(self, *args):
        if len(args) == 1:
            # If one argument is passed, return the square
            return args[0] ** 2
        elif len(args) == 2:
            # If two arguments are passed, return their sum
            return args[0] + args[1]
        elif len(args) == 3:
            # If three arguments are passed, return their product
            return args[0] * args[1] * args[2]
        else:
            return "Unsupported number of arguments!"

# Create a Calculator object
calc = Calculator()

# Test with different numbers of arguments
result_square = calc.calculate(5)
print(f"Square of 5: {result_square}")  # Output: 25

result_sum = calc.calculate(5, 10)
print(f"Sum of 5 and 10: {result_sum}")  # Output: 15

result_product = calc.calculate(2, 3, 4)
print(f"Product of 2, 3, and 4: {result_product}")  # Output: 24

result_unsupported = calc.calculate(1, 2, 3, 4)
print(result_unsupported)  # Output: Unsupported number of arguments!
