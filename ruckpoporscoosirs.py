import random
while True:
    user_action = input("Enter a choice(rock, paper or scissors): ")
    possible_actions = ["rock","paper","scissors"]
    computers_actions = random.choice(possible_actions)
    print(f"\nYou chose{user_action}, and the computer chose{computers_actions}.\n")

    if user_action == computers_actions:
        print(f"Both players selected {computers_actions}. It's a tie!")
    
    elif user_action == "rock":
        if computers_actions == "scissors":
            print("Rock smashes scissors, YOU WIN!!!")
        else:
            print("Paper covers rock, YOU LOSE 😭")
    
    elif user_action == "paper":
        if computers_actions == "rock":
            print("Paper covers rock, YOU WIN!!!")
        else:
            print("Scissors cuts through paper, YOU LOSE 😡")

    elif user_action == "scissors":
        if computers_actions == "paper":
            print("Scissors cuts through paper, YOU WIN!!!")
        else:
            print("Rock smashes scissors, YOU LOSE ❌")
    play_again = input("Play again? (y/n): ")
    if play_again != "y":
        break