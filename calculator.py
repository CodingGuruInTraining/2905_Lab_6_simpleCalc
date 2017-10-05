import Calc

def main():
    # Make new object.
    newCalculator = Calc.Calculator

    # Handle game loop.
    keepGoing = True
    while keepGoing:
        # Retrieves user inputs.
        num1 = getInput(1)
        op = getOperator()
        num2 = getInput(2)

        # Runs appropriate Class method.
        if op == "+":
            answer = newCalculator.addition(num1, num2)
        elif op == "-":
            answer = newCalculator.subtraction(num1, num2)
        elif op == "*":
            answer = newCalculator.multiply(num1, num2)
        elif op == "/":
            answer = newCalculator.division(num1, num2)

        # Displays results.
        showAnswer(num1, num2, op, answer)

        # Prompts user if they want to continue.
        wantsMore = input("Any more? (Y/N)")
        if wantsMore.lower() != "y":
            keepGoing = False

def getInput(number):
    # Gets number value and converts to int.
    value = input("Enter number " + str(number) + ": ")
    return int(value)

def getOperator():
    # Gets operator value.
    value = input("Enter operator symbol: ")
    return value

def showAnswer(number1, number2, operator, answer):
    # Prints equation followed by answer.
    print(str(number1) + " " + operator + " " + str(number2) + " = " + str(answer))

# Runs main.
main()

