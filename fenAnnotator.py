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
    

    def annotateVariations(self, variations, mainMove, board):
        try:
            fen_before = board.fen()
            score_before = self.getScore(board.fen())
            score_val_before = score_before.get('score').white().cp
            v = score_before.get('pv')
            eventual_variation = board.variation_san(v[:6])

            # Limit the variation to 10 halfmoves
            truncated_variation = v[:10]

            board.push(mainMove)
            score_after = self.getScore(board.fen())
            score_val_after = score_after.get('score').white().cp

            line_to_add = False
            if abs(score_val_after - score_val_before) > 50:
                variations.comment = (
                    variations.comment
                    + ' -### '
                    + str(score_val_after)
                    + ' # from '
                    + str(score_val_before)
                    + ' with '
                    + eventual_variation
                    + ' # ###- '
                )
                line_to_add = True
            if len(variations.variations) == 0:
                variations.comment = variations.comment + '|||' + str(score_val_after) + '|||'
            print(board)
        except:
            print('ERROR')
        for childVaratiation in variations:
            print("-----------------------------------")
            varBoard = chess.Board(board.fen())
            self.annotateVariations(childVaratiation, childVaratiation.move, varBoard)

        if  line_to_add:
            # Ensure variations is a chess.pgn.GameNode
            if isinstance(variations, chess.pgn.GameNode):
                # Convert the truncated variation string into a list of chess.Move objects
                move_list = []
                for move_san in v[:6]:
                    try:
                        move_list.append(move_san)
                    except ValueError:
                        print(f"Invalid move in variation: {move_san}")
                        break

                # Add the move list as a variation
                if move_list:
                    variations.parent.add_line(move_list)
                    print("Added line: ", move_list)
            else:
                print("ERROR: 'variations' is not a chess.pgn.GameNode")