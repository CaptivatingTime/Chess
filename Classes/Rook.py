from Classes.Piece import Piece

class Rook(Piece):

    def getMoves(self):
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
        




