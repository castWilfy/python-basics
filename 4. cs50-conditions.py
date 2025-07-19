#*********************************************************************************
# Conditions in Python
# 1. IF-ELIF-ELSE Statement
# 2. OR and AND Operators
# 3. Match Statement
#*********************************************************************************

# 1. IF-ELIF-ELSE Statement
x = int(input("What's X?: "))
Y = int(input("What's Y?: "))

if x < Y:
    print("X is less than Y")
elif x > Y:
    print("X is greater than Y")
else:
    print("X is equal to Y")

# 2. OR and AND Operators
if x < Y or x > Y:   #Also valid: if x != Y:
    print("X is either less than or greater than Y")
else:
    print("X is equal to Y")

# Using AND operator
score = int(input("What's your score?: "))
if score>= 90 and score <= 100:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")   

#*********************************************************************************
# Even or Odd Check
#*********************************************************************************  
def main():
    number = int(input("Enter a number: "))
    if is_even(number):
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

def is_even(n):
    return n % 2 == 0  # Returns True if n is even, False if odd

#*********************************************************************************
# 3. Match Statement
#*********************************************************************************
day = input("Enter a day of the week: ").lower()
match day:
    case "monday":
        print("Start of the work week!")
    case "tuesday":
        print("It's Tuesday!")
    case "wednesday":
        print("Midweek already!")
    case "thursday":
        print("Almost there!")
    case "friday":
        print("Weekend is near!")
    case "saturday" | "sunday":  # Match both Saturday and Sunday
        print("It's the weekend!")
    case _:
        print("That's not a valid day!")