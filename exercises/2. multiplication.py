"""
# 2. Multiplication Table

Question:
Create a program that prints the multiplication table for any number from 1 to 10.
Output: Enter a number: 7
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
...
7 x 10 = 70
"""

def main():
    number = int(input("Enter a number: "))
    
    print(f"Multiplication table for {number}:")
    
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

main()