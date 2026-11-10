"""
    This module implements the game playing harness.
"""
from __future__ import print_function
# Andrew Edwards -- almostimplemented.com
# =======================================
# Harness for running a checkers match.
#
# Last updated: July 21, 2014

from builtins import str
from builtins import input
from builtins import range
import checkers
import agent
import sys
import os

BLACK, WHITE = 0, 1

def main():
    print ("***************************************************")
    print ("*                    Checkers                     *")
    print ("*                                                 *")
    print ("*                 Andrew Edwards                  *")
    print ("*            www.almostimplemented.com            *")
    print ("***************************************************")
    print ("\n")
    print ("\n")

    n = -1
    while not n in [0, 1, 2]:
        n = eval(input("How many human players? (0, 1, 2): "))
        try:
            n = int(n)
        except ValueError:
            print ("Please input 0, 1, or 2.")

    if n == 2:
        B = checkers.CheckerBoard()
        print ("Black moves first.")
        turn = 1
        current_player = B.active
        while not game_over(B):
            os.system('cls' if os.name == 'nt' else 'clear')
            print (B)

            legal_moves = B.get_moves()

            if B.jump:
                print ("Make jump.")
                print ("")
            else:
                print ("Turn %i" % turn)
                print ("")

            for (i, move) in enumerate(get_move_strings(B)):
                print ("Move " + str(i) + ": " + move)

            while True:
                move_idx = eval(input("Enter your move number: "))
                try:
                    move_idx = int(move_idx)
                except ValueError:
                    print ("Please input a valid move number.")
                    continue

                if move_idx in range(len(legal_moves)):
                    break
                else:
                    print ("Please input a valid move number.")
                    continue

            B.make_move(legal_moves[move_idx])

            # If jumps remain, then the board will not update current player
            if B.active == current_player:
                print ("Jumps must be taken.")
                continue
            else:
                current_player = B.active
                turn += 1

        print (B)
        if B.active == WHITE:
            print ("Congrats Black, you win!")
        else:
            print ("Congrats White, you win!")

        return 0


    elif n == 1:
        agent_module = input("Enter name of agent module: ");
        __import__(agent_module)
        agent_module = sys.modules[agent_module]
        cpu = agent.CheckersAgent(agent_module.move_function)
        while True:
            choice = eval(input("Enter 0 to go first and 1 to go second: "))
            try:
                choice = int(choice)
                break
            except ValueError:
                print ("Please input 0 or 1.")
                continue
        turn = 0
        B = checkers.CheckerBoard()
        current_player = B.active
        print ("Black moves first.")
        while not B.is_over():
            os.system('cls' if os.name == 'nt' else 'clear')
            print (B)
            if turn % 2 == choice:
                legal_moves = B.get_moves()
                if B.jump:
                    print ("Make jump.")
                    print ("")
                else:
                    print ("Turn %i" % (turn + 1))
                    print ("")
                for (i, move) in enumerate(get_move_strings(B)):
                    print ("Move " + str(i) + ": " + move)
                while True:
                    move_idx = eval(input("Enter your move number: "))
                    try:
                        move_idx = int(move_idx)
                    except ValueError:
                        print ("Please input a valid move number.")
                        continue
                    if move_idx in range(len(legal_moves)):
                        break
                    else:
                        print ("Please input a valid move number.")
                        continue
                B.make_move(legal_moves[move_idx])
                # If jumps remain, then the board will not update current player
                if B.active == current_player:
                    print ("Jumps must be taken.")
                    continue
                else:
                    current_player = B.active
                    turn += 1
            else:
                B.make_move(cpu.make_move(B))
                if B.active == current_player:
                    print ("Jumps must be taken.")
                    continue
                else:
                    current_player = B.active
                    turn += 1
        print (B)
        if B.active == WHITE:
            print ("Congrats Black, you win!")
        else:
            print ("Congrats White, you win!")
        return 0
    else:
        agent_module = input("Enter name of first agent module: ");
        __import__(agent_module)
        agent_module = sys.modules[agent_module]
        cpu_1 = agent.CheckersAgent(agent_module.move_function)
        agent_module = input("Enter name of second agent module: ");
        __import__(agent_module)
        agent_module = sys.modules[agent_module]
        cpu_2 = agent.CheckersAgent(agent_module.move_function)
        debug = input("Would you like to step through game play? [Y/N]: ")
        debug = 1 if debug.lower()[0] == 'y' else 0
        B = checkers.CheckerBoard()
        current_player = B.active
        if debug:
            print ("sorry not ready")
            return 0
        else:
            while not B.is_over():
                B.make_move(cpu_1.make_move(B))
                if B.active == current_player:
                    continue
                current_player = B.active
                while B.active == current_player and not B.is_over():
                    B.make_move(cpu_2.make_move(B))
                current_player = B.active
            if B.active == WHITE:
                print ("Congrats Black, you win!")
            else:
                print ("Congrats White, you win!")
            return 0



def game_over(board):
    return len(board.get_moves()) == 0

def square_number(bit):
    """Convert a single-bit board value to its square number (1-32)."""
    b = bit.bit_length() - 1
    return 1 + b - b // 9

def get_move_strings(board):
    """Build the move menu directly from board.get_moves(), so the numbers always match the real list (including extended jumps)."""
    labels = []
    for move in board.get_moves():
        move = abs(move)
        origin = move & board.pieces[board.active]
        dest = move ^ origin
        text = "%i to %i" % (square_number(origin), square_number(dest))
        if abs(origin.bit_length() - dest.bit_length()) in (12, 15):
            text += " (extended jump)"
        labels.append(text)
    return labels

if __name__ == '__main__':
    try:
        status = main()
        sys.exit(status)
    except KeyboardInterrupt:
        print ("")
        print ("Game terminated.")
        sys.exit(1)
