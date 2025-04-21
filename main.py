from Classes.Player import Player

from Classes.Board import Board


def movePiece(board, player, currentX, currentY, destX, destY):
    selected_piece = player.InitialPieces[currentY][currentX]
    currentX = selected_piece.getX()
    currentY = selected_piece.getY()

    #print(selected_piece.getMoves(player.InitialPieces))
    move = selected_piece.move(destX, destY,player.InitialPieces)
    if move == 1:
        board.UpdatePieces(selected_piece, currentX, currentY)
    if selected_piece.getName() == "Pawn":
        selected_piece.setHasMoved()
    return move    

def registerCapturables(movedPiece, player1, player2):
    ValidMoves = []
    CapturePossible = []
    prevX = None
    prevY = None
    firstReached = False # flag if first piece in diagonal, row or column is seen

    if movedPiece.getColor() == player1.getColor():
        ValidMoves = movedPiece.getMoves(player1.InitialPieces)
        OpponentPieces = player2.getPieces()
        for move in ValidMoves:
            firstReached = False
            for y in range(8):
                for x in range(8):
                    if OpponentPieces[y][x] != None:
                        if prevX != None and prevY != None:
                            offsets = [(1,1), (1, -1), (-1,1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]
                            for offset in offsets:
                                if prevX + offset[0] != x and prevY + offset[1] != y:
                                    firstReached = True
                        if firstReached == False:
                            if move[0] == x and move[1] == y:
                                CapturePossible.append((x, y))
                                prevX = x
                                prevY = y


    movedPiece.setCapturables(CapturePossible)





def main():
    p1 = Player("white")

    for row in range(7, -1, -1):
        full_row = " "
        for column in range(8):
            if p1.InitialPieces[row][column] != None:
                full_row = full_row + " " + p1.InitialPieces[row][column].getName() + f"({p1.InitialPieces[row][column].getColor()})"
            else: full_row = full_row + " " + ("Empty")
        #print(full_row)
        print("\n")

    p2 = Player("black")
    for row in range(8):
        full_row2 = " "
        for column in range(8):
            if p2.InitialPieces[row][column] != None:
                full_row2 = full_row2 + " " + p2.InitialPieces[row][column].getName() + f"({p2.InitialPieces[row][column].getColor()})"
            else: full_row2 = full_row2 + " " + ("Empty")
        #print(full_row2)
        print("\n")

    board = Board(p1, p2)
    board.printBoard()
    #movePiece(board, p1, 0, 1, 2, 2)
    #board.printBoard()
    selected_piece = p1.InitialPieces[0][0]
    print(selected_piece.getCapturables())
    move = movePiece(board, p1, 0, 1, 0, 3)
    move = movePiece(board, p1, 0, 0, 0, 2)
    #move = movePiece(board, p1, 0, 2, 1, 2)
    if move == 1:
        registerCapturables(selected_piece, p1, p2)
    print(selected_piece.getCapturables())
    print(selected_piece.getMoves(p1.InitialPieces))
    #movePiece(board, p1, 5, 1, 5, 2)
    #print(selected_piece.getMoves(p1.InitialPieces))
    #movePiece(board, p1, 2, 0, 6, 4)
    board.printBoard()



if __name__ == '__main__':
    main()