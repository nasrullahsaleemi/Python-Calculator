## Creating a List to record History
history = []


## Defining a Function to allow user to select from a Menu
def printing():
    # Creating Menu
    print("=============================")
    print("      Python Calculator      ")
    print("=============================")
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. View History")
    print("8. Clear History")
    print("9. Exit")

    # Asking user for input and validating it
    while True:
        try:
            selection = int(input("Select an option: "))
        except ValueError:
            print("Enter a Number 😑")
            continue
        if selection >= 1 and selection <= 9:
            return selection
        else:
            print("Invalid Selection ❌")
            continue


## Creating an adition Funciton
def add(x, y):
    addition = x + y
    return addition

## Creating a Substraction Funciton
def sub(x, y):
    subtract = y - x
    return subtract

## Creating a Multiply Function
def mul(x, y):
    multiply = x * y
    return multiply

## Creating a divide Function
def divide(x, y):
    try:
        division = x / y
    except ZeroDivisionError:
        division = "Undefined"
    
    return division

## Creating a power Funciton
def power(x, y):
    power1 = x ** y
    return power1

## Creating a Square root Function
def sr(x):
    squareroot = x ** 0.5
    return squareroot

## Creating a Function to view History
def his():
    if history == []:
        print("--------- History --------")
        print("  No Calculation History  ")
        print("--------------------------")
    else:
        print("--------- History --------")
        for i in history:
            print(f"  {i}")
        print("--------------------------")

## Creating Function to clear history
def clearhis():
    history.clear()

## Main source code
def main():
    while True:
        # Storing the printing() value into selection1 variable
        selection1 = printing()
        # Reseting Values
        x = 0
        y = 0
        if selection1 == 1:
            x = float(input("Enter First Value: "))
            y = float(input("Enter Second Value: "))
            answer = add(x, y)
            print("----")
            print(f"{x} + {y} = {answer}")
            history.append(f"{x} + {y} = {answer}")
        elif selection1 == 2:
            x = float(input("What do you want to Subtract: "))
            y = float(input("From what: "))
            answer = sub(x, y)
            print("----")
            print(f"{y} - {x} = {answer}")
            history.append(f"{y} - {x} = {answer}")
        elif selection1 == 3:
            x = float(input("Enter First Value: "))
            y = float(input("Enter Second Value: "))
            answer = mul(x, y)
            print("----")
            print(f"{x} * {y} = {answer}")
            history.append(f"{x} * {y} = {answer}")
        elif selection1 == 4:
            x = float(input("Enter Numerator: "))
            y = float(input("Enter Denominator: "))
            answer = divide(x, y)
            print("----")
            print(f"{x} / {y} = {answer}")
            history.append(f"{x} / {y} = {answer}")
        elif selection1 == 5:
            x = float(input("Enter First Value: "))
            y = float(input("Enter Second Value (Power): "))
            answer = power(x, y)
            print("----")
            print(f"{x} ^ {y} = {answer}")
            history.append(f"{x} ^ {y} = {answer}")
        elif selection1 == 6:
            x = float(input("Enter Value to Find Square Root: "))
            answer = sr(x)
            print("----")
            print(f"Square Root of {x} = {answer}")
            history.append(f"√{x} = {answer}")
        elif selection1 == 7:
            his()
        elif selection1 == 8:
            clearhis()
            print("History Cleared ✅")
        else:
            print("Thank you for using the calculator!")
            break

main()