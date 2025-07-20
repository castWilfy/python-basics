#*********************************************************************************
# Loops in Python
# 1. While Loop
# 2. For Loop
# 3. Loop Control Statements (break, continue)
#*********************************************************************************

# 1. While Loop
i = 0
while i < 3:
    print(f"Iteration {i}")
    i += 1  # Increment i by 1

# 2. For Loop
for j in range(3):  # Loop from 0 to 2
    print(f"Iteration {j}")

# 3. List Iteration
fruits = ["apple", "banana", "cherry"] 
for fruit in fruits:
    print(fruit)

for fruit in range(len(fruits)):  # Using range to iterate over indices
    print(fruit, fruits[fruit])

# 4. Dictionary Iteration
person = {
            "name": "Alice", 
            "age": 30
}     
for key, value in person.items():
    print(f"{key}: {value}")

# 5. Dictionary in a list
student = [
    {"name": "Alice", "age": 30, "house": "Gryffindor"},
    {"name": "Bob", "age": 25, "house": "Hufflepuff"},
    {"name": "Charlie", "age": 35, "house": None}
]
for person in student:
    print(f"{person['name']} is {person['age']} years old and belongs to {person['house']}")