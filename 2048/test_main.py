from unittest import TestCase
import main

class Test(TestCase):
    def test_random_algo(self):
        main.random_algo()

    def test_greedy_algo(self):
        main.greedy_algo()

    def test_mcts_algo(self):
        main.mcts_algo()