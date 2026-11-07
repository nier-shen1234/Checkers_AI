from __future__ import print_function
from builtins import str
from builtins import range
import checkers
import agent
import arthur
import random_agent

BLACK, WHITE = 0, 1

arthur_wins = 0
random_agent_wins = 0

print("Starting AI Tournament: Arthur vs Random Agent")

for i in range(10):
    B = checkers.CheckerBoard()
    cpu_1 = agent.CheckersAgent(lambda board: arthur.move_function(board, 4))
    cpu_2 = agent.CheckersAgent(random_agent.move_function)

    current_player = B.active
    turn = 1

    while not B.is_over():
        B.make_move(cpu_1.make_move(B))
        if B.active == current_player:
            continue
        current_player = B.active
        turn += 1
        while not B.is_over() and B.active == current_player:
            B.make_move(cpu_2.make_move(B))
        current_player = B.active

    if B.active == WHITE:
        random_agent_wins += 1
        print(f"Game {i + 1}: Random Agent wins in {turn}, turns")
    else:
        arthur_wins += 1
        print(f"Game {i + 1}: Arthur wins in {turn}, turns")

print(f"\nTournament Results:\nArthur wins: {arthur_wins}\nRandom Agent wins: {random_agent_wins}")