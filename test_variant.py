from checkers import CheckerBoard

# Initialize the board with your custom setup
board = CheckerBoard()

# Print out the raw jump and move data to verify your extended logic
print("--- TESTING JUMPS ---")
print("All Jumps:", [bin(j) for j in board.get_jumps()])

print("--- TESTING MOVES ---")
print("All Moves:", [bin(m) for m in board.get_moves()])