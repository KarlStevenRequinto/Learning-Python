import random

print("Welcome to the Number Guessing Game!")
while True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    print(" ")

    if difficulty == "easy" or difficulty == "hard":
        break

    print("Please choose between 'easy' and 'hard'")

print(f"Difficulty: {difficulty}")
print(" ")
print("I'm thinking of a number between 1 and 100.")

number_to_guess = random.randint(1, 100)

attempts = 0
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
else:
    attempts = 0

print(f"You have {attempts} attempts remaining to guess the number")
print(" ")

while True:
    guess = int(input("Make a guess: "))

    if guess == number_to_guess:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess < number_to_guess:
        print("Too low. Guess a higher number.")
    else:
        print("Too high. Guess a lower number.")

    attempts -= 1
    if attempts == 0:
        print("Oops! You ran out of attempts. The number was", number_to_guess)
        break

    print(f"You have {attempts} attempts remaining to guess the number")
    print(" ")


