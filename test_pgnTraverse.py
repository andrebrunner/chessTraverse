import unittest
import chess
import chess.pgn
import io  # Import io for StringIO
from pgnTraverse import PgnTraverse

class TestPgnTraverse(unittest.TestCase):
    def setUp(self):
        """
        Set up a sample PGN game and initialize the PgnTraverse object.
        """
        # Sample PGN game
        pgn = """
        1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6
        """
        # Wrap the PGN string in a StringIO object
        pgn_file = io.StringIO(pgn)
        # Parse the PGN game
        game = chess.pgn.read_game(pgn_file)
        self.variations = game.variations  # Extract the variations

        # Initialize the PgnTraverse object
        self.pgn_traverse = PgnTraverse()
        self.pgn_traverse.setup(self.variations[0])

    def test_generateFenArray(self):
        """
        Test the generateFenArray method to ensure it generates the correct FEN strings.
        """
        # Generate the FEN array
        fen_array = self.pgn_traverse.generateFenArray()
        print(fen_array)

        # Expected FEN strings for the given PGN game
        expected_fen_array = ['rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1', 
                              'rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2',
                                'rnbqkbnr/pppp1ppp/8/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2', 
                                'r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 2 3',
                                  'r1bqkbnr/pppp1ppp/2n5/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R b KQkq - 3 3',
                                    'r1bqkbnr/1ppp1ppp/p1n5/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 0 4', 
                                    'r1bqkbnr/1ppp1ppp/p1n5/4p3/B3P3/5N2/PPPP1PPP/RNBQK2R b KQkq - 1 4',
                                      'r1bqkb1r/1ppp1ppp/p1n2n2/4p3/B3P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 2 5']

        # Assert that the generated FEN array matches the expected FEN array
        self.assertEqual(sorted(fen_array), sorted(expected_fen_array))


if __name__ == "__main__":
    unittest.main()