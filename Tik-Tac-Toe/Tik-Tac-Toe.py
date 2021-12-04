
# gloal variable


board = ["-", "-", "-"
        ,"-", "-", "-"
        ,"-", "-", "-"]

game_still_running = True

winner = None

current_player = "X"


def play_game():
    global game_still_running
    global winner
    
    board_display()

    while game_still_running:
        handel_turn(current_player)
        check_if_game_isOver()
        flip_player()
    
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")
   
def board_display():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
    print("\n")
    


def handel_turn(player):

    print(player + "'s turn ")
    position = input("enter number between 1-9: ")
    
    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("invalid input, choose a number between 1-9 ")

        position = int(position)-1
        
        if board[position] == "-":
            valid = True
        else:
            print("you cant go their")

    board[position] = player
    
    board_display()

def check_if_game_isOver():
    check_for_winner()
    check_if_tie()

def check_for_winner():

    global winner

    row_winner = check_row()
    colum_winner = check_colums()
    diog_winner = check_diog()
    if row_winner:
        winner = row_winner
    elif colum_winner:
        winner = colum_winner
    elif diog_winner:
        winner = diog_winner
    else:
        winner = None

def check_row():
    global game_still_running
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_running = False
    
    if row_1:
       return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None

def check_colums():
    global game_still_running
    colum1 = board[0] == board[3] == board[6] != "-"
    colum2 = board[1] == board[4] == board[7] != "-"
    colum3 = board[2] == board[5] == board[8] != "-"
    if colum1 or colum2 or colum3:
        game_still_running = False
    
    if colum1:
       return board[0]
    elif colum2:
        return board[1]
    elif colum3:
        return board[2]
    else:
        return None
        
def check_diog():
    global game_still_running
    diog1 = board[0] == board[4] == board[8] != "-"
    diog2 = board[6] == board[4] == board[2] != "-"
    if diog1 or diog2 :
        game_still_running = False
    
    if diog1:
       return board[0]
    elif diog2:
        return board[6]
    else:
        return None


def check_if_tie():
    global game_still_running

    if "-" not in board:
        print("gone")
        game_still_running = False
        return True
  # Else there is no tie
    else:
        return False
    
def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"

play_game()