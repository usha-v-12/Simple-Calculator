# Simple Calculator

# Get the first number from the user
num1 = float(input("Enter the first number: "))

# Get the second number from the user
num2 = float(input("Enter the second number: "))

# Choose the operation
print("\nSelect operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation = input("Enter the number of the operation (1/2/3/4): ")

# Perform the operation
if operation == "1":
    result = num1 + num2
    print("Result:", result)
elif operation == "2":
    result = num1 - num2
    print("Result:", result)
elif operation == "3":
    result = num1 * num2
    print("Result:", result)
elif operation == "4":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation choice")
