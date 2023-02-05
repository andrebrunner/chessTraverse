import chess
import chess.pgn
import chess.engine
import concurrent.futures

class FenEvaluator:

    evaluatedPositions = dict()
    
    def setup(self, enginePath, engineDepth):
        self.enginePath = enginePath
        self.engineDepth = engineDepth

    def evalBoard(self, board):
        engine = chess.engine.SimpleEngine.popen_uci(self.enginePath)
        info = engine.analyse(board, chess.engine.Limit(depth=self.engineDepth))
        engine.quit()
        self.evaluatedPositions[board.fen()] = info 
        return info
    
    def generateEvalFenList(self, fenList):
        boardlist = []
        for fen in fenList:
            board = chess.Board(fen)
            #self.evaluatedPositions[fen] = self.evalBoard(board)
            boardlist.append(board)

        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            executor.map(self.evalBoard, boardlist)

        return self.evaluatedPositions
