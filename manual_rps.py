import random
def get_user_choice():
    user_choice = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
#get_user_choice()
def get_computer_choice():
    #get_user_choice()
    possible_actions = ["rock", "paper", "scissors"]
    computer_choice = random.choice(possible_actions)
#get_computer_choice()

def get_winner():
    get_user_choice = get_user_choice()
    get_computer_choice = get_computer_choice()

    if get_user_choice == get_computer_choice:
        print(f"Both players selected {get_user_choice}. It's a tie!")
    elif get_user_choice == "rock":
        if get_computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif get_user_choice == "paper":
        if get_computer_choice == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif get_user_choice == "scissors":
        if get_computer_choice == "paper":
            print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
get_winner()
