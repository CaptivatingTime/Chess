from Classes.Pawn import Pawn
from Classes.Knight import Knight
from Classes.Rook import Rook
from Classes.Bishop import Bishop
from Classes.Queen import Queen
from Classes.King import King


class Player:
    def __init__(self, color):
        
        if color == "white":
            y  = 0
            dy = 1
        elif color == "black":
            y  = 7
            dy = -1

        self.InitialPieces = [[None for j in range(8)] for i in range(8)]

        for i in range (8):
            self.InitialPieces[y + dy][i] = Pawn(color, i, y + dy) # list in list structure coordinates are (y,x)
            
        self.InitialPieces[y][0] =   Rook(color, 0, y)
        self.InitialPieces[y][7] =   Rook(color, 7, y)

        self.InitialPieces[y][1] = Knight(color, 1, y)
        self.InitialPieces[y][6] = Knight(color, 6, y)

        self.InitialPieces[y][2] = Bishop(color, 2, y)
        self.InitialPieces[y][5] = Bishop(color, 5, y)

        self.InitialPieces[y][3] =  Queen(color, 3, y)

        self.InitialPieces[y][4] =   King(color, 4, y)

    def getPieces(self):
        return self.InitialPieces