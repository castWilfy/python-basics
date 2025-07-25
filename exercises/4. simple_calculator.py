"""
4. Simple Calculator
Create a calculator that can add, subtract, multiply, or divide two numbers based on user choice.
Workflow:

Get first number
Get operation (+, -, *, /)
Get second number
Calculate and display result
Handle division by zero

"""
def main():
    # Get first number
    num1 = float(input("Enter the first number: "))
    
    # Get operation
    operation = input("Enter an operation (+, -, *, /): ")
    
    # Get second number
    num2 = float(input("Enter the second number: "))
    
    # Perform calculation based on operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Invalid operation. Please use +, -, *, or /.")
        return
    
    # Display result
    print(f"The result of {num1} {operation} {num2} is: {result}")
