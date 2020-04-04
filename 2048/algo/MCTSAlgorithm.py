import csv
import time
import constants as c
from utils.GameUtils import GameUtils

from game import puzzle


class MCTSAlgorithm:
    def __init__(self):
        self.name = "MCTSAlgorithm"
        self.gamegrid = puzzle.GameGrid()

    def is_all_mcts_heuristics_equal(self, result_scores):
        return sum(result_scores) / 4 == result_scores[0]

    def execute_with_basic_heuristic(self):
        evaluation_list = []
        header_list = ["Move", "Score"]
        evaluation_list.append(header_list)
        moves_count = 0
        for i in range(400):
            heuristics = list()
            for move in GameUtils.moves:
                heuristic_for_move = self.monte_carlo_search_score(move)
                heuristics.append(heuristic_for_move)
            if self.is_all_mcts_heuristics_equal(heuristics):
                self.gamegrid.master.event_generate(GameUtils().get_random_move_name())

            max_heuristic_index = heuristics.index(max(heuristics))
            self.gamegrid.master.event_generate(GameUtils.actions_name_dict[max_heuristic_index])
            time.sleep(0.01)
            moves_count += 1
            evaluation_row = []
            evaluation_row.append(moves_count)
            evaluation_row.append(self.gamegrid.score)
            evaluation_list.append(evaluation_row)
        self.gamegrid.master.event_generate("<<QUIT>>")
        with open('../evaluations/mcts_scores.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(evaluation_list)
        print("Algorithm: MCTS ==> final Score ==> " + str(self.gamegrid.score))
        return self.gamegrid.score

    def monte_carlo_search_score(self, move):
        scores = list()
        new_game_state, done, score_for_current_move, empty_cells_count, weighted_cell_score = move(self.gamegrid.matrix)
        scores.append(score_for_current_move)
        for i in range(c.MCT_SEARCH_DEPTH):
            random_move = GameUtils().get_random_move_function()
            new_game_state, done, score_for_current_move, empty_cells_count, weighted_cell_score = random_move(
                new_game_state)
            scores.append(score_for_current_move)
        return sum(scores) / len(scores)

    def execute_with_empty_cell_heuristic(self):
        evaluation_list = []
        header_list = ["Move", "Score"]
        evaluation_list.append(header_list)
        moves_count = 0
        for i in range(400):
            heuristics = list()
            for move in GameUtils.moves:
                heuristic_for_move = self.monte_carlo_search_score_with_empty_cell_heuristics(move)
                heuristics.append(heuristic_for_move)
            if self.is_all_mcts_heuristics_equal(heuristics):
                self.gamegrid.master.event_generate(GameUtils().get_random_move_name())

            max_heuristic_index = heuristics.index(max(heuristics))
            self.gamegrid.master.event_generate(GameUtils.actions_name_dict[max_heuristic_index])
            time.sleep(0.01)
            moves_count += 1
            evaluation_row = [moves_count, self.gamegrid.score]
            evaluation_list.append(evaluation_row)
        self.gamegrid.master.event_generate("<<QUIT>>")
        with open('../evaluations/mcts_empty_cell_heuristics_scores.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(evaluation_list)
        print("Algorithm: MCTS Empty Cell Heuristics ==> final Score ==> " + str(self.gamegrid.score))
        return self.gamegrid.score

    def monte_carlo_search_score_with_empty_cell_heuristics(self, move):
        scores = list()
        new_game_state, done, score_for_current_move, empty_cells_count, weighted_cell_score = move(
            self.gamegrid.matrix)
        scores.append(score_for_current_move)
        for i in range(c.MCT_SEARCH_DEPTH):
            random_move = GameUtils().get_random_move_function()
            new_game_state, done, score_for_current_move, empty_cells_count, weighted_cell_score = random_move(
                new_game_state)
            new_score = c.Alpha * score_for_current_move + c.Beta * empty_cells_count + c.K
            scores.append(new_score)
        return sum(scores) / len(scores)
