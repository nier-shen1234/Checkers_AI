import checkers
import agent
import arthur
import arthur_modified
import random_agent

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
        max_moves = 100

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
            print(f"--- Game {i+1} reached move limit! Evaluating piece count... ---\n")

            if hasattr(board, 'get_board'):
                flat_board = board.get_board()
                p1_pieces = sum(1 for p in flat_board if p == 1 or p == 'r')
                p2_pieces = sum(1 for p in flat_board if p == 'b' or p == 2)
            else:
                # Absolute fallback if attribute structure differs
                p1_pieces, p2_pieces = 12, 12

            print(f"[{p1_name}] Pieces: {p1_pieces} | [{p2_name}] Pieces: {p2_pieces}")
            
            if p1_pieces > p2_pieces:
                print(f"[{p1_name}] is winning by piece count!")
                if i % 2 == 0:
                    p1_wins += 1
                else:
                    p2_wins += 1
            elif p2_pieces > p1_pieces:
                print(f"[{p2_name}] is winning by piece count!")
                if i % 2 == 0:
                    p2_wins += 1
                else:
                    p1_wins += 1
            else:
                print(f"Both players are tied in piece count!")
                ties += 1
        else:
            if hasattr(board, 'winner'):
                winner = board.winner()
            elif hasattr(board, 'get_winner'):
                winner = board.get_winner()
            else:
                winner = None

            print(f"--- Game {i+1} finished! Winner: {winner} ---\n")
            if winner == 1:
                p1_wins += 1
            elif winner == 2 or winner == -1:
                p2_wins += 1
            else:
                ties += 1

    print("\n=== TOURNAMENT RESULTS ===")
    print(f"Standard Arthur Wins: {p1_wins}")
    print(f"Modified Arthur Wins: {p2_wins}")
    print(f"Ties: {ties}")

if __name__ == "__main__":
    run_tournament(num_games=3)