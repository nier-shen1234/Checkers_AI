import checkers
import agent
import arthur
import arthur_modified

def run_tournament(num_games=5):
    # Initialize the agents at Depth 3
    player1 = agent.CheckersAgent(lambda board: arthur.move_function(board, 3))
    player2 = agent.CheckersAgent(lambda board: arthur_modified.move_function(board, 3))

    p1_wins = 0
    p2_wins = 0
    ties = 0

    print(f"Starting Tournament: Standard Arthur vs. Modified Arthur ({num_games} games)...\n")

    for i in range(num_games):
        board = checkers.CheckerBoard()
        
        # Alternate who goes first each game to keep it fair
        if i % 2 == 0:
            current_p1, current_p2 = player1, player2
            p1_name, p2_name = "Standard Arthur", "Modified Arthur"
        else:
            current_p1, current_p2 = player2, player1
            p1_name, p2_name = "Modified Arthur", "Standard Arthur"

        # Game loop with a move limit cap to prevent endless shuffling loops
        move_count = 0
        max_moves = 60

        while not board.is_over() and move_count < max_moves:
            move1 = current_p1.make_move(board)
            if move1 is None:
                break
            board = board.peek_move(move1)
            move_count += 1
            print(f"[{p1_name}] made a move.")
            
            if board.is_over() or move_count >= max_moves:
                break

            move2 = current_p2.make_move(board)
            if move2 is None:
                break
            board = board.peek_move(move2)
            move_count += 1
            print(f"[{p2_name}] made a move.")

        # Tally scores based on outcome or move limit tie
        if move_count >= max_moves:
            print(f"--- Game {i+1} ended in a Tie (Move limit reached)! ---\n")
            ties += 1
        else:
            winner = board.get_winner()
            print(f"--- Game {i+1} finished! Winner: {winner} ---\n")
            if winner == 1:
                p1_wins += 1
            elif winner == 2:
                p2_wins += 1
            else:
                ties += 1

    print("\n=== TOURNAMENT RESULTS ===")
    print(f"Standard Arthur Wins: {p1_wins}")
    print(f"Modified Arthur Wins: {p2_wins}")
    print(f"Ties: {ties}")

if __name__ == "__main__":
    run_tournament(num_games=3)