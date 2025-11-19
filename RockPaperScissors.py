# Rock Paper Scissors: Duel
# 5:30 Club Project
# Version 1.0

# Used .json for Settings file as .txt seemed trickier to format and manipulate
import json

# ================= ASCII Art =================
# This variable contains ASCII art to make the main block of code cleaner and more readable,
# but also serves as a nice header for the start of the Code :)
rps_art = """
                _    ,-,    _
         ,--, /   \\/'    \\/   \\
        |    '     '     |     |
        |    |     |     |     |.
        | D  |  U  |  E  |  L  ||
        |    |     |     |     | \\
         \\__/:     :     |     | |
              `---',\\___/,\\___/ /'
                   `==._ .._. /
"""

# ================= Constants & Globals =================
# This Dictionary defines which moves beat which other moves,
# used a list initially but this is easier to read and expand
rps_victor = {
    'rock': 'scissors',
    'scissors': 'paper',
    'paper': 'rock',
}

# ================= Functions =================

# This function loads settings from the settings.json file.
# It has default values in case the file isn't found.
def load_settings(filename="settings.json"):
    try:
        with open(filename, "r") as f:
            loaded_settings = json.load(f)
    except FileNotFoundError:
        loaded_settings = {
            "rps_match_bestof": 1,
            "player_one_name": "Player 1",
            "player_two_name": "Player 2",
        }
    return loaded_settings

# This functions opens the settings.json and writes to it with the
# json.dump function from json library.
def save_settings(filename="settings.json"):
    saved_settings = {
        "rps_match_bestof": rps_match_bestof,
        "player_one_name": player_one_name,
        "player_two_name": player_two_name
    }
    with open(filename, "w") as f:
        json.dump(saved_settings, f, indent=4)
    print("Settings saved!\n")

# This function "clears" the screen by adding many new lines so that
# input is anonymised, honour system implies you don't scroll up!
def clear_screen():
    print("\n" * 40)

# Simple pause functions so that text doesn't fly through without player input, 2 variants
def pause():
    input("Press enter to continue...")
def pause_main_menu():
    input("Press enter to return to the main menu...")

# This Function is Input Validation for the RPS Game
# Added dictionary to allow shortcuts for players
def check_valid_rps_input(player_name):
    valid_rps_input_shortcut = {"r": "rock", "rock": "rock",
                                "p": "paper", "paper": "paper",
                                "s": "scissors", "scissors": "scissors"}
    while True:
        choice = input(f"\n{player_name}, choose your weapon!\nRock (r), Paper (p) or Scissors (s)!\n>> ").strip().lower()
        checked_choice = valid_rps_input_shortcut.get(choice, choice)
        if checked_choice in ("rock", "paper", "scissors"):
            return checked_choice
        print("\nInvalid input, please enter rock, paper or scissors.")

# This function compares overall scores and declares a winner,
# iterating the global wins count for the respective player
def declare_winner(a, b):
    if a > b:
        print(f"\nThe final score is {a} - {b}\nThe winner is {player_one_name}!\n")
        global player_one_wins
        player_one_wins += 1
    elif a < b:
        print(f"\nThe final score is {a} - {b}\nThe winner is {player_two_name}!\n")
        global player_two_wins
        player_two_wins += 1
    else:
        print(f"\nThe final score is {a} - {b}\nIt's a tie, nobody wins today!\n")

