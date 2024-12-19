
import random
guess_number = random.randint(1, 10)
print(random.randint(1,10))

user_guess = int(input("Guess a number between 1 and 10: "))

if user_guess == guess_number:
    print("Congratulations! You guessed the right number.")
else:
    print("Sorry, your guess doesn't match.")



