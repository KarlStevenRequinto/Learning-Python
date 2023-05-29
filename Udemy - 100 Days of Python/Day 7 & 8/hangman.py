import random
word_list = ["ardvark", "resolving", "deltas", "windows", "microsoft"]

chosen_word = random.choice(word_list)
print(chosen_word)

display = []
lives = 6
for underscores in chosen_word:
    display += "_"
print(f"{' '.join(display)}")

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print("You lose.")
            end_of_game = True
            
        print(f"{lives} lives left.")
    if not end_of_game:
        print(f"{' '.join(display)}")
        

    if "_" not in display:
        print("You win!")
        end_of_game = True
