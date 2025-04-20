
class Board():
    def __init__(self, player1, player2):
        self.Layout = [[None for j in range(8)] for i in range(8)]

        self.players = [player1,player2]

        self.all_player_pieces = [player1.getPieces(),player2.getPieces()]
        
        for player_pieces in self.all_player_pieces:
            for row in player_pieces:
                for piece in row:
                    if piece != None:
                        pieceX = piece.getX()
                        pieceY = piece.getY()
                        self.Layout[pieceY][pieceX] = piece

        

    def printBoard(self):
        for row in range(7, -1, -1):
            full_row = " "
            for column in range(8):
                if self.Layout[row][column] != None:
                    full_row = full_row + " " + self.Layout[row][column].getName() + f"({self.Layout[row][column].getColor()})"
                else: full_row = full_row + " " + ("Empty")
            print(full_row)
            print("\n")

    def UpdatePieces(self, piece, oldX, oldY):
        self.Layout[oldY][oldX] = None
        newX = piece.getX()
        newY = piece.getY()
        self.Layout[newY][newX] = piece
        
        for player in self.players:
            if player.getColor() == piece.getColor():
                player.InitialPieces[oldY][oldX] = None
                player.InitialPieces[newY][newX] = piece
                




                        
        
                
                    

                

