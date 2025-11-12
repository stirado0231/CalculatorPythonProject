# Simple 4 Function Calculator
# Each section includes required tags and shows basic Python concepts.

# FUNCTIONS
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b


# LIST
history = []

# BOOLEAN
active = True

# CONTROL LOOP
while active:
    print()
    print("Calculator")
    print()
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Show History")
    print("6. Exit")
    print()

    # INT
    try:
        operation = int(input("Select the number of the operation: "))
    except ValueError:  # ADDED: exception handling for invalid input
        print("Invalid input. Please enter a number from 1 to 6.")
        history.append("Invalid menu input")
        continue

    # ADDED: MAIN OPERATIONS
    if operation == 1:
        # FLOAT
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = addition(num1, num2)
            print("The sum is:", result)
            history.append(str(num1) + " + " + str(num2) + " = " + str(result))
        except ValueError:
            print("Invalid number. Please enter numeric values only.")
            history.append("Invalid numeric input for addition.")

    elif operation == 2:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = subtraction(num1, num2)
            print("The difference is:", result)
            history.append(str(num1) + " - " + str(num2) + " = " + str(result))
        except ValueError:
            print("Invalid number. Please enter numeric values only.")
            history.append("Invalid numeric input for subtraction.")

    elif operation == 3:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = multiplication(num1, num2)
            print("The multiplication is:", result)
            history.append(str(num1) + " * " + str(num2) + " = " + str(result))
        except ValueError:
            print("Invalid number. Please enter numeric values only.")
            history.append("Invalid numeric input for multiplication.")

    elif operation == 4:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if num2 == 0:
                print("Undefined (division by zero)")
                history.append(str(num1) + " / " + str(num2) + " = Undefined")
            else:
                result = division(num1, num2)
                print("The quotient is:", result)
                history.append(str(num1) + " / " + str(num2) + " = " + str(result))
        except ValueError:
            print("Invalid number. Please enter numeric values only.")
            history.append("Invalid numeric input for division.")

    elif operation == 5:
        if len(history) == 0:
            print("No history yet.")
        else:
            print("Calculation History:")
            for record in history:
                print(record)

    elif operation == 6:
        print("Exiting calculator...")
        active = False

    else:
        print("Invalid input, please select a number from 1 to 6.")
        history.append("Invalid menu selection")

# ADDED: End message
print()
print("Thank you for using the calculator!")
print("Session Summary:")
for i in history:
    print(i)


# TUPLE (stores last calculation in a fixed form)
if len(history) > 0:
    last_operation = ("Last Calculation", history[-1])
    print()
    print("Tuple Example:", last_operation)

# DICTIONARY (maps operation numbers to names)
operation_dict = {
    1: "Addition",
    2: "Subtraction",
    3: "Multiplication",
    4: "Division",
    5: "Show History",
    6: "Exit"
}
print()
print("Dictionary Example:")
for key, value in operation_dict.items():
    print(key, ":", value)
