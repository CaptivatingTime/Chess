from Classes.Piece import Piece

class King(Piece):

    name = "King"

    def getName(self):
        return self.name

    def getMoves(self, occupiedSquares):
        self.ValidMoves.clear()

        currentX = self.getX()
        currentY = self.getY()

        offsets = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

        for offset in offsets:
            newX = offset[0] + currentX
            newY = offset[1] + currentY
            if self.outOfBoard(newX, newY) == False and self.checkPath(occupiedSquares, newX, newY):
                self.ValidMoves.append((newX, newY))
        
        return self.ValidMoves