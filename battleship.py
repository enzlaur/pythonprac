from random import randint

board = []
ship_row = 0
ship_col = 0


def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

def initiate_board():
    # Create 5x5 board
    for x in range(5):
        board.append(["O"] * 5)
    # Place the ship in a random location
    ship_row = random_row(board)
    ship_col = random_col(board)
    #print ship_row
    #print ship_col

def guess_game(ship_row, ship_col, max_turns):
    for turn in range(max_turns):
        turn = 0
        print "Turn", turn + 1
        guess_row = int(raw_input("Guess Row:"))
        guess_col = int(raw_input("Guess Col:"))

        if guess_row == ship_row and guess_col == ship_col:
            print "Congratulations! You sunk my battleship!"
            board[guess_row][guess_col] = "S"
            print_board(board)
            break
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print "Oops, that's not even in the ocean."
            elif(board[guess_row][guess_col] == "X"):
                print "You guessed that one already."
            else:
                print "You missed my battleship!"
                board[guess_row][guess_col] = "X"
            if turn == (max_turns - 1):
                print "Game Over!!!"
            # Print (turn + 1) here!
        print_board(board)
        turn += 1


def playGame():
    max_turns = int(raw_input("How many turns?: "))
    initiate_board()
    guess_game(ship_row, ship_col, max_turns)


playGame()
