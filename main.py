from board import Board
from connectFour import *
from PvsP import * 
from astar import *
from monteCarlo import *

board = Board()

def main():
    play = True
    while play:
        board.resetBoard()
        start_p = askForFirstPlayer()

<<<<<<< HEAD
    if start_p == 'X':
        sec_p = 'O'
    else:
        sec_p = 'X'
=======
        if start_p == 'X':
            sec_p = 'O'
        else:
            sec_p = 'O'
>>>>>>> 1f5e7db5765bbf963c2321cee26de85f182fe59c

        game = askForAlgorithm()
        if game == 1:
            print("Escolhido Player vs Player", end="\n")
            gamePvsP(board, start_p, sec_p)
        if game == 2:
            print("Escolhido A*", end="\n")
            gameAstar(board, start_p)
        if game == 3:
            print("Escolhido MonteCarlo", end="\n")

        play = playAgain()


if __name__ == '__main__':
    main()