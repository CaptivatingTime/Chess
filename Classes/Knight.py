from Classes.Piece import Piece

class Knight(Piece):
    name = "Knight"

    def getName(self):
        return self.name
    
    def getMoves(self, occupiedSquares):
        self.ValidMoves.clear()
        currentX = self.getX()
        currentY = self.getY()

        offsets = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                   (2, 1), (2, -1), (-2, 1), (-2, -1)]        
        
        for offset in offsets:
             newX = currentX + offset[0]
             newY = currentY + offset[1]
             if self.outOfBoard(newX, newY) == False:
                 if occupiedSquares[newY][newX] == None:
                    self.ValidMoves.append((newX, newY))                

        return self.ValidMoves                            

