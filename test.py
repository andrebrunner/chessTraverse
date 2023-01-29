import chess
import chess.pgn
import chess.engine
import sys
import getopt

#-i
inputFile = "C:/Users/andre/develop/chessTraverse/x.pgn"
#-o
outputFile="zzz.pgn"
#-d
engineDepth=1
#-e
enginePath="C:\Stockfish\stockfish_15.1_win_x64_popcnt\stockfish-windows-2022-x86-64-modern.exe"
# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
# Arguments passed
print("\nName of Python script:", sys.argv[0])

argv = sys.argv[1:]
opts, args = getopt.getopt(argv, 'i:o:d:e:')
for o in opts:
    print(o)      
    if (o[0] == '-i'):
        inputFile = o[1]
    if (o[0] == '-o'):
        outputFile = o[1]
    if (o[0] == '-d'):
        engineDepth = o[1]
    if (o[0] == '-e'):
        enginePath = o[1]

print('Inputfile:' + inputFile)        
print('Outputfile:' + outputFile)        
print('Depth:' + str(engineDepth))        
print('Enginepath:' + enginePath)        

def evalBoard(board):
  engine = chess.engine.SimpleEngine.popen_uci(enginePath)
  info = engine.analyse(board, chess.engine.Limit(depth=engineDepth))
  engine.quit()
  return info

def evaluteAndPrint(board):
  if board.fen() in positionCache.keys():
    return positionCache[board.fen()]
  info = evalBoard(board)
  print(board)
  score_cp = info.get('score').white().cp
  print(score_cp)
  positionCache[board.fen()] = info
  return info
  

def traverseVariations(variation, mainMove, board) :
  print('##################################')
  info_before = evaluteAndPrint(board)
  score_before = info_before.get('score').white().cp
  eventual_Variation = board.variation_san(info_before.get('pv')) 
  board.push(mainMove) 
  print('----------------------------------')
  info_after = evaluteAndPrint(board)
  score_after = info_after.get('score').white().cp
  if abs(score_after - score_before) > 100:
    variation.comment = variation.comment + ' -### ' +str(score_after) +' vs. ' + str(score_before) + eventual_Variation + ' ###-' 
    print('??????????')
    print(mainMove.uci())
    print(board.fen())
  print('##################################')
  if len(variation.variations)==0:
    variation.comment = variation.comment + ' -### ' +str(score_after) +' vs. ' + str(score_before) +' ###-'
  for childVaratiation in variation.variations:
    varBoard = chess.Board(board.fen())
    traverseVariations(childVaratiation, childVaratiation.move,  varBoard)  

    
pgn = open(inputFile)

first_game = chess.pgn.read_game(pgn)

board = first_game.board()

positionCache = {
  '' : 0
}

traverseVariations(first_game.variations[0], first_game.variations[0].move, board)

#for move in first_game.mainline_moves():
 #   board.push(move)


print(board)

print(first_game)

print(first_game, file=open(outputFile, "w"), end="\n\n")
