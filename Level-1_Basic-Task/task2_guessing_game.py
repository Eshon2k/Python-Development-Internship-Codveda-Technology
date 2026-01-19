import random

def number_guessing_game():
    # Generate a random integer between 1 and 100 inclusive
    number_to_guess = random.randint(1, 100)
    # Initialize the number of attempts to zero
    attempts = 0
    # Initialize the guessed flag to False
    guessed = False

    # Print welcome message
    print("Welcome to the Number Guessing Game!")
    # Print instructions for the player
    print("I have selected a number between 1 and 100. Can you guess it?")

    # Loop until the user guesses the number
    while not guessed:
        # Prompt the user to enter a guess and convert it to an integer
        user_guess = int(input("Enter your guess: "))
        # Increment the attempts counter
        attempts += 1

        # Check if the guess is less than the number to guess
        if user_guess < number_to_guess:
            print("Too low!")
        # Check if the guess is greater than the number to guess
        elif user_guess > number_to_guess:
            print("Too high!")
        # If the guess is correct
        else:
            guessed = True
            # Congratulate the user and show the number of attempts
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")

# Call the function to start the game
number_guessing_game()

