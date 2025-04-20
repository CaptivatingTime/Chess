from Classes.Piece import Piece

class Rook(Piece):
    name = "Rook"

    def getName(self):
        return self.name



    def getMoves(self, occupiedSquares):
        self.ValidMoves.clear()
        currentX = self.getX()
        currentY = self.getY()

        pathX_free = True
        pathY_free = True
        
        for i in range(8):
            if pathX_free:
                if i != currentX:
                    newX = i
                    if self.checkPath(occupiedSquares, newX, currentY):
                        self.ValidMoves.append((newX, currentY))
                    else:
                        pathX_free = False
            if pathY_free:         
                if i != currentY:
                    newY = i
                    if self.checkPath(occupiedSquares, currentX, newY):
                        self.ValidMoves.append((currentX, newY))
                    else:
                        pathY_free = False
        
        return self.ValidMoves
        




