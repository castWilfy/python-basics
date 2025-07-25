"""
# 1. Number Classifier

Question:
Write a program that asks for a number and prints whether it's:
- Positive, negative, or zero
- Even or odd
- Single digit, double digit, or more

"""
def main():
    number = int(input("Enter a number: "))
    
    print(f"The number {number} is:")
    
    # Classify positive, negative, or zero
    if number > 0:
        print("- Positive")
    elif number < 0:
        print("- Negative")
    else:
        print("- Zero")
    
    # Check if even or odd (skip for zero if desired)
    if number != 0:  # Optional: skip even/odd for zero
        if number % 2 == 0:
            print("- Even")
        else:
            print("- Odd")
    
    # Check the number of digits using absolute value
    abs_number = abs(number)
    if abs_number < 10:
        print("- Single digit")
    elif abs_number < 100:
        print("- Double digit")
    else:
        print("- More than two digits")

main()