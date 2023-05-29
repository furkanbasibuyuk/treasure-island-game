def game_start():
    print("""
    _                                       _     _                 _ 
    | |                                   (_)   | |               | |
    | |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
    | __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
    | |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
    \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
    """)
    print("Welcome to Treasure Island!")
    print("Your mission is to find the treasure.\n")

def choose_difficulty():
    while True:
        print("Select a difficulty level:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        difficulty = input("Enter the difficulty level (1-3): ")
        
        if difficulty in ["1", "2", "3"]:
            return int(difficulty)
        else:
            print("Invalid input! Please enter a number between 1 and 3.\n")

def get_left_or_right_choice():
    while True:
        user_choice = input('You are at a crossroad, where do you want to go? Type "left" or "right": ').lower()
        if user_choice in ["left", "right"]:
            return user_choice
        else:
            print("Invalid input! Please enter either 'left' or 'right'.\n")

def get_wait_or_swim_choice():
    while True:
        user_choice = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across: ').lower()
        if user_choice in ["wait", "swim"]:
            return user_choice
        else:
            print("Invalid input! Please enter either 'wait' or 'swim'.\n")

def get_color_choice():
    while True:
        user_choice = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose? ').lower()
        if user_choice in ["red", "yellow", "blue"]:
            return user_choice
        else:
            print("Invalid input! Please enter either 'red', 'yellow', or 'blue'.\n")


def play_game(difficulty):
    if difficulty == 1:
        max_wrong_choices = 2
    elif difficulty == 2:
        max_wrong_choices = 1
    else:
        max_wrong_choices = 0
    
    wrong_choices = 0

    choice1 = get_left_or_right_choice()
    
    if choice1 == "left":
        choice2 = get_wait_or_swim_choice()
        
        if choice2 == "wait":
            choice3 = get_color_choice()
            
            if choice3 == "yellow":
                print("WOW! YOU FOUND THE TREASURE!!!! YOU ARE THE WINNER!")
            else:
                print("Oops! You chose the wrong door. Game Over!")
                wrong_choices += 1
        else:
            print("Oops! You got attacked by sharks while swimming across the lake. Game Over!")
            wrong_choices += 1
    else:
        print("Oops! You fell into a hole. Game Over!")
        wrong_choices += 1
    
    if wrong_choices > max_wrong_choices:
        print("You made too many wrong choices. Game Over!")

def main():
    game_start()
    difficulty = choose_difficulty()
    play_game(difficulty)

main()
