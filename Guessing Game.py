import random

def guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            user_guess = int(input("Enter your guess (between 1 and 100): "))
            attempts += 1

            if user_guess < 1 or user_guess > 100:
                print("Please enter a number within the specified range (1-100).")
                continue

            if user_guess < secret_number:
                print("Too low! Try guessing a higher number.")
            elif user_guess > secret_number:
                print("Too high! Try guessing a lower number.")
            else:
                print(f"Congratulations! You've guessed the correct number ({secret_number}) in {attempts} attempts!")
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")

guessing_game()

