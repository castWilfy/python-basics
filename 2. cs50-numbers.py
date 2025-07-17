#INT Operations
x = int(input("What's X?: "))
Y = int(input("What's Y?: "))
print(f"X + Y = {x + Y}")

#FLOAT Operations
a = float(input("What's A?: "))
b = float(input("What's B?: "))
rt = a + b

print(f"Total: {rt}")
print(f"Round Total: {round(rt, 2)}")  # Round to 2 decimal places
print(f"Formatted Total: {rt:.2f}")  # Format to 2 decimal places
print(f"Formatted Total with Commas: {rt:,.2f}")  # Format with commas and 2 decimal places