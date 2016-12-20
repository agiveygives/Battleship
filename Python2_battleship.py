from random import randint

turns = 30

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

#picks a random row
def random_row(board):
    return randint(0, len(board) - 1)

#picks a random column
def random_col(board):
    return randint(0, len(board[0]) - 1)

#randomly decides if a ship is placed vertically
def vertical():
    return randint(0, 1)

#checks if the ship is vertical
#if it is it returns 0
#if not it returns 1
def horizontal(vertical):
    if vertical == 0:
        return 1
    else:
        return 0

#creates a ship dictionary of passed string name and int size
#the ship is then placed on the board		
def create_ship(name, size):
    # creates and places a ship
    # returns dictionary ship
    # ship creation
    we_good = False
    ship = {
		"place_tries": 0,
        "name": name,
        "hits": size,
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
		ship["place_tries"] += 1
		ship["nose_row"] = random_row(board)
		ship["nose_col"] = random_col(board)
		ship["port_row"] = ship["nose_row"] + ((size - 1) * ship["vertical"])
		ship["port_col"] = ship["nose_col"] + ((size - 1) * horizontal(ship["vertical"]))

		if ship["port_row"] not in range(10):
			ship["port_row"] = ship["nose_row"] - (size - 1)
		if ship["port_col"] not in range(10):
			ship["port_col"] = ship["nose_col"] - (size - 1)

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
			for x in range(size):
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
				ship["range_row"] = []
				ship["range_col"] = []
				break
			else:
				we_good = True
        #end of while loop
    for i in range(size):
        used.append([ship["range_row"][i], ship["range_col"][i]])
    return ship

#checks if the guess was a hit on the ship
#passes the row guess, column guess, and the ship checking
def check_hit(guess_row, guess_col, ship):
	if board[guess_row][guess_col] == "O":
		if guess_row in ship["range_row"] and guess_col in ship["range_col"] and ship["hits"] == 1:
			ship["hits"] -= 1
			board[guess_row][guess_col] = "H"
			print "Congratulations! You sunk my %s!" % ship["name"]
			return True
		elif guess_row in ship["range_row"] and guess_col in ship["range_col"] and ship["hits"] > 1:
			ship["hits"] -= 1
			board[guess_row][guess_col] = "H"
			print "You hit my %s!" % ship["name"]
			return True
		else:
			return False
	else:
		return False
    
# ship creation
destroyer = create_ship("Destroyer", 2)
#print "On try %s, %s was placed on row(s) %s and column(s) %s" % (destroyer["place_tries"], destroyer["name"], destroyer["range_row"], destroyer["range_col"])
crusier = create_ship("Cruiser", 3)
#print "On try %s, %s was placed on row(s) %s and column(s) %s" % (crusier["place_tries"], crusier["name"], crusier["range_row"], crusier["range_col"])
sub = create_ship("Submarine", 3)
#print "On try %s, %s was placed on row(s) %s and column(s) %s" % (sub["place_tries"], sub["name"], sub["range_row"], sub["range_col"])
battleship = create_ship("Battleship", 4)
#print "On try %s, %s was placed on row(s) %s and column(s) %s" % (battleship["place_tries"], battleship["name"], battleship["range_row"], battleship["range_col"])
carrier = create_ship("Carrier", 5)
#print "On try %s, %s was placed on row(s) %s and column(s) %s" % (carrier["place_tries"], carrier["name"], carrier["range_row"], carrier["range_col"])

#the Guessing Game
for turn in range(turns):
	print "Turn: ", turn + 1						#prints the turn the player is on
	guess_row = int(raw_input("Guess Row:"))		#gets input of the row for the guess
 	guess_col = int(raw_input("Guess Col:"))		#gets input of the column for the guess
    
	if check_hit(guess_row, guess_col, destroyer):
		#checks if the guess was a hit on the destroyer and reprints the board if it's a hit
		print_board(board)
	elif check_hit(guess_row, guess_col, crusier):
		#if the guess was not a hit on the destroyer it checks the crusier and reprints the board if it's a hit
		print_board(board)
	elif check_hit(guess_row, guess_col, sub):
		#if the guess was not a hit on the crusier it checks the submarine and reprints the board if it's a hit
		print_board(board)
	elif check_hit(guess_row, guess_col, battleship):
		#if the guess was not a hit on the submarine ut checks the battleship and reprints the board if it's a hit
		print_board(board)
	elif check_hit(guess_row, guess_col, carrier):
		#if the guess was not a hit on the battleship it checks the carrier and reprints the board if it's a hit
		print_board(board)
	else:
		#if the guess wasn't a hit on any of the ships it checks if the guess missed the board, was already used, or if it was just a miss
		if (guess_row < 0 or guess_row > 9) or (guess_col < 0 or guess_col > 9):
			#prints if the guess wasn't on the board and lets the player re-do the turn
			turn -= 1
			print "Oops, that's not even in the ocean."
		elif board[guess_row][guess_col] != "O":
			#prints if the guess was already used and lets the player re-do the turn
			turn -= 1
			print "You guessed that one already."
		else:
			#prints if the guess was a miss
			print "You missed!"
			board[guess_row][guess_col] = "M"
		#reprints the board
		print_board(board)
		
	print
	if battleship["hits"] == 0 and carrier["hits"] == 0 and sub["hits"] == 0 and destroyer["hits"] == 0 and cruiser["hits"] == 0:
		print "Woah, you won."
		break
		
	if turn == turns - 1:
		#if the last turn has been completed without a victory print this
		print "Game Over"
