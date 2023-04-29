def print_board(board):
    print(f"{board[0]}   |  {board[1]}   | {board[2]}")
    print("------------------")
    print(f"{board[3]}   |  {board[4]}   | {board[5]}")
    print("------------------")
    print(f"{board[6]}   |  {board[7]}   | {board[8]}")
    

def is_winner(board,player):
        if (board[0] == player and board[1] == player and board[2] == player) or \
        (board[3] == player and board[4] == player and board[5] == player) or \
        (board[6] == player and board[7] == player and board[8] == player) or \
        (board[0] == player and board[3] == player and board[6] == player) or \
        (board[1] == player and board[4] == player and board[7] == player) or \
        (board[2] == player and board[5] == player and board[8] == player) or \
        (board[0] == player and board[4] == player and board[8] == player) or \
        (board[2] == player and board[4] == player and board[6] == player):
            return True
        else:
            return False


def tie(board):
    for i in board:
        if i == " ":
            return False
    return True


def playgame():
    board = [" "]*9
    player = ["X","O"]
    current_player = player[0]

    while True:
        print_board(board)
        position = input(f"Player {current_player} enter the Position  ")
        position = int(position)-1

        if board[position]!= " ":
            print("Position Occupied")
            continue

        board[position]=current_player

        if is_winner(board,current_player):
            print_board(board)
            print(f"{current_player} wins")
            break

        if tie(board):
            print_board(board)
            print("It is a Tie")
            break

        if current_player == player[0]:
            current_player=player[1]
        else:
            current_player=player[0]  


        


playgame()