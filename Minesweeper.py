import numpy as np
import random as rand
from random import seed
from datetime import datetime


class Minesweeper:

    seed(datetime.now())

    def __init__(self, x=0, y=0, mines=0):
        self.board = np.zeros(shape=(x, y), dtype=int)
        self.x = x
        self.y = y
        self.mines = mines

        for i in range(0, self.mines):
            # If the generated location already has a mine,
            # reroll the x and y until theres an open spot
            while True:
                mx = rand.randint(0, self.x - 1)
                my = rand.randint(0, self.y - 1)
                if self.board[mx][my] != -1: break

            self.board[mx][my] = -1

            for k in range(my - 1, my + 2):
                for j in range(mx - 1, mx + 2):
                    if j < 0 or k < 0 or j > self.x-1 or k > self.y-1 or self.board[j][k] == -1:
                        continue
                    else:
                        self.board[j][k] += 1

        self.msg = ""
        safe_flag = False
        for j in range(self.y):
            for i in range(self.x):
                if self.board[i][j] == -1:
                    self.msg += "||:boom:||"
                if self.board[i][j] == 0:
                    if not safe_flag:
                        safe_flag = True
                        self.msg += ":zero:"
                    else:
                        self.msg += "||:zero:||"
                if self.board[i][j] == 1:
                    self.msg += "||:one:||"
                if self.board[i][j] == 2:
                    self.msg += "||:two:||"
                if self.board[i][j] == 3:
                    self.msg += "||:three:||"
                if self.board[i][j] == 4:
                    self.msg += "||:four:||"
                if self.board[i][j] == 5:
                    self.msg += "||:five:||"
                if self.board[i][j] == 6:
                    self.msg += "||:six:||"
                if self.board[i][j] == 7:
                    self.msg += "||:seven:||"
                if self.board[i][j] == 8:
                    self.msg += "||:eight:||"
            self.msg += "\n"

    def printBoard(self):
        for j in range(self.y):
            for i in range(self.x):
                print(self.board[i][j], end=" ")
            print()
