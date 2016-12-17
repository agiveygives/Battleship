from random import randint

board = []
used = []

for x in range(10):
    board.append(["O"] * 10)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def check_use(coordinate):
    #checks if a position is already in use
    #returns true is place is being used, false if it is free
    if coordinate in used:
        return True
    else:
        return False

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)
    
def vertical():
    return randint(0, 1)

def horizontal(vertical):
    if vertical == 0:
        return 1
    else:
        return 0
    
def create_ship(name, size):
    # creates and places a ship
    # returns dictionary ship
    # ship creation
    we_good = False
    ship = {
        "name": name,
        "hits": size - 1,
        "vertical": vertical(),
        "nose_row": 0,
        "nose_col": 0,
        "port_row": 0,
        "port_col": 0,
        "range_row": [],
        "range_col": []
    }

    # ship placement
    while not we_good:
        ship["nose_row"] = random_row(board)
        ship["nose_col"] = random_col(board)
        ship["port_row"] = ship["nose_row"] + ((size - 1) * ship["vertical"])
        ship["port_col"] = ship["nose_col"] + ((size - 1) * horizontal(ship["vertical"]))

        if ship["port_row"] not in range(10):
            ship["port_row"] = ship["nose_row"] - 3
        if ship["port_col"] not in range(10):
            ship["port_col"] = ship["nose_col"] - 3

        if ship["nose_row"] == ship["port_row"]:
            for x in range(size):
                ship["range_row"].append(ship["nose_row"])
        else:
            if ship["nose_row"] < ship["port_row"]:
                for x in range(ship["nose_row"], ship["port_row"] + 1):
                    ship["range_row"].append(x)
            else:
                for x in range(ship["port_row"], ship["nose_row"] + 1):
                    ship["range_row"].append(x)

        if ship["nose_col"] == ship["port_col"]:
            for x in range(4):
                ship["range_col"].append(ship["nose_col"])
        else:
            if ship["nose_col"] < ship["port_col"]:
                for x in range(ship["nose_col"], ship["port_col"] + 1):
                    ship["range_col"].append(x)
            else:
                for x in range(ship["port_col"], ship["nose_col"] + 1):
                    ship["range_col"].append(x)
        for i in range(size):
            if [ship["range_row"][i], ship["range_col"][i]] in used:
                we_good = False
                break
            else:
                we_good = True
        #end of while loop
    for i in range(size):
        used.append([ship["range_row"][i], ship["range_col"][i]])
    return ship

def check_hit(guess_row, guess_col, ship):
    if guess_row in ship["range_row"] and guess_col in ship["range_col"] and ship["hits"] == 0 and board[guess_row][guess_col] != "H":
        print "Congratulations! You sunk my %s!" % ship["name"]
        return True
    elif guess_row in ship["range_row"] and guess_col in ship["range_col"] and ship["hits"] > 0 and board[guess_row][guess_col] != "H":
        ship["hits"] -= 1
        board[guess_row][guess_col] = "H"
        print "You hit my %s!" % ship["name"]
        return True
    else:
        return False
    
# ship creation
battleship = create_ship("Battleship", 4)
carrier = create_ship("Carrier", 5)
sub = create_ship("Submarine", 3)

for turn in range(10):
    print battleship["range_row"]
    print battleship["range_col"]
    print carrier["range_row"]
    print carrier["range_col"]
    print "Turn: ", turn + 1
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    
    if check_hit(guess_row, guess_col, battleship):
    elif check_hit(guess_row, guess_col, carrier):
    elif check_hit(guess_row, guess_col, sub):
    else:
        if (guess_row < 0 or guess_row > 9) or (guess_col < 0 or guess_col > 9):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "H" or board[guess_row][guess_col] == "M"):
            print "You guessed that one already."
        else:
            print "You missed!"
            board[guess_row][guess_col] = "M"
        if turn == 10:
            print "Game Over"
    if battleship["hits"] == 0 and carrier["hits"] == 0 and sub["hits"] == 0:
        print "Woah, you won."
        break
    print_board(board)
