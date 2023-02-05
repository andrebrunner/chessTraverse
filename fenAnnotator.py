import chess
import chess.pgn


class FENAnnotator:
  
    variations = []
    evaluatedPositions = []


    def setup(self, variations, evaluatedPositions):
        self.variations = variations
        self.board = chess.Board()
        self.evaluatedPositions = evaluatedPositions

    def annotate(self):
        self.annotateVariations(self.variations, self.variations.move, self.board)
       

    def getScore(self, fen):
        return self.evaluatedPositions[fen]

    def annotateVariations(self, variations, mainMove, board) :
        try:
            score_before = self.getScore(board.fen())
            board.push(mainMove) 
            score_after = self.getScore(board.fen())
            mainMove.comment = mainMove.comment + ' -### ' +str(score_after) +' vs. ' + str(score_before)  +' ###- '
            print(board)
            self.fenArray.append(board.fen())
        except:
            print('ERROR')
        for childVaratiation in variations:
            print("-----------------------------------")
            varBoard = chess.Board(board.fen())
            self.annotateVariations(childVaratiation, childVaratiation.move,  varBoard) 