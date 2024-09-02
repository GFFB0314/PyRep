#Original version
from random import randint

def generate(max_value):
    answ = randint(1, max_value)
    while True:
        try:
            choice = int(input(f"Guess a number between 1-{max_value}: "))
            if choice == answ:
                print("Congratulation your guess was wright!")
                break
            elif choice < answ:
                print("Your guess is too low!")
            elif choice > answ:
                print("Your guess is too high!")
        except ValueError:
            print("Your guess was be correct number!")

def main():
    max = int(input("Enter the max value to guess to: "))
    generate(max)

if __name__ == "__main__":
    main()