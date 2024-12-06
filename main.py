from utilities import generate_piece, print_board
import random
import sys

DEV_MODE = False


def main(game_board: [[int, ], ]) -> [[int, ], ]:
    
    piece = generate_piece(game_board)
    game_board[piece['row']][piece['column']] = piece['value']
    
    piece = generate_piece(game_board)
    game_board[piece['row']][piece['column']] = piece['value']
    
    game_over(game_board)
    print_board(game_board)
        
    user_input = str(input())
    
    if user_input == 'q':
        print("Goodbye")
    else:
        print_board(game_board)
        
    """
    2048 main function, runs a game of 2048 in the console.

    Uses the following keys:
    w - shift up
    a - shift left
    s - shift down
    d - shift right
    q - ends the game and returns control of the console
    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: returns the ending game board
    """
    # Initialize board's first cell
    # TODO: generate a random piece and location using the generate_piece function
    # TODO: place the piece at the specified location
    
    # Game Loop

        # TODO: UPDATE/ADD PIECE TO BOARD
        # place a random piece on the board
        # check to see if the game is over using the game_over function

        # TODO: Show updated board using the print_board function

        # TODO: GET AND EXECUTE USER MOVE
        # Take input until the user's move is a valid key
        # if the user quits the game, print Goodbye and stop the Game Loop
        # User's Move Loop:
            # Execute the user's move
            # Compare board before user's move & after user's move
                # get and execute another move if board has not changed

        # Check if the user wins
    return game_board


def game_over(game_board: [[int, ], ]) -> bool:
      
    result_list = []
    for row in game_board:
        if 0 in row:
            return False
            
    for i in range(4):
        for j in range(4):
            if i < 3 and game_board[i][j] == game_board[i+1][j]:
                return False
            if j < 3 and game_board[i][j] == game_board[i][j+1]:
                return False
        
    """
    Query the provided board's game state.

    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: Boolean indicating if the game is over (True) or not (False)
    """
    # TODO: Loop over the board and determine if the game is over
    return True  # TODO: Don't always return false


if __name__ == "__main__":
    main([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]])
   