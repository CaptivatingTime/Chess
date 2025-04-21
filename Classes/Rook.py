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
        
        for i in range(currentX, 8, 1):
            if pathX_free:
                    newX = i
                    if currentX != newX:
                        if self.checkPath(occupiedSquares, newX, currentY):
                            self.ValidMoves.append((newX, currentY))
                        else:
                            pathX_free = False
        pathX_free = True
        for i in range(currentX, -1, -1):
            if pathX_free:
                    newX = i
                    if currentX != newX:
                        if self.checkPath(occupiedSquares, newX, currentY):
                            self.ValidMoves.append((newX, currentY))
                        else:
                            pathX_free = False
                    
        for i in range(currentY, 8, 1):
            if pathY_free:
                    newY = i
                    if currentY != newY:
                        if self.checkPath(occupiedSquares, currentX, newY):
                            self.ValidMoves.append((currentX, newY))
                        else:
                            pathY_free = False
        pathY_free = True
        for i in range(currentY, -1, -1):
            if pathY_free:
                    newY = i
                    if currentY != newY:
                        if self.checkPath(occupiedSquares, currentX, newY):
                            self.ValidMoves.append((currentX, newY))
                        else:
                            pathY_free = False


        
        return self.ValidMoves
        




