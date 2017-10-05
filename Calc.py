class Calculator:

    # Addition method.
    def addition(number1, number2):
        return number1 + number2

    # Subtraction method.
    def subtraction(number1, number2):
        return number1 - number2

    # Multiplication method.
    def multiply(number1, number2):
        return number1 * number2

    # Division method.
    def division(number1, number2):
        # Simple error handling.
        if number2 == 0:
            print("No division by 0!")
            return 0
        else:
            return number1 / number2