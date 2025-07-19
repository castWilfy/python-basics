# Get user input and store it in a variable
name = input("What's your name? ")

# This is a simple Python script that prints a message
print("Hello, world!")
print(name) #pass a variable to the print function

""" Multi line comment """
# Print in a single line
print("Hello, " + name + "!") # Concatenate strings to greet the user
print("Hello,", name) # Concatenate with a default space

""" Print Function Documentation
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

This function prints the objects to the text stream file, separated by sep and followed by end.
- *objects: The objects to be printed. Multiple objects can be passed.
"""

#String Manipulation
name = name.strip()  # Remove leading and trailing whitespace
name = name.capitalize()  # Capitalize the first letter of the string
name = name.title()  # Capitalize the first letter of each word

name = name.strip().capitalize().title()  # Combine both operations in one line

# Using f-string for formatted output
print(f"Hello, {name}!")