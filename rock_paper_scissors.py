import random

print("Welcome to Rock, Paper, Scissors Game!")
user_score = 0
computer_score = 0

while True:
    user_choice = input("\nChoose Rock, Paper, or Scissors: ").lower()

    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
        user_score += 1
    elif user_choice in choices:
        print("You lose!")
        computer_score += 1
    else:
        print("Invalid choice! Please choose Rock, Paper, or Scissors.")
        continue  

    print(f"Score => You: {user_score} | Computer: {computer_score}")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!  Final Score:")
        print(f"You: {user_score} | Computer: {computer_score}")
        break
