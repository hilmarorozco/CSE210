'''
Tic-Tac-Toe
Week 2: 01/15/2022
Author: Hilmar Orozco

'''

def main():
    print('Welcome to Tic-Tac-Toe!')

    player = next_player("")
    board = create_board()
    while not (has_winner(board) or is_a_draw(board)):
        display_board(board)
        make_move(player, board)
        player = next_player(player)
    display_board(board)
    print("Thanks for playing Tic-Tac-Toe!") 

def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def display_board(board):
    
    print()
    print(f"       |       |    ")
    print(f"   {board[0]}   |   {board[1]}   |   {board[2]}")
    print(f"       |       |    ")
    print('-------+-------+-------')
    print(f"       |       |    ")
    print(f"   {board[3]}   |   {board[4]}   |   {board[5]}")
    print(f"       |       |    ")
    print('-------+-------+-------')
    print(f"       |       |    ")
    print(f"   {board[6]}   |   {board[7]}   |   {board[8]}")
    print(f"       |       |    ")
    print()
    
    
def is_a_draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 


    
def has_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

            

def make_move(player, board):
    #square = int(input(f"{player}'s turn to choose a square (1-9): "))
    #board[square - 1] = player
    try:
        square = int(input(f"{player}'s turn to choose a square (1-9): "))

        if square >9 or square <1 or board[square-1] == "o" or board[square-1] == "x":
            raise ValueError()
        board[square-1] = player
    except ValueError:
        print("Position taken. Choose a valid position.")
        make_move(player,board)
        return


def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

if __name__ == "__main__":
    main()