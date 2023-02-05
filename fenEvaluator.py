import chess
import chess.pgn
import chess.engine

class FenEvaluator:

    evaluatedPositions = dict()
    
    def setup(self, enginePath, engineDepth):
        self.enginePath = enginePath
        self.engineDepth = engineDepth

    def evalBoard(self, board):
        engine = chess.engine.SimpleEngine.popen_uci(self.enginePath)
        info = engine.analyse(board, chess.engine.Limit(depth=self.engineDepth))
        engine.quit()
        return info
    
    def generateEvalFenList(self, fenList):
        for fen in fenList:
            board = chess.Board(fen)
            self.evaluatedPositions[fen] = self.evalBoard(board)
        return self.evaluatedPositions
