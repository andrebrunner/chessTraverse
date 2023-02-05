import chess
import chess.pgn
import chess.engine
import sys
import getopt
from pgnTraverse import PgnTraverse
from fenEvaluator import FenEvaluator
from fenAnnotator import FENAnnotator


#-i
inputFile = "C:/Users/andre/develop/chessTraverse/x.pgn"
#-o
outputFile="zzz.pgn"
#-d
engineDepth=10
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

    
pgn = open(inputFile)

first_game = chess.pgn.read_game(pgn)

board = first_game.board()

positionCache = {
  '' : 0
}

pgnTraverser = PgnTraverse()
pgnTraverser.setup(first_game.variations[0])
fenList = pgnTraverser.generateFenArray()

print( fenList)

positionEvaluator =FenEvaluator()
positionEvaluator.setup(enginePath, engineDepth)
evaluatedFens = positionEvaluator.generateEvalFenList(fenList)

for fen in evaluatedFens:
    board = chess.Board(fen)
    print(board)
    print(evaluatedFens[fen])


fenAnnotator = FENAnnotator()
fenAnnotator.setup(first_game.variations[0], evaluatedFens)
fenAnnotator.annotate()

print(first_game)

print(first_game, file=open(outputFile, "w"), end="\n\n")
