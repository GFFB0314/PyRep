#Additional functionalities
from random import randint

def generate(max_value):
    count = 0
    answ = randint(1, max_value)
    while True:
        try:
            count += 1
            choice = int(input(f"Guess a number between 1-{max_value}: "))
            if choice == answ:#since decision() isn't returning any value, it will always break the loop
                print("Your guess was right!")#because when a function doesn't return a value it implicitely return 'None' which is consider as false.
                if decision(count):
                    pass
                else:
                    break
            elif choice < answ:
                print("Your guess is too low!")
            elif choice > answ:
                print("Your guess is too high!")
        except ValueError:
            print("Your guess has to be a number!")


def decision(count):
    #decision doesn't return any value
    if count <= 3:
        print("You won the game!")
    else:
        print("But you loose the game!")

def main():
    max = int(input("Enter the max value to guess to: "))
    generate(max)

if __name__ == "__main__":
    main()
