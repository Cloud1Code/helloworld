import random

# Function to play the game
def play_game():
    # Generate a random number
    secret_number = random.randint(1, 10)

    # Allow the user for a guess
    user_guess = int(input("Guess a number between 1 and 10: "))

    # Check if the guess matches the secret number
    if user_guess == secret_number:
        print("Congratulations! You guessed the right number.")
    else:
        print("Sorry, your guess doesn't match the secret number.")

# Main loop to play the game again
while True:
    play_game()

    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no) ")
    if play_again.lower() != "yes":
        break