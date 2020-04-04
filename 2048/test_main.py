from unittest import TestCase
import csv
from algo.RandomAlgorithm import RandomAlgorithm
from algo.GreedyAlgorithm import GreedyAlgorithm
from algo.MCTSAlgorithm import MCTSAlgorithm
from algo.ExpectiMinimaxAlgorithm import ExpectiMinimaxAlgorithm


class Test(TestCase):

    def test_random_algo(self):
        random_algorithm_instance = RandomAlgorithm()
        random_algorithm_instance.execute()

    def test_greedy_algo_basic(self):
        greedy_algorithm_instance = GreedyAlgorithm()
        greedy_algorithm_instance.execute_with_basic_heuristic()

    def test_greedy_algo_with_empty_cell_heuristics(self):
        greedy_algorithm_instance = GreedyAlgorithm()
        greedy_algorithm_instance.execute_with_empty_cell_heuristic()

    def test_mcts_algo_basic(self):
        mcts_algorithm_instance = MCTSAlgorithm()
        mcts_algorithm_instance.execute_with_basic_heuristic()

    def test_mcts_algo_with_empty_cell_heuristics(self):
        mcts_algorithm_instance = MCTSAlgorithm()
        mcts_algorithm_instance.execute_with_empty_cell_heuristic()

    def test_generate_eval_score_random_for_100_runs(self):
        header_list = ["Run Id", "Score"]
        evaluation_list = [header_list]
        for i in range(20):
            random_algorithm_instance = RandomAlgorithm()
            score = random_algorithm_instance.execute()
            evaluation_row = [i, score]
            evaluation_list.append(evaluation_row)

        with open('../evaluations/avg_run_evaluation/100_run_scores_random_algo.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(evaluation_list)

    def test_expectiminimax_new(self):
        expecti_minimax_algorithm_instance = ExpectiMinimaxAlgorithm()
        expecti_minimax_algorithm_instance.execute()
