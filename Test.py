import unittest
import pygame
import time
from Snakegame import load_high_score, save_high_score, show_score

class SnakeGameTestCase(unittest.TestCase):
    def test_load_high_score(self):
        # Test when the high_score.txt file exists
        # Modify the high_score.txt file manually to simulate different scenarios
        high_score = load_high_score()
        self.assertIsNotNone(high_score)
        print("Loaded High Score:", high_score)

    def test_save_high_score(self):
        # Test saving a new high score
        new_high_score = 200
        save_high_score(new_high_score)
        high_score = load_high_score()
        self.assertEqual(high_score, new_high_score)
        print("Saved High Score:", new_high_score)



if __name__ == '__main__':
    unittest.main()
