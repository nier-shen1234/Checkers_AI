

# This file describes the time complexity of the checkers AI. Time complexity increases with depth O(b^d)

import time 
import checkers
import arthur
import agent

def benchmark_depths():
    depths_test = [2, 3, 4, 5, 6]

    print("Depth test: Measuring time per move...\n")

    for depth in depths_test:
        B = checkers.CheckerBoard()
        cpu = agent.CheckersAgent(lambda board: arthur.move_function(board, depth))

        start_time = time.time()
        move = cpu.make_move(B)
        end_time = time.time()

        elapsed_time = end_time - start_time
        print(f"Depth {depth}: Time taken for move: {elapsed_time:.6f} seconds")

if __name__ == "__main__":
    benchmark_depths()

