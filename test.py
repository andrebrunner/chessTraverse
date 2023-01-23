import chess
import chess.pgn
#import chess.engine

def evalBoard(board):
    engine = chess.engine.SimpleEngine.popen_uci("C:\Stockfish\stockfish_15.1_win_x64_popcnt\stockfish-windows-2022-x86-64-modern.exe")
    info = engine.analyse(board, chess.engine.Limit(time=0.1))
    engine.quit()
    return info["score"]


def traverseVariations(variation, mainMove, board) :
    score = evalBoard(board)
    print("before: " + score)
    board.push(mainMove) 
    print('----------------------------------')
    score = evalBoard(board)
    print("after: " + score)
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
