# Homework 3 - Board Game System
# Name: Rinku Mahato
# Date: 04/03/2026

def loadGameData(filename):
    """Reads game data from a file and returns it as a list."""
    data = []
    with open(filename, "r") as file:
        for line in file:
            data.append(line.strip())
    return data


def saveGameData(filename, data):
    """updated game state back to the file"""
    with open(filename, "w") as file:
        for item in data:
            file.write(item + "\n")

def displayGame(data):
    """Displays the current game state."""
    print("\nCurrent Game State:")
    for item in data:
        print(item)

def switchTurn(data):
    """switch to the next player """
    players = []
    turn_index = -1
    current_turn = None

    # find current turn and collect players
    for i in range(len(data)):
        if data [i].startswith("Turn:"):
            turn_index = i 
            current_turn = data[i].split(": ")[1]
        else:
            parts = data[i].split(": ")
            if parts [0].isdigit():
                name = parts[1]
                if name.startswith("Player"): #only real players
                    players.append(name)
    
    if not players:
        return
    #find next player
    if current_turn in players:
        next_index = (players.index(current_turn)+ 1) % len(players)
        next_player = players[next_index]
    else:
        next_player = players[0]

    #replace Turn 
    data[turn_index] = f"Turn: {next_player}"
    print(f"Turn changed to {next_player}")


def movePlayer(data):

    """Example function to simulate moving a player."""
    
    player = input("Enter player name: ")

    #check whose turn it is
    current_turn = None
    for item in data:
        if item.startswith("Turn:"):
            current_turn = item.split(": ")[1]
            break

    if player !=current_turn:
        print(f"It's not your turn! It's {current_turn}'s turn")
        return
    
    steps = int(input("Enter steps to move: "))

    index = -1
    current_pos = 0 


    #Find Player 
    for i in range(len(data)):
        parts = data[i].split(": ")
        if not parts[0]. isdigit():
            continue
        
        position,name = parts
        if name == player:
            index = i 
            current_pos = int(position)
            break

    #if player not found
    if index == -1:
        print("player not found")
        return 
    
    #move player 
    new_pos = current_pos + steps
    # check if somehting is already there
    for item in data:
        parts = item.split(": ")
        if parts[0].isdigit() and int(parts[0]) == new_pos:
            event = parts[1]
            print(f"{player} landed on {event}!")


    data[index] = f"{new_pos}: {player}"

    print (f"{player} moved from {current_pos} to {new_pos}")

    switchTurn(data)
    # Students will modify this


def main():
    filename = "events.txt"   # Students can rename if needed

    gameData = loadGameData(filename)

    print(gameData)

    while True:
        displayGame(gameData)

    # Example interaction
        choice = input("\nMove player? (y/n): ").lower()
        if choice == "y":
            movePlayer(gameData)
            saveGameData(filename, gameData)
        else:
            print("Goodbye!")
            break



if __name__ == "__main__":
    main()