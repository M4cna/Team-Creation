import random as r
from colorama import init, Fore

# Initialize colorama for colored terminal output
init()
print("-" * 30)
kisi = int(input(Fore.GREEN + "How many people: " + Fore.RESET))
print("-" * 30)
print(Fore.GREEN + "WELCOME TO THE MINI FOOTBALL TEAM CREATION APPLICATION" + Fore.RESET + Fore.WHITE + " WELCOME" + Fore.RESET)
secim = (
    Fore.LIGHTCYAN_EX + "1- ADD_PLAYER" + Fore.RESET +
    Fore.LIGHTBLACK_EX + "\n2- VIEW_TEAM" + Fore.RESET +
    Fore.LIGHTYELLOW_EX + "\n3- RANDOM_BALL_SELECTION\n" + Fore.RESET +
    Fore.LIGHTMAGENTA_EX + "4- SHUFFLE_TEAMS" + Fore.RESET
)
team1 = list()
team2 = list()
all_players = list()

def ADD_PLAYER():
    print("-" * 30)
    print(Fore.LIGHTCYAN_EX + "PLAYER ENTRY SCREEN" + Fore.RESET)
    print("-" * 30)
    for i in range(kisi):
        # Taking player input and adding to all players list
        player = input("Please enter player name: ")
        all_players.append(player)
    input("Continue? Press ENTER to proceed")
    print("-" * 30)

def VIEW_TEAM():
    print("-" * 30)
    print(Fore.LIGHTBLACK_EX + "YOU ARE IN THE PLAYER VIEW SCREEN" + Fore.RESET)
    print("-" * 30)
    team_to_view = int(input("Do you want to view team 1 or team 2: "))
    if team_to_view == 1:
        count = 1
        for player in team1:
            print(count, "- Player name: ", player)
            count += 1
        print("-" * 30)
    elif team_to_view == 2:
        count = 1
        for player in team2:
            print(count, "- Player name: ", player)
            count += 1
        print("-" * 30)
    else:
        print("Please enter a value between 1 and 2")
    input("Continue? Press ENTER to proceed")
    print("-" * 30)

def RANDOM_BALL_SELECTION():
    print("-" * 30)
    teams = [Fore.LIGHTBLUE_EX + "TEAM 1" + Fore.RESET, Fore.LIGHTRED_EX + "TEAM 2" + Fore.RESET]
    selected_team = r.choice(teams)
    print("-" * 30)
    print(Fore.LIGHTGREEN_EX + "The team that gets the ball: " + selected_team + Fore.RESET)
    print("-" * 30)

def SHUFFLE_TEAMS(x, y):
    print("-" * 30)
    # Clear existing teams
    x.clear()
    y.clear()
    # Shuffle all players and split them into two teams
    r.shuffle(all_players)
    half = kisi // 2
    x.extend(all_players[:half])
    y.extend(all_players[half:])
    print("-" * 30)
    print("Shuffling completed..")
    print("-" * 30)
    input("Continue? Press ENTER to proceed")
    print("-" * 30)

while True:
    print(secim)
    print("-" * 30)
    choice = int(input("Please choose an action: "))
    print("-" * 30)
    if choice == 1:
        ADD_PLAYER()
    elif choice == 2:
        VIEW_TEAM()
    elif choice == 3:
        RANDOM_BALL_SELECTION()
    elif choice == 4:
        SHUFFLE_TEAMS(team1, team2)
    else:
        print("-" * 30)
        print("Please choose a number between 1 and 4")
        print("-" * 30)