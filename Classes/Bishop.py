from Classes.Piece import Piece

class Bishop(Piece):
    name = "Bishop"

    def getName(self):
        return self.name 

    def getMoves(self, occupiedSquares):
        self.ValidMoves.clear()
        n = 0

        ValidX_range1 = 7 - self.getX()

        path_free = True

        for i in range (ValidX_range1):
            n = n + 1
            newX = self.getX() + n
            newY = self.getY() + n
            if self.outOfBoard(newX, newY) or self.checkPath(occupiedSquares, newX, newY) == False:
                break
            self.ValidMoves.append((newX, newY))
        n = 0
        for i in range (self.getX()):
            n = n + 1
            newX = self.getX() - n
            newY = self.getY() + n
            if self.outOfBoard(newX, newY) or self.checkPath(occupiedSquares, newX, newY) == False:
                break            
            self.ValidMoves.append((newX, newY))

        if self.getY() != 0:
         n = 0
         for i in range (self.getY()):
            n = n + 1
            newX = self.getX() - n
            newY = self.getY() - n
            if self.outOfBoard(newX, newY) or self.checkPath(occupiedSquares, newX, newY) == False:
                break
            self.ValidMoves.append((newX, newY))
        n = 0
        for i in range (self.getY()):
            n = n + 1
            newX = self.getX() + n
            newY = self.getY() - n
            if self.outOfBoard(newX, newY) or self.checkPath(occupiedSquares, newX, newY) == False:
                break
            self.ValidMoves.append((newX, newY))           
            
        return self.ValidMoves