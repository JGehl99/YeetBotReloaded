import numpy as np
import random as rand
from random import seed
from datetime import datetime

class Minesweeper:

    def __init__(self, x=0, y=0):
        seed(datetime.now())
        self.board = np.zeros(shape=(x, y), dtype=int)
        self.x = x
        self.y = y

    def printBoard(self):
        for j in range(self.y):
            for i in range(self.x):
                print(self.board[i][j], end=" ")
            print()

    def fillBoard(self):
        for i in range(1, 25):
            mineX = rand.randint(1, self.x-2)
            mineY = rand.randint(1, self.y-2)
            if self.board[mineX][mineY] != -1:
                self.board[mineX][mineY] = -1
                for y in range(mineY - 1, mineY + 2):
                    for x in range(mineX - 1, mineX + 2):
                        if self.board[x][y] != -1:
                            self.board[x][y] += 1



