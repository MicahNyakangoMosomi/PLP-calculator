# Ask for the first number
num1 = float(input("Enter the first number: "))

# Ask for the second number
num2 = float(input("Enter the second number: "))

# Ask for the operation
operation = input("Enter an operation (+, -, *, /): ")

# Perform the operation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero.")
        exit()
    result = num1 / num2
else:
    print("Invalid operation")
    exit()

# Print the result
print(f"{num1} {operation} {num2} = {result}")
