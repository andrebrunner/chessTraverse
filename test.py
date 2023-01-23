import chess
import chess.pgn
import chess.engine

def evalBoard(board):
  engine = chess.engine.SimpleEngine.popen_uci("C:/Stockfish/stockfish_15.1_win_x64_popcnt/stockfish-windows-2022-x86-64-modern.exe")
  info = engine.analyse(board, chess.engine.Limit(time=1.0))
  engine.quit()
  return info["score"]


def traverseVariations(variation, mainMove, board) :
  score = evalBoard(board)
  print("before: ")
  score_before = score.white().cp
  print(score_before)
  board.push(mainMove) 
  print('----------------------------------')
  print(board)
  score = evalBoard(board)
  print("after: ")
  score_after = score.white().cp
  print(score_after)
  if abs(score_after - score_before) > 100:
    print('??????????')
  print('----------------------------------')
  for childVaratiation in variation.variations:
    varBoard = chess.Board(board.fen())
    traverseVariations(childVaratiation, childVaratiation.move,  varBoard)  

    
pgn = open("C:/Users/andre/develop/chessTraverse/x.pgn")

first_game = chess.pgn.read_game(pgn)

board = first_game.board()

traverseVariations(first_game.variations[0], first_game.variations[0].move, board)

#for move in first_game.mainline_moves():
 #   board.push(move)


print(board)
