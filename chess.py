from tabulate import tabulate


# Define chess board as matrix. Define x and y axis's values.
board = [[None for _ in range(8)] for _ in range(8)]
X_AXIS = ["a", "b", "c", "d", "e", "f", "g", "h"]
Y_AXIS = ["8", "7", "6", "5", "4", "3", "2", "1"]

# Define possible moves of chess piece - knight.
knight = [
    [-1, -2],
    [-1, 2],
    [1, -2],
    [1, 2],
    [-2, -1],
    [-2, 1],
    [2, -1],
    [2, 1]
]

queen = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1],
    [1, 1],
    [-1, -1],
    [1, -1],
    [-1, 1]
]
    
def main():
    # Function, which asks user's input and returns white piece's name, coordinates in the matrix, and updated board.
    piece, white_x, white_y = add_white(board, X_AXIS, Y_AXIS)

    # Function which asks user's input and returns updated board.
    add_black(board, X_AXIS, Y_AXIS)

    # Check which piece was chosen.
    if piece == "knight":
        # Function that executes knight's moves and returns updated board
        move_knight(board, knight, white_x, white_y)
    else:
        # Function that executes queen's moves and returns updated board
        move_queen(board, queen, white_x, white_y)

    # Print out final status of board.
    print(tabulate(board, showindex=Y_AXIS, headers=X_AXIS, tablefmt = "grid", stralign="center"))


def add_white(board, X_AXIS, Y_AXIS):
    """
    Input white piece. 
    Check user input format, coordinates if fits to the board. 
    Provides error if input is not correct, or confirmation if it was correct

    Parameters:
    Chess board, X and Y axis labels for the board

    Returns:
    Type of white piece what was added
    Coordinates of white piece
    Updates board with white piece placed on it                                         
    """
    print("Let's play! Pick one piece out of knight or queen and place it on the board.")
    while True:
        user_input = input("Example how input should be: knight 'a5'. Your move: ").lower()
        try:
            piece, position = user_input.split()
        except ValueError:
            print("Wrong input format")
        else:
            if piece in ["knight", "queen"] and len(position) == 2:
                try:
                    white_x = X_AXIS.index(position[0])
                    white_y = Y_AXIS.index(position[1])
                except ValueError:
                    print("Out of the board. Letters should be: a-h, numbers:1-8")
                else:
                    print("White", piece, "added succesfully on:", position)
                    board[white_y][white_x] = "W " + piece
                    return piece, white_x, white_y
            else:
                if piece not in ["knight", "queen"]:
                    print("Wrong piece. Chose from knight or queen")
                if len(position) != 2:
                    print("Wrong coordinates!")


def add_black(board, X_AXIS, Y_AXIS):
    """
    Input black piece
    Check user input format, coordinates if fits to the board. 
    Provides error if input is not correct, or confirmation if it was correct
    Checks that there is at least 1, but not more than 16 black pieces added
    Check if piece is not placed on occupied cell

    Parameters:
    Chess board, X and Y axis labels for the board

    Returns:
    Updated board with black pieces placed on it                            
    """
    i = 1
    while i <= 16:
        user_input = input("Add black piece in the format of e.g. 'b2'. When finished with adding - type 'done' ").strip().lower()
        if i == 1 and user_input == "done":
            print("At least one black piece must be added")
        elif user_input == "done":
            return board
        else:
            try:
                black_x = X_AXIS.index(user_input[0])
                black_y = Y_AXIS.index(user_input[1])
            except(ValueError):
                print("Out of the board. Letters should be: a-h, numbers:1-8")
            else:
                if board[black_y][black_x] == None:
                    board[black_y][black_x] = "b"
                    i += 1
                    print("Black piece added successfully on:", user_input)
                else:
                    print("This cell is already occupied")
    else:
        print("16 black pieces already added")
        return board


def move_knight(board, knight, white_x, white_y):
    """
    Check which pieces can be taken out by knight.
    
    Parameters:
    Chess board, matrix of knight's moves, white piece's coordinates

    Returns:
    Updated board with marked blacked pieces which can be taken out   
    """
    for move in knight:
        new_x = white_x + int(move[1])
        new_y = white_y + int(move[0])
        if 0 <= new_x < 8 and 0 <= new_y < 8:
            if board[new_y][new_x] == "b":
                board[new_y][new_x] = "b - out"

    return board


def move_queen(board, queen, white_x, white_y):
    """
    Check which pieces can be taken out by queen.
    
    Parameters:
    Chess board, matrix of queen's, white piece's coordinates

    Returns:
    Updated board with marked blacked pieces which can be taken out   
    """
    for move in queen:
        for i in range (8):
            new_x = white_x + int(i)*int(move[1])
            new_y = white_y + int(i)*int(move[0])
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                if board[new_y][new_x] == "b":
                    board[new_y][new_x] = "b - out"
                    break
    return board


if __name__ == "__main__":
    main()
