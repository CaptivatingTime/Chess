from Classes.Piece import Piece

class Pawn(Piece):
    hasMoved = False
    canCapture = False

    def getMoves(self):
        n = 0
        ValidX = []
        ValidY = []

        ValidX.append(self.getX())
        if self.canCapture:
            ValidX.append(self.getX() + 1)
            ValidX.append(self.getX() - 1)

        if self.hasMoved:
            ValidY.append(self.getY() + 1)
        else:
            for i in range(2):
                n = n + 1
                ValidY.append(self.getY() + n)
            self.hasMoved = True
        for x in ValidX:
            for y in ValidY:
                self.ValidMoves.append((x,y))
        

        return self.ValidMoves
    

    




        

