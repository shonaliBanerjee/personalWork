empty = "   None  "
board = [[empty for i in range(8)] for j in range(8)]
pieces = [
    "Black Rook", "Black Knight", "Black Bishop", "Black King", "Black Queen",
    "Black Pawn", "White Rook", "White Knight", "White Bishop", "White King",
    "White Queen", "White Pawn", "   None  "
]
turnCount = 0
colourTurn = "White"

board[7][0] = "Black Rook"
board[7][1] = "Black Knight"
board[7][2] = "Black Bishop"
board[7][3] = "Black Queen"
board[7][4] = "Black King"
board[7][5] = "Black Bishop"
board[7][6] = "Black Knight"
board[7][7] = "Black Rook"

board[0][0] = "White Rook"
board[0][1] = "White Knight"
board[0][2] = "White Bishop"
board[0][3] = "White Queen"
board[0][4] = "White King"
board[0][5] = "White Bishop"
board[0][6] = "White Knight"
board[0][7] = "White Rook"

for i in range(8):
    board[1][i] = "White Pawn"

for i in range(8):
    board[6][i] = 'Black Pawn'

board.reverse()
for i in range(len(board)):
    print(board[i], sep="\n")

while True:
    try:
        pieceAdd = input("\nWhat piece would you like to move: ")
        piecePosition = list(
            input("What notation is this piece currently at: "))
        pieceRow = int(piecePosition[1])
        pieceColumn = str(piecePosition[0])
        movePosition = list(input("What notation should this piece be at: "))
        rowAdd = int(movePosition[1])
        columnAdd = str(movePosition[0])

    except Exception:
        print("You have entered invalid input. Try again.")
        continue

    if pieceColumn not in "abcdefgh" or columnAdd not in "abcdefgh":
        print("You have entered invalid input. Try again.")
        continue

    if colourTurn not in pieceAdd.title():
        print("It is not your turn.")
        continue

    if pieceColumn == "a":
        pieceColumn = int(1)
    elif pieceColumn == "b":
        pieceColumn = int(2)
    elif pieceColumn == "c":
        pieceColumn = int(3)
    elif pieceColumn == "d":
        pieceColumn = int(4)
    elif pieceColumn == "e":
        pieceColumn = int(5)
    elif pieceColumn == "f":
        pieceColumn = int(6)
    elif pieceColumn == "g":
        pieceColumn = int(7)
    elif pieceColumn == "h":
        pieceColumn = int(8)

    if columnAdd == "a":
        columnAdd = int(1)
    elif columnAdd == "b":
        columnAdd = int(2)
    elif columnAdd == "c":
        columnAdd = int(3)
    elif columnAdd == "d":
        columnAdd = int(4)
    elif columnAdd == "e":
        columnAdd = int(5)
    elif columnAdd == "f":
        columnAdd = int(6)
    elif columnAdd == "g":
        columnAdd = int(7)
    elif columnAdd == "h":
        columnAdd = int(8)

    if pieceRow == rowAdd and pieceColumn == columnAdd:
        print("\nPieces must move. Try another move.")
        continue

    if "Pawn" in pieceAdd:
        if "White" in pieceAdd:
            if rowAdd < pieceRow:
                print("\nPawns cannot move backward. Try another move.")
                continue

        elif "Black" in pieceAdd:
            if rowAdd > pieceRow:
                print("\nPawns cannot move backward. Try another move.")
                continue

        if rowAdd - pieceRow == 2:
            if "White" in pieceAdd:
                if pieceRow != 2:
                    print(
                        "\nPawns cannot generally move two spaces. Try another move."
                    )
                    continue
            elif "Black" in pieceAdd:
                if pieceRow != 7:
                    print(
                        "\nPawns cannot generally move two spaces. Try another move."
                    )
                    continue

    if "Rook" in pieceAdd:
        if (columnAdd != pieceColumn) & (rowAdd != pieceRow):
            print(
                "\nRooks must move in straight, non-diagonal lines. Try another move."
            )
            continue

    if "Knight" in pieceAdd:
        if not (
            (columnAdd - pieceColumn == 2 or columnAdd - pieceColumn == -2) and
            (rowAdd - pieceRow == 1 or rowAdd - pieceRow == -1)) and not (
                (columnAdd - pieceColumn == 1 or columnAdd - pieceColumn == -1)
                and (rowAdd - pieceRow == 2 or rowAdd - pieceRow == -2)):
            print(
                "\nKnights must move two squares in one direction and one square in another direction. Try another move."
            )
            continue

    if "Bishop" in pieceAdd:
        if (columnAdd - pieceColumn) == 0:
            print("\nBishops must move diagonally. Try another move.")
            continue
        elif (rowAdd - pieceRow) / (columnAdd - pieceColumn) != 1 and (
                rowAdd - pieceRow) / (columnAdd - pieceColumn) != -1:
            print("\nBishops must move diagonally. Try another move.")
            continue

    if "Queen" in pieceAdd:
        if not ((columnAdd != pieceColumn) &
                (rowAdd == pieceRow)) and not ((columnAdd == pieceColumn) &
                                               (rowAdd != pieceRow)):
            if not ((rowAdd - pieceRow) /
                    (columnAdd - pieceColumn) == 1) and not (
                        (rowAdd - pieceRow) / (columnAdd - pieceColumn) == -1):
                print(
                    "The queen may move diagonally or straight, but not like a knight. Try another move."
                )
                continue

    if "King" in pieceAdd:
        if (columnAdd - pieceColumn > 1) or (rowAdd - pieceRow > 1):
            print(
                "\nThe king may only move one space at a time, in any direction. Try another move."
            )
            continue

    pieceAdd = pieceAdd.title()
    pieceRow = 9 - pieceRow - 1
    pieceColumn -= 1
    rowAdd = 9 - rowAdd - 1
    columnAdd -= 1

    pieceMove = board[pieceRow][pieceColumn]

    if pieceAdd not in pieces:
        print("That is not a valid piece. Try another move.\n")
        continue
    elif pieceMove != pieceAdd:
        print("That piece is not in that position. Try another move.\n")
        continue

    pieceOccupy = board[rowAdd][columnAdd]
    if "Black" in pieceOccupy:
        if "Black" not in pieceMove:
            print("\nWhite has taken", pieceOccupy, "with", pieceMove, ".")
        elif "Black" in pieceMove:
            print(
                "Pieces cannot share a space with others of the same colour. Try another move.\n"
            )
            continue
    elif "White" in pieceOccupy:
        if "White" not in pieceMove:
            print("\nBlack has taken", pieceOccupy, "with", pieceMove, ".")
        elif "White" in pieceMove:
            print(
                "Pieces cannot share a space with others of the same colour. Try another move.\n"
            )
            continue

    board[rowAdd][columnAdd] = pieceMove
    board[pieceRow][pieceColumn] = "   None  "

    print()
    for i in range(len(board)):
        print(board[i], sep="\n")

    turnCount += 1
    if colourTurn == "White":
        colourTurn = "Black"
    elif colourTurn == "Black":
        colourTurn = "White"
