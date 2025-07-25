"""
6. Prime Number Checker
Create a program that checks if a number is prime and finds all prime numbers up to that number.

Example Output:
Enter a number: 20
20 is not a prime number
Prime numbers up to 20: 2, 3, 5, 7, 11, 13, 17, 19
"""
def main():
    number = int(input("Enter a number: "))
    
    if is_prime(number):
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
    
    primes_up_to_number = [i for i in range(2, number + 1) if is_prime(i)]
    print(f"Prime numbers up to {number}: {', '.join(map(str, primes_up_to_number))}")

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:  # Handle even numbers quickly
        return False
    
    # Check odd divisors from 3 upward
    for i in range(3, num, 2):
        if num % i == 0:
            return False
    return True

main()