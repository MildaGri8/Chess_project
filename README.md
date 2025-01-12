# Chess program
The first practical graded task will require you to implement a Python program which will answer a simple question – given a board state that the user enters, with 1 white figure and up to 16 black figures, which black figures can the white figure take?

# Explanation

White piece input function.

Black pieces input function

Checking knight's moves function

Checking queen's moves function

Providing results back to user in visual format using Tabulate library

# Usage

Run the program

Enter name of white piece out of available two: "knight" or "queen" and coordinate on the board, e.g.: "b2"

Enter coordinates of black pieces in the same format, e.g.: "b5". It has to be at least 1 black piece, but not more than 16. When finished, enter "done" for program to continue.

Get results in chess board format. Letter "W" followed with name indicates white piece's possition on the board and it's type.

Letter "b" indicates black pieces possition on the board.

Letters "b - out" indicates black pieces which would be captured by white piece.

# Potential improvements
Formating of board to have same width for all columns and height for rows

Adding functionality to have type for black pieces as well, in case program should execute more chess game steps
