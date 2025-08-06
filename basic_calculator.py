#Basic calculator
num1= float(input("Enter first number: "))

#Get user input for the operation
operation = input("Enter operation (+, -, *, /): ")

#get user input for the second number
num2 = float(input("Enter second number: "))

#Perform the operation based on user input
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero is not allowed.")
        exit() #Exit the program if division by zero occurs
else:
    print("Error: Invalid operation. Please enter +, -, *, or /.")
    exit() #Exit the program if an invalid operation is entered
    # Print the result
print(f"The result of {num1} {operation} {num2} is: {result}")
#End of basic calculator