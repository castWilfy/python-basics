import random;

def main():
    number = random.randint(1, 100)
    counter = 5

    while True:   
        if counter > 0:
            print(f"{counter} chances to go")
            guess = int(input("Guess the number: "))\
            
            if guess != number:
                print("Sorry, try again!")
                counter -= 1
            else:
                print("Awesome, numbers matched!")
                print(f"Awesome - {number} was the right answer")
                break
        else:
            print(f"No more chances left! The number was {number}.")
            break
main()