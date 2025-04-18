class Piece:
    def __init__(self, color, x, y):
        self.__color = color
        self.__posX = x
        self.__posY = y
        self.ValidMoves = []

    def outOfBoard(self, x, y):
        if x > 7 or y > 7 or x < 0 or y < 0:
            return True
        else:
            return False

                
    def getPosition(self):
        return (self.posX, self.posY)
    
    def getX(self):
        return self.__posX
    
    def getY(self):
        return self.__posY
    
    def getMoves(self): # Piece possible moves go here
        return

    def move(self, destX, destY):
        self.ValidMoves.clear()
        self.getMoves()
        if (destX, destY) in self.ValidMoves:
            self.posX = destX
            self.posY = destY
            print(f"new piece location ({destX},{destY})")
            return 1
        else:
            print("Not valid move")
            return 0

    def canCapture(self):
        return # Piece possible captures go here