from utilities import generate_piece, print_board
import random

DEV_MODE = False


def main(game_board: [[int, ], ]) -> [[int, ], ]:
    
    piece = generate_piece(game_board)
    game_board[piece['row']][piece['column']] = piece['value']
    
    piece = generate_piece(game_board)
    game_board[piece['row']][piece['column']] = piece['value']
    
    game_over(game_board)
    print_board(game_board)
    print()
        
    user_input = str(input())
    valid_inputs = ['w','a','s','d','q']
    
    
    while user_input:
        while user_input not in valid_inputs:
            print("Not a valid input...")
            user_input = str(input())
            
        win = False  
            
        if user_input == 'q':
            print("Goodbye")
            break
        
        elif user_input == 'a':
            for row in game_board:
                row_save = []
                for item in row:
                    if item != 0:
                        row_save.append(item)
                
                i = 0
                while i < len(row_save) - 1:
                    if row_save[i] == row_save[i + 1]:
                        row_save[i] += row_save[i + 1]
                        row_save.pop(i + 1) 
                    i +=1
                    
                for i in range(4):  
                    if i < len(row_save):
                        row[i] = row_save[i]
                    else:
                        row[i] = 0
            
            piece = generate_piece(game_board)
            game_board[piece['row']][piece['column']] = piece['value']
            
            print_board(game_board)
            print()

            
        elif user_input == 'd':
            for row in game_board:
                row.reverse()
                row_save = []
                for item in row:
                    if item != 0:
                        row_save.append(item)
                
                i = 0
                while i < len(row_save) - 1:
                    if row_save[i] == row_save[i + 1]:
                        row_save[i] += row_save[i + 1]
                        row_save.pop(i + 1) 
                    i +=1
                    
                for i in range(4):  
                    if i < len(row_save):
                        row[i] = row_save[i]
                    else:
                        row[i] = 0
                row.reverse()
            piece = generate_piece(game_board)
            game_board[piece['row']][piece['column']] = piece['value']
            
            print_board(game_board)
            print()
        
        else:
            print_board(game_board)
            print()
        for row in game_board:
            for col in row:
                if col == 2048:
                    win = True
        if win is True:
            print("You win!")
            break
        user_input = str(input())
  
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
    main([[0, 0, 1024, 1024],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]])
   