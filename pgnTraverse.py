import chess
import chess.pgn

class PgnTraverse:
    # Class-level variables to store variations and FEN strings
    variations = []
    fenArray = []

    def setup(self, variations):
        """
        Initializes the PgnTraverse object with a list of variations and sets up the chess board.
        
        Args:
            variations (list): A list of variations to traverse.
        """
        self.variations = variations
        self.board = chess.Board()  # Initialize a new chess board

    def generateFenArray(self):
        """
        Generates an array of FEN strings by traversing the variations.
        
        Returns:
            list: A list of FEN strings representing the board states.
        """
        # Start traversing variations from the root
        self.traverseVariations(self.variations, self.variations.move, self.board)
        return self.fenArray

    def traverseVariations(self, variations, mainMove, board):
        """
        Recursively traverses the variations and generates FEN strings for each board state.
        
        Args:
            variations (list): A list of child variations to traverse.
            mainMove (chess.Move): The main move to apply to the board.
            board (chess.Board): The current state of the chess board.
        """
        try:
            # Apply the main move to the board
            board.push(mainMove)
            print(board)  # Print the board state for debugging
            # Append the current board's FEN string to the FEN array
            self.fenArray.append(board.fen())
        except Exception as e:
            # Handle any errors that occur during move application
            print('ERROR:', e)

        # Recursively traverse each child variation
        for childVariation in variations:
            print("-----------------------------------")  # Debug separator
            # Create a new board based on the current board's FEN
            varBoard = chess.Board(board.fen())
            # Recursively traverse the child variation
            self.traverseVariations(childVariation, childVariation.move, varBoard)