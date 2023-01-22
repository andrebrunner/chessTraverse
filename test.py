import chess
import chess.pgn

def traverseVariations(variation, mainMove, board) :
    board.push(mainMove)
    print('----------------------------------')
    print(board)
    print('----------------------------------')
    for childVaratiation in variation.variations:
      varBoard = chess.Board(board.fen())
      traverseVariations(childVaratiation, childVaratiation.move,  varBoard)  


pgn = open("QIDMaster.pgn")

first_game = chess.pgn.read_game(pgn)

board = first_game.board()

traverseVariations(first_game.variations[0], first_game.variations[0].move, board)

#for move in first_game.mainline_moves():
 #   board.push(move)


print(board)
