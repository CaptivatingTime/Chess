from Classes.Piece import Piece

class Rook(Piece):
    name = "Rook"

    def getName(self):
        return self.name


    def getMoves(self, occupiedSquares):
        currentX = self.getX()
        currentY = self.getY()

        for i in range(8):
            if i != currentX:
                newX = i
                self.ValidMoves.append((newX, currentY))
            if i != currentY:
                newY = i
                self.ValidMoves.append((currentX, newY))
        
        return self.ValidMoves
        




