import chess
import chess.pgn
from fenEvaluator import FenEvaluator

class FENAnnotator:
  
    variations = []
    evaluatedPositions = []


    def setup(self, variations, evaluatedPositions, enginePath, engineDepth):
        self.variations = variations
        self.board = chess.Board()
        self.evaluatedPositions = evaluatedPositions
        self.enginePath = enginePath
        self.engineDepth = engineDepth

    def annotate(self):
        self.annotateVariations(self.variations, self.variations.move, self.board)
       

    def getScore(self, fen):
        if fen in self.evaluatedPositions.keys():
            return self.evaluatedPositions[fen]
        else:
            positionEvaluator =FenEvaluator()
            positionEvaluator.setup(self.enginePath, self.engineDepth)
            tempBoard = chess.Board(fen)
            return positionEvaluator.evalBoard(tempBoard)

    def annotateVariations(self, variations, mainMove, board) :
        try:
            fen_before = board.fen()
            score_before = self.getScore(board.fen())
            score_val_before = score_before.get('score').white().cp
            eventual_variation = board.variation_san(score_before.get('pv')) 
            board.push(mainMove) 
            score_after = self.getScore(board.fen())
            score_val_after = score_after.get('score').white().cp
            if abs(score_val_after - score_val_before) > 50:
                variations.comment = variations.comment + ' -### ' +str(score_val_after) +' # from  ' + str(score_val_before)  +' with ' +eventual_variation+ '# ###- '
            if (len(variations.variations) ==0):
                variations.comment = variations.comment + '|||' + str(score_val_after) + '|||'
            print(board)
        except:
            print('ERROR')
        for childVaratiation in variations:
            print("-----------------------------------")
            varBoard = chess.Board(board.fen())
            self.annotateVariations(childVaratiation, childVaratiation.move,  varBoard) 