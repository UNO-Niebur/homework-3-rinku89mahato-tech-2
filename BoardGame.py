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


def displayGame(data):
    """Displays the current game state."""
    print("\nCurrent Game State:")
    for item in data:
        print(item)


def movePlayer(data):
    """Example function to simulate moving a player."""
    
    player = input("Enteer player name: ")
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
            print(f"{player} landed on {parts[1]}!")

    data[index] = f"{new_pos}: {player}"

    print (f"{player}moved from {current_pos} to {new_pos}")
    # Students will modify this


def main():
    filename = "events.txt"   # Students can rename if needed

    gameData = loadGameData(filename)

    while True:
        displayGame(gameData)

    # Example innteraction
        choice = input("\nMove player? (y/n): ").lower()
        if choice == "y":
            movePlayer(gameData)
        else:
            print("Goodbye!")
            break



if __name__ == "__main__":
    main()