# This is the main game function.
def rps_match_play(best_of, player_one, player_two):
    # Initial variables used in logic
    player_one_score = 0
    player_two_score = 0
    remaining_games = best_of
    required_wins = (best_of // 2) + 1
    # This logic determines if the loop continues, if there are more games because of Best_of setting
    # OR if it is calculated a player CANNOT reach the required number of wins
    while (remaining_games > 0
           and player_one_score < required_wins
           and player_two_score < required_wins):
        player_one_input = check_valid_rps_input(player_one)
        clear_screen()
        player_two_input = check_valid_rps_input(player_two)
        # Draw outcome
        if player_one_input == player_two_input:
            print("\nDRAW!"
                  "\nThe DUEL goes on...")
            pause()
        # if the inputs are evaluated as one of the winning combinations in rps_victor, Player 1 wins
        elif rps_victor[player_one_input] == player_two_input:
            remaining_games -= 1
            player_one_score += 1
            print(f"\n{player_one} Wins!"
                  f"\nThe game count stands at {player_one_score} - {player_two_score}!")
            pause()
        # else Player 2 wins
        else:
            remaining_games -= 1
            player_two_score += 1
            print(f"\n{player_two} Wins!"
                  f"\nThe game count stands at {player_one_score} - {player_two_score}!")
            pause()
    # Ending remarks, including an íf statement to inform the players if one can no longer win
    if remaining_games > 0:
        if player_one_score < required_wins:
            print(f"\n{player_one} can no longer win...")
        elif player_two_score < required_wins:
            print(f"\n{player_two} can no longer win...")
    declare_winner(player_one_score, player_two_score)
    print(f"The overall count stands at {player_one_wins} - {player_two_wins}!\n")
    pause_main_menu()

# ================= Main Body =================
# Initializes settings and some variables
settings = load_settings()
rps_match_bestof = settings["rps_match_bestof"]
player_one_name = settings["player_one_name"]
player_two_name = settings["player_two_name"]
player_one_wins = 0
player_two_wins = 0

# Menu Selection
while True:
    print("\n====================================================="
          "\nWelcome to ROCK PAPER SCISSORS: DUEL!"
          f"{rps_art}\n"
          "1: Begin Rock Paper Scissors!\n"
          "2: See Match History\n"
          "3: Settings\n\n"
          "Enter which Option you would like to select (1,2,3): "
          "\nEnter EXIT if you would like to end the program."
          "\n======================================================\n")

    menu_choice = input(">> ").strip().lower()

    # End of Program
    if menu_choice in ("exit", "end", "quit", "finish", "leave", "kill"):
        print("Ending Program, see you next time!")
        break

    # Main Game Loop, calls the Game Function for easier Readability
    elif menu_choice in ("1", "one"):
        rps_match_play(rps_match_bestof, player_one_name, player_two_name)

    # Simple log for Match History
    elif menu_choice in ("2", "two"):
        print(f"\nThe overall count stands at {player_one_wins} - {player_two_wins}!")
        pause_main_menu()

    # Settings Menu
    elif menu_choice in ("3", "three"):
        # Nested Settings Menu
        while True:
            print(f"\nCurrent Settings:"
                f"\n1: Best of             = {rps_match_bestof}"
                f"\n2: Player 1's Name     = {player_one_name}"
                f"\n3: Player 2's Name     = {player_two_name}"
                f"\n\nChoose a Setting to modify it (1,2,3):"
                f"\nInput anything else to return to the main menu."
                  )
            menu_choice_settings = input(">> ").strip().lower()

            # First selection to change Best of Setting, using try loop for input validation
            if menu_choice_settings in ("1", "one"):
                try:
                    new_bestof = int(input("\nPlease input how many games you want to play in each match: "
                                           "\nRemember, even numbers will lead to ties!\n\n>> "))
                    if new_bestof > 0:
                        rps_match_bestof = new_bestof
                        print(f"Matches are now set to a best of {rps_match_bestof}")
                        save_settings()
                    else:
                        print("\nPlease input a positive number.")
                        pause()
                except ValueError:
                    print("\nPlease input a valid integer.")
                    pause()

            # Second selection to change Player 1's name
            elif menu_choice_settings in ("2", "two"):
                player_one_name = input("\nPlease enter the new name for Player 1:\n>> ")
                save_settings()

            # Third selection to change Player 2's name
            elif menu_choice_settings in ("3", "three"):
                player_two_name = input("\nPlease enter the new name for Player 2:\n>> ")
                save_settings()

            # Any input returns to Main Menu, to prevent accidental changes to settings
            else:
                print("Returning to main menu...")
                break

    #Invalid input from User
    else:
        print("\nInvalid selection, please try again.")
        pause()