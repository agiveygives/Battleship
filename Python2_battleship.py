from random import randint

board = []

for x in range(10):
    board.append(["O"] * 10)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

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

battleship = {
    "hits": 0,
    "vertical": vertical(),
    "nose_row": random_row(board),
    "nose_col": random_col(board),
    "port_row": 0,
    "port_col": 0,
    "range_row": [],
    "range_col": []
}

battleship["port_row"] = battleship["nose_row"] + (3 * battleship["vertical"])
battleship["port_col"] = battleship["nose_col"] + (3 * horizontal(battleship["vertical"]))

if battleship["port_row"] not in range(10):
    battleship["port_row"] = battleship["nose_row"] - 3
if battleship["port_col"] not in range(10):
    battleship["port_col"] = battleship["nose_col"] - 3

if battleship["nose_row"] == battleship["port_row"]:
    for x in range(4):
        battleship["range_row"].append(battleship["nose_row"])
else:
    if battleship["nose_row"] < battleship["port_row"]:
        for x in range(battleship["nose_row"], battleship["port_row"] + 1):
            battleship["range_row"].append(x)
    else:
        for x in range(battleship["port_row"], battleship["nose_row"] + 1):
            battleship["range_row"].append(x)
    
if battleship["nose_col"] == battleship["port_col"]:
    for x in range(4):
        battleship["range_col"].append(battleship["nose_col"])
else:
    if battleship["nose_col"] < battleship["port_col"]:
        for x in range(battleship["nose_col"], battleship["port_col"] + 1):
            battleship["range_col"].append(x)
    else:
        for x in range(battleship["port_col"], battleship["nose_col"] + 1):
            battleship["range_col"].append(x)
    
for turn in range(10):
    print battleship["range_row"]
    print battleship["range_col"]
    print "Turn: ", turn + 1
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    
    if guess_row in battleship["range_row"] and guess_col in battleship["range_col"] and battleship["hits"] == 3 and board[guess_row][guess_col] != "H":
        print "Congratulations! You sunk my battleship!"
        break
    elif guess_row in battleship["range_row"] and guess_col in battleship["range_col"] and battleship["hits"] < 3 and board[guess_row][guess_col] != "H":
        battleship["hits"] += 1
        board[guess_row][guess_col] = "H"
        print "You hit my battleship!"
        print_board(board)
    else:
        if (guess_row < 0 or guess_row > 9) or (guess_col < 0 or guess_col > 9):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "H" or board[guess_row][guess_col] == "M"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "M"
        if turn == 10:
            print "Game Over"
        print_board(board)