from Classes.Piece import Piece

class Knight(Piece):
    
    def getMoves(self):
        currentX = self.getX()
        currentY = self.getY()

        offsets = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                   (2, 1), (2, -1), (-2, 1), (-2, -1)]        
        
        for offset in offsets:
             newX = currentX + offset[0]
             newY = currentY + offset[1]
             if self.outOfBoard(newX, newY) == False:
                 self.ValidMoves.append((newX, newY))                

        return self.ValidMoves                            

