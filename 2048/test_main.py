from unittest import TestCase
import unittest
import csv
from algo.RandomAlgorithm import RandomAlgorithm
from algo.GreedyAlgorithm import GreedyAlgorithm
from algo.MCTSAlgorithm import MCTSAlgorithm
from algo.ExpectimaxAlgorithm import ExpectimaxAlgorithm

class Test(TestCase):

    def test_random_algo(self):
        random_algorithm_instance = RandomAlgorithm()
        random_algorithm_instance.execute()

    def test_greedy_algo_basic(self):
        greedy_algorithm_instance = GreedyAlgorithm()
        greedy_algorithm_instance.execute_with_basic_heuristic()

    def test_greedy_algo_with_empty_cell_heuristics(self):
        greedy_algorithm_instance = GreedyAlgorithm(alpha=0.0, beta=1, gamma=0, k=1)
        greedy_algorithm_instance.execute_with_empty_cell_heuristic()

    def test_greedy_algo_with_weighted_cell_heuristics(self):
        greedy_algorithm_instance = GreedyAlgorithm(alpha=0, beta=0, gamma=1, k=1)
        greedy_algorithm_instance.execute_with_weighted_cell_heuristic()

    def test_mcts_algo_basic(self):
        mcts_algorithm_instance = MCTSAlgorithm()
        mcts_algorithm_instance.execute_with_basic_heuristic()

    def test_mcts_algo_with_empty_cell_heuristics(self):
        mcts_algorithm_instance = MCTSAlgorithm(alpha=0.0, beta=1, gamma=0, k=1)
        mcts_algorithm_instance.execute_with_empty_cell_heuristic()

    def test_mcts_algo_with_weighted_cell_heuristics(self):
        mcts_algorithm_instance = MCTSAlgorithm(alpha=0, beta=0, gamma=1, k=1)
        mcts_algorithm_instance.execute_with_weighted_cell_heuristic()

    @unittest.skip
    def test_generate_eval_score_random_for_100_runs(self):
        header_list = ["Run Id", "Score"]
        evaluation_list = [header_list]
        for i in range(100):
            random_algorithm_instance = RandomAlgorithm()
            score = random_algorithm_instance.execute()
            evaluation_row = [i, score]
            evaluation_list.append(evaluation_row)

        with open('../evaluations/avg_run_evaluation/100_run_scores_random_algo.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(evaluation_list)
    @unittest.skip
    def test_generate_eval_score_greedy_basic_for_100_runs(self):
        header_list = ["Run Id", "Score"]
        evaluation_list = [header_list]
        for i in range(100):
            greedy_algorithm_instance = GreedyAlgorithm()
            score = greedy_algorithm_instance.execute_with_basic_heuristic()
            evaluation_row = [i, score]
            evaluation_list.append(evaluation_row)

        with open('../evaluations/avg_run_evaluation/100_run_scores_greedy_algo_basic.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(evaluation_list)
    @unittest.skip
    def test_generate_eval_score_greedy_basic_empty_cell_for_100_runs(self):
        header_list = ["Run Id", "Score"]
        evaluation_list = [header_list]
        for i in range(100):
            greedy_algorithm_instance = GreedyAlgorithm(alpha=0.0, beta=1, gamma=0, k=1)
            score = greedy_algorithm_instance.execute_with_empty_cell_heuristic()
            evaluation_row = [i, score]
            evaluation_list.append(evaluation_row)

        with open('../evaluations/avg_run_evaluation/100_run_scores_greedy_algo_empty_cell_heuristics.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(evaluation_list)

    @unittest.skip
    def test_generate_eval_score_greedy_weighted_cell_for_100_runs(self):
        header_list = ["Run Id", "Score"]
        evaluation_list = [header_list]
        for i in range(100):
            greedy_algorithm_instance = GreedyAlgorithm(alpha=0, beta=0, gamma=1, k=1)
            score = greedy_algorithm_instance.execute_with_weighted_cell_heuristic()
            evaluation_row = [i, score]
            evaluation_list.append(evaluation_row)

        with open('../evaluations/avg_run_evaluation/100_run_scores_greedy_algo_weighted_cell_heuristics.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(evaluation_list)

    @unittest.skip
    def test_generate_eval_score_mcts_basic_for_100_runs(self):
        header_list = ["Run Id", "Score"]
        evaluation_list = [header_list]
        for i in range(100):
            mcts_algorithm_instance = MCTSAlgorithm()
            score = mcts_algorithm_instance.execute_with_basic_heuristic()
            evaluation_row = [i, score]
            evaluation_list.append(evaluation_row)

        with open('../evaluations/avg_run_evaluation/100_run_scores_mcts_algo_basic.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(evaluation_list)

    @unittest.skip
    def test_generate_eval_score_mcts_empty_cell_for_100_runs(self):
        header_list = ["Run Id", "Score"]
        evaluation_list = [header_list]
        for i in range(100):
            mcts_algorithm_instance = MCTSAlgorithm(alpha=0.0, beta=1, gamma=0, k=1)
            score = mcts_algorithm_instance.execute_with_empty_cell_heuristic()
            evaluation_row = [i, score]
            evaluation_list.append(evaluation_row)

        with open('../evaluations/avg_run_evaluation/100_run_scores_mcts_algo_empty_cell_heuristics.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(evaluation_list)

    @unittest.skip
    def test_generate_eval_score_mcts_weighted_cell_for_100_runs(self):
        header_list = ["Run Id", "Score"]
        evaluation_list = [header_list]
        for i in range(100):
            mcts_algorithm_instance = MCTSAlgorithm(alpha=0, beta=0, gamma=1, k=1)
            score = mcts_algorithm_instance.execute_with_weighted_cell_heuristic()
            evaluation_row = [i, score]
            evaluation_list.append(evaluation_row)

        with open('../evaluations/avg_run_evaluation/100_run_scores_mcts_algo_weighted_cell_heuristics.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(evaluation_list)


    @unittest.skip
    def test_expectimax(self):
        """
        # Test for 1000 runs
        header_list = ["Run Id", "Score"]
        evaluation_list = [header_list]
        for i in range(100):
            expecti_max_algorithm_instance = ExpectimaxAlgorithm()
            score = expecti_max_algorithm_instance.execute()
            evaluation_row = [i, score]
            evaluation_list.append(evaluation_row)

        with open('../evaluations/avg_run_evaluation/100_run_scores_expectimax_algo_with_snake_line_heuristics_and_depth_2.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(evaluation_list)
        """
        expecti_max_algorithm_instance = ExpectimaxAlgorithm()
        expecti_max_algorithm_instance.execute()
