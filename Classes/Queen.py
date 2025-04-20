from Classes.Piece import Piece

class Queen(Piece):
    name = "Queen"

    def getName(self):
        return self.name
    
    def __getDiagonal(self, x, y, dx, dy):
        for i in range(8):
            if i != 0:
                newX = x + i * dx
                newY = y + i * dy
                if self.outOfBoard(newX, newY):
                    break
                self.ValidMoves.append((newX, newY))

    def getMoves(self, occupiedSquares):

        currentX = self.getX()
        currentY = self.getY()

        self.__getDiagonal(currentX, currentY,  1,  1)   # Top right
        self.__getDiagonal(currentX, currentY,  1, -1)   # Bottom right
        self.__getDiagonal(currentX, currentY, -1,  1)   # Top left
        self.__getDiagonal(currentX, currentY, -1, -1)   # Bottom left

        for i in range(8):
            if i != currentX:
                newX = i
                self.ValidMoves.append((newX, currentY))
            if i != currentY:
                newY = i
                self.ValidMoves.append((currentX, newY))
                
        return self.ValidMoves
                