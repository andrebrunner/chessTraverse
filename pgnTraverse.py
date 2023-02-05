import chess
import chess.pgn


class PgnTraverse:
  
    variations = []
    fenArray = []


    def setup(self, variations):
        self.variations = variations
        self.board = chess.Board()

    def generateFenArray(self):
        self.traverseVariations(self.variations, self.variations.move, self.board)
        return self.fenArray


    def traverseVariations(self, variations, mainMove, board) :
        try:
            board.push(mainMove) 
            print(board)
            self.fenArray.append(board.fen())
        except:
            print('ERROR')
        for childVaratiation in variations:
            print("-----------------------------------")
            varBoard = chess.Board(board.fen())
            self.traverseVariations(childVaratiation, childVaratiation.move,  varBoard) 