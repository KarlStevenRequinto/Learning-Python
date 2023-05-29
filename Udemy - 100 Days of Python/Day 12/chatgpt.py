
import random

print("Welcome to the Number Guessing Game!")

# Prompt for difficulty level until a valid input is provided
while True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    print()

    if difficulty in ["easy", "hard"]:
        break

    print("Please choose between 'easy' and 'hard'")

print(f"Difficulty: {difficulty}")
print()
print("I'm thinking of a number between 1 and 100.")

number_to_guess = random.randint(1, 100)
attempts = 10 if difficulty == "easy" else 5

print(f"You have {attempts} attempts remaining to guess the number")
print()

# Main game loop
while attempts > 0:
    guess = int(input("Make a guess: "))

    if guess == number_to_guess:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess < number_to_guess:
        print("Too low. Guess a higher number.")
    else:
        print("Too high. Guess a lower number.")

    attempts -= 1
    print(f"You have {attempts} attempts remaining to guess the number")
    print()

# Out of attempts
if attempts == 0:
    print("Oops! You ran out of attempts. The number was", number_to_guess)