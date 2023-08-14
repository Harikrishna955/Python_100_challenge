def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


operations = {
    "+": add,
    "-": subtract,
    "*": multiplication,
    "/": division
}


def calculation():
    number1 = float(input('Enter first number: '))
    should_continue = True
    while should_continue:
        for operation in operations:
            print(operation)
        operation_symbol = input("select an operation from above: ")
        number2 = float(input('Enter the next number: '))
        answer = operations[operation_symbol](number1, number2)
        print(f"{number1} {operation_symbol} {number2} = {answer}")
        print(f"Do you want to continue with the calculation or not")
        again = input("type Y(yes) or N(no)").lower()
        if again == 'y' or 'yes':
            number1 = answer
        else:
            should_continue = False
            print(f"do you want or want to perform new calculation")
            if input("type Y(yes) to perform new calculation or N(no) to terminate the program: ")[0].lower() == 'y':
                calculation()


calculation()
