import random

emojis={'r':'rock','p':'paper','s':'scissors'}
choice=['r','p','s']


def get_user_choices():
    while True:
        user_choice=input("rock,paper, or scissors? ")
        if user_choice in choice:
            return user_choice
        else:
            print("invalid choice")



def display_user_choice(user_choice,computer_choices):
    print(f"You chose {emojis[user_choice]}")
    print(f"computer chose {emojis[computer_choices]}")


def determine_winner(user_choice,computer_choices):
    if user_choice== computer_choices:
        print("Tie!")
    elif ((user_choice=='r' and computer_choices=='s') or(user_choice=='s' and computer_choices=='p') or (user_choice=='p' and computer_choices=='r')):
        print("You won!")
    else:
        print("You lost!")


def play_game():
    while True:
        user_choice=get_user_choices()

        computer_choices=random.choice(choice)

        display_user_choice(user_choice,computer_choices)

        determine_winner(user_choice,computer_choices)

        should_continue=input("continue?(y/n): ").lower()
        if should_continue == 'n':
            print("thanks for playing! ")
            break
play_game()



