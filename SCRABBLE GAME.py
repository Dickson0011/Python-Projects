import random

# Initialize the Scrabble board
scrabble_board = [[' ' for _ in range(15)] for _ in range(15)]

# Dictionary of letters and their corresponding point values
letter_values = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1,
    'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1,
    'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}

# Function to display the Scrabble board
def display_board(board):
    for row in board:
        print(" ".join(row))
    print()

# Function to calculate the score of a word
def calculate_score(word):
    score = 0
    for letter in word:
        score += letter_values.get(letter.upper(), 0)
    return score

# Function to place a word on the board
def place_word(board, word, row, col, direction):
    if direction == 'across':
        for letter in word:
            board[row][col] = letter
            col += 1
    elif direction == 'down':
        for letter in word:
            board[row][col] = letter
            row += 1

# Main game loop
while True:
    display_board(scrabble_board)
    
    # Player's turn
    player_word = input("Enter a word to play (or 'quit' to end the game): ").upper()
    
    if player_word == 'QUIT':
        break
    
    row = int(input("Enter the starting row (0-14): "))
    col = int(input("Enter the starting column (0-14): "))
    direction = input("Enter the direction ('across' or 'down'): ").lower()
    
    if direction not in ['across', 'down']:
        print("Invalid direction. Please enter 'across' or 'down'.")
        continue
    
    # Check if the word fits on the board
    if direction == 'across':
        if col + len(player_word) > 15:
            print("Word doesn't fit on the board. Try again.")
            continue
    elif direction == 'down':
        if row + len(player_word) > 15:
            print("Word doesn't fit on the board. Try again.")
            continue
    
    # Check if the word intersects with existing letters on the board
    valid_intersection = True
    for i, letter in enumerate(player_word):
        if direction == 'across':
            if scrabble_board[row][col + i] != ' ' and scrabble_board[row][col + i] != letter:
                valid_intersection = False
                break
        elif direction == 'down':
            if scrabble_board[row + i][col] != ' ' and scrabble_board[row + i][col] != letter:
                valid_intersection = False
                break
    
    if not valid_intersection:
        print("Word doesn't intersect with existing letters. Try again.")
        continue
    
    # Calculate the score and place the word on the board
    score = calculate_score(player_word)
    place_word(scrabble_board, player_word, row, col, direction)
    
    print(f"Score for '{player_word}': {score}")
    input("Press Enter to continue...")

print("Thanks for playing Scrabble!")
