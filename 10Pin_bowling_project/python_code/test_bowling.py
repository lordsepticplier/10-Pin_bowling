"""
Unit tests for the Bowling Game

this has normal games, edge cases, invailed, and tests that all the functions 
work as they should
"""

import unittest
from bowling_game import BowlingGame

class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        """Set up a new game before each test."""
        self.game = BowlingGame()

    def same_rolls(self, n, pins):
        """helps roll the same number of pins multiple times."""
        for _ in range(n):
            self.game.roll(pins)

    def test_normal_game(self):
        """Test a normal game."""
        #this has all the rolls in it the space is to seperate the rounds
        rolls = [8,1,   6, 4,   5, 2,   10,   7, 3,   0, 7,   7, 2,    10,   9, 0,   7, 3, 7]

        #this puts all the rolls in the game
        for pins in rolls:
            self.game.roll(pins)

        # Expected score: 122
        self.assertEqual(122, self.game.score())

    def test_all_spares_game(self):
        """Test a game where all rounds are spares."""
        #this has all the rolls in it the space is to seperate the rounds
        rolls = [0, 10,   1, 9,   2, 8,   3,7,   4, 6,   5, 5,   6, 4,    7,3,   8, 2,   9, 1, 10]

        #this puts all the rolls in the game
        for pins in rolls:
            self.game.roll(pins)

        # Expected score: 155
        self.assertEqual(155, self.game.score())
    
    def test_all_strikes_game(self):
        """Test a game where all rounds are a strike."""
        self.same_rolls(12, 10)
        # Expected score: 300
        self.assertEqual(300, self.game.score())

    def test_all_missed_game(self):
        """Test a game where all rounds are a miss."""
        self.same_rolls(20, 0)
        # Expected score: 0 (0 pin × 20 rolls)
        self.assertEqual(0, self.game.score())

    def test_negitive_game(self):
        """Test a game where -1 which isn't possible happens."""
        self.game.roll(-1)
        self.same_rolls(19, 0)
        # Expected score: error or 0 (makes invailed/cheating roll 0)
        self.assertEqual(0, self.game.score())

    def test_bowls_11_game(self):
        """Test a game where 11 which isn't possible happens."""
        self.game.roll(11)
        self.same_rolls(11, 10)
        # Expected score: error or 270 (makes invailed/cheating roll 0)
        self.assertEqual(270, self.game.score())

    def test_more_than_10_game(self):
        """Test a game where more pins are hit then is left."""
        self.game.roll(9)
        self.game.roll(4)
        # Expected score: error or 9 (makes invailed/cheating roll 0)
        self.same_rolls(18, 0)

        self.assertEqual(9, self.game.score())

    def test_bowls_3_times_without_bonus_game(self):
        """Test a game where they bowl 3 times on round 10 even tho they didn't get a bonus."""
        self.same_rolls(18, 0)

        self.game.roll(3)
        self.game.roll(3)
        self.game.roll(3)
        # Expected score: error or 6 (ignores the final roll)
        self.assertEqual(6, self.game.score())

if __name__ == "__main__":
    unittest.main()
