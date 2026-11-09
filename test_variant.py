import checkers 

board = checkers.CheckerBoard()

board.black = 0
board.white = 0
board.kings = 0

board.black |= (1 << 8)   
board.white |= (1 << 13)  

print("--- BOARD STATE FOR CLASS DEMO ---")
print(board)

print("\n--- GENERATED LEGAL JUMPS ---")
jumps = board.get_jumps()
print("Raw jump bit-encodings:", jumps)

print("\n--- AVAILABLE MOVES LIST ---")
for idx, move in enumerate(board.get_moves()):
    print(f"Option {idx}: {move}")