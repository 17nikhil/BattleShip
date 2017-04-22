from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!\n"
print "The rules are simple. You\'re playing against me."
print "Just key in the co-ordinates where you want your ship and try to sink my ship by placing your ship wherever you think my ship is."
print "You can\'t see where my ships are because that would make things too easy and we don\'t want that now :P "
print "Here is the empty board. Start placing your ships and don\'t forget to have a blast!"

print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

flag=0

while flag==0:
    ship_row = random_row(board)
    ship_col = random_col(board)
    while board[ship_row][ship_col]=="X":
        ship_row = random_row(board)
        ship_col = random_col(board)
    else:
        size = int(raw_input("type 1 for a small ship or 2 for a big ship"))
        guess_row = int(raw_input("Guess Row:"))
        guess_col = int(raw_input("Guess Col:"))
        z=randint(0,1)
        if guess_row == ship_row and guess_col == ship_col:
            print "Congratulations! You sunk my battleship!"
            flag=1
            if size==2:
                if z==0:
                    if guess_row+1 == ship_row and guess_col == ship_col:
                        print "Congratulations! You sunk my battleship!"
                        flag=1
                elif z==1:
                    if guess_row == ship_row and guess_col+1 == ship_col:
                        print "Congratulations! You sunk my battleship!"
                        flag=1
            break            
        else:
            if (guess_row < 0 or guess_row >len(board)-1) or (guess_col < 0 or guess_col > len(board)-1):
                print "Oops, that's not even in the ocean."
            elif(board[guess_row][guess_col] == "X"):
                print "You guessed that one already."
            else:
                print "You missed my battleship!"
                if size==1:
              	    board[guess_row][guess_col] = "X"
                elif size==2:
                    if(guess_row+1 >len(board)-1) or (guess_col+1 > len(board)-1):
            		    print "Oops, the ship doesn\'t fit in the ocean."
                    else:
                        board[guess_row][guess_col] = "X"
                    
                        if z==0:
                            board[guess_row+1][guess_col] = "X"
                        elif z==1:
                            board[guess_row][guess_col+1] = "X"
            
                print_board(board)