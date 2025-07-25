"""
Write a program that prints different patterns based on user input:

1. Triangle Pattern
*
**
***
****
*****
"""
def main():
    # Get the number of rows for the triangle pattern
    tri_rows = int(input("Enter the number of rows for the triangle pattern: "))
    pyra_rows = int(input("Enter the number of rows for the pyramid pattern: "))
    triangle_pattern(tri_rows)
    triangle_pyramid(tri_rows)
    number_pyramid(pyra_rows)


def triangle_pattern(num_rows):
    print("Triangle Pattern:")
    for i in range(1, num_rows + 1):
        print('*' * i)

def triangle_pyramid(num_rows):
    print("Triangle Pyramid:")
    for i in range(1, num_rows + 1):
        # Build the number sequence as a list
        pattern = []
        
        # Add ascending: 1, 2, 3, ..., i
        for num in range(1, i + 1):
            pattern.append("*")

        # Add descending: i-1, i-2, ..., 1
        for num in range(i - 1, 0, -1):
            pattern.append("*")

# Create spaces and combine
        spaces = " " * (num_rows - i)
        line = spaces + "".join(pattern)
        print(line)


def number_pyramid(py_rows):
    print("Pyramid Pattern:")
    for i in range(1, py_rows + 1):
        # Build the number sequence as a list
        numbers = []
        
        # Add ascending: 1, 2, 3, ..., i
        for num in range(1, i + 1):
            numbers.append(num)
        
        # Add descending: i-1, i-2, ..., 1
        for num in range(i - 1, 0, -1):
            numbers.append(num)
        
        # Create spaces and combine
        spaces = " " * (py_rows - i)
        line = spaces + "".join(map(str,numbers))
        print(line)

main()