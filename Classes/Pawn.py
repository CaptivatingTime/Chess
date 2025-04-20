from Classes.Piece import Piece

class Pawn(Piece):
    hasMoved = False
    canCapture = False

    name = "Pawn"

    def getName(self):
        return self.name
    
    def setHasMoved(self):
        self.hasMoved = True
    
    def getMoves(self, occupiedSquares):
        self.ValidMoves.clear()
        n = 0
        ValidX = []
        ValidY = []

        ValidX.append(self.getX())
        if self.canCapture:
            ValidX.append(self.getX() + 1)
            ValidX.append(self.getX() - 1) 

        if self.hasMoved:
            ValidY.append(self.getY() + 1)
        else:
            for i in range(2):
                n = n + 1
                ValidY.append(self.getY() + n)
            
        for x in ValidX:
            for y in ValidY:
                if self.checkPath(occupiedSquares, x, y) == False:
                    break
                self.ValidMoves.append((x,y))
                #self.hasMoved = True
        

        return self.ValidMoves
    

    




        

