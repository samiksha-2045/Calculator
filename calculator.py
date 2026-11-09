
# Simple Calculator

print("========== SIMPLE CALCULATOR ==========")

while True:

    # Input two numbers
    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))

    # Display operations
    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("\nEnter your choice (1-4): ")

    # Perform calculation
    if choice == "1":
        result = num1 + num2
        print("Result:", result)

    elif choice == "2":
        result = num1 - num2
        print("Result:", result)

    elif choice == "3":
        result = num1 * num2
        print("Result:", result)

    elif choice == "4":
        if num2 != 0:
            result = num1 / num2
            print("Result:", result)
        else:
            print("Error! Division by zero is not allowed.")

    else:
        print("Invalid operation! Please select between 1 and 4.")

    # Ask user whether to continue
    again = input("\nDo you want to calculate again? (yes/no): ")

    if again.lower() != "yes":
        print("\nThank you for using the calculator!")
        break
