from board import Board
from connectFour import *
from PvsP import * 
from astar import *
from monteCarlo import *
from min import *
from connectFour import inputPlayer, askForFirstPlayer, askForAlgorithm, playAgain
from PvsP import gamePvsP
from astar import gameAstar
from min import gameMiniMax
from monteCarlo import gameMonteCarlo as game_monte_carlo



def main():
    play = True
    order = inputPlayer(askForFirstPlayer())
    board = Board(order[0])
    while play:
        board.resetBoard()
        game = askForAlgorithm()
        if game == 1:
            print("Escolhido Player vs Player.", end="\n")
            gamePvsP(board, order)
        if game == 2:
            print("Escolhido A*.", end="\n")
            gameAstar(board, order)
        if game == 3:
            print("Escolhido MonteCarlo", end="\n")
            game_monte_carlo(board, order)
        if game == 4:
            print("Escolhido Minimax", end='\n')
            gameMiniMax(board, order)

        play = playAgain()


if __name__ == '__main__':
    main()