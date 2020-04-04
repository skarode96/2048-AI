from unittest import TestCase
import main
import csv

class Test(TestCase):
    def test_random_algo(self):
        main.random_algo()

    def test_greedy_algo(self):
        main.greedy_algo()

    def test_greedy_algo_with_empty_cell_heuristics(self):
        main.greedy_algo_with_empty_cell_heuristics()

    def test_mcts_algo(self):
        main.mcts_algo()

    def test_mcts_algo_with_empty_cell_heuristics(self):
        main.mcts_algo_with_empty_cell_heuristics()

    def test_generate_eval_score_random_for_100_runs(self):
        header_list = ["Run Id", "Score"]
        evaluation_list = [header_list]
        for i in range(20):
            score = main.random_algo()
            evaluation_row = [i, score]
            evaluation_list.append(evaluation_row)

        with open('../evaluations/avg_run_evaluation/100_run_scores_random_algo.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(evaluation_list)




    def test_expectiminmax_algo(self):
        main.expectiminimax_algo()