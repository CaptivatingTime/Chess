class Piece:
    def __init__(self, color, x, y):
        self.__color = color
        self.__posX = x
        self.__posY = y
        self.ValidMoves = []

    def checkPath(self, occupiedSquares, x, y): # Checks if path is clear for movement
        if occupiedSquares[y][x] != None:
            return False
        else:
            return True

    def outOfBoard(self, x, y):
        if x > 7 or y > 7 or x < 0 or y < 0:
            return True
        else:
            return False

    def getColor(self):
        return self.__color
    
    def getPosition(self):
        return (self.posX, self.posY)
    
    def getX(self):
        return self.__posX
    
    def getY(self):
        return self.__posY
    
    def getMoves(self): # Piece possible moves go here
        return

    def move(self, destX, destY, occupiedSquares):
        self.ValidMoves.clear()
        self.getMoves(occupiedSquares)
        if (destX, destY) in self.ValidMoves:
            self.__posX = destX
            self.__posY = destY
            print(f"new piece location ({destX},{destY})")
            return 1
        else:
            print("Not valid move")
            return 0

    def canCapture(self):
        return # Piece possible captures go here
    
