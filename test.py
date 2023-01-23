import chess
import chess.pgn
import chess.engine

def evalBoard(board):
  engine = chess.engine.SimpleEngine.popen_uci("C:/Stockfish/stockfish_15.1_win_x64_popcnt/stockfish-windows-2022-x86-64-modern.exe")
  info = engine.analyse(board, chess.engine.Limit(depth=20))
  engine.quit()
  return info["score"]

def evaluteAndPrint(board):
  if board.fen() in positionCache.keys():
    return positionCache[board.fen()]
  score = evalBoard(board)
  print(board)
  score_cp = score.white().cp
  print(score_cp)
  positionCache[board.fen()] = score_cp
  return score_cp
  

def traverseVariations(variation, mainMove, board) :
  print('##################################')
  score_before = evaluteAndPrint(board)
  board.push(mainMove) 
  print('----------------------------------')
  score_after = evaluteAndPrint(board)
  if abs(score_after - score_before) > 100:
    print('??????????')
    print(mainMove.uci())
    print(board.fen())
  print('##################################')
  for childVaratiation in variation.variations:
    varBoard = chess.Board(board.fen())
    traverseVariations(childVaratiation, childVaratiation.move,  varBoard)  

    
pgn = open("C:/Users/andre/develop/chessTraverse/x.pgn")

first_game = chess.pgn.read_game(pgn)

board = first_game.board()

positionCache = {
  '' : 0
}

traverseVariations(first_game.variations[0], first_game.variations[0].move, board)

#for move in first_game.mainline_moves():
 #   board.push(move)


print(board)
