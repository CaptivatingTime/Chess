from Classes.Piece import Piece

class Queen(Piece):
    name = "Queen"

    def getName(self):
        return self.name
    
    def __getDiagonal(self, occupiedSquares, x, y, dx, dy):
        for i in range(8):
            if i != 0:
                newX = x + i * dx
                newY = y + i * dy
                if self.outOfBoard(newX, newY) or self.checkPath(occupiedSquares, newX, newY) == False:
                    break
                self.ValidMoves.append((newX, newY))

    def getMoves(self, occupiedSquares):
        self.ValidMoves.clear()

        currentX = self.getX()
        currentY = self.getY()

        self.__getDiagonal(occupiedSquares, currentX, currentY,  1,  1)   # Top right
        self.__getDiagonal(occupiedSquares, currentX, currentY,  1, -1)   # Bottom right
        self.__getDiagonal(occupiedSquares, currentX, currentY, -1,  1)   # Top left
        self.__getDiagonal(occupiedSquares, currentX, currentY, -1, -1)   # Bottom left

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
                