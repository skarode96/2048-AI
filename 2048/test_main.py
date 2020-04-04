from unittest import TestCase
import main

class Test(TestCase):
    def test_random_algo(self):
        main.random_algo()

    def test_greedy_algo(self):
        main.greedy_algo()

    def test_greedy_algo_with_empty_cell_heuristics(self):
        main.greedy_algo_with_empty_cell_heuristics()

    def test_mcts_algo(self):
        main.mcts_algo()

    # def test_expectiminmax_algo(self):
    #     main.expectiminimax_algo()