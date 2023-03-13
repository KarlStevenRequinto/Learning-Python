import random

computer_choice = random.choice(["scissors","rock","paper"])
user_choice = input("Rock? Paper? or Scissors\n")

if computer_choice == user_choice:
    print("Its a Tie! The computer had "+str(computer_choice)+".")
elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice =="rock") or (user_choice == "scissors" and computer_choice =="paper"):
    print("You win! The computer had "+str(computer_choice)+".")
else:
    print("You lose!The computer had "+str(computer_choice)+".")