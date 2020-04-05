from game import puzzle
import time
import random
import csv
from utils.GameUtils import GameUtils
import numpy as np
from game import constants as c

Alpha = 0.0
Beta = 1
K = 1
class GreedyAlgorithm:

    def __init__(self, alpha=0.0, beta=0.0, gamma=0.0,  k=1):
        self.name = "GreedyAlgorithm"
        self.gamegrid = puzzle.GameGrid()
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.k = k

    def execute_with_basic_heuristic(self):
        evaluation_list = []
        header_list = ["Move", "Score"]
        evaluation_list.append(header_list)
        moves_count = 0
        for i in range(400):
            scores = []
            for move in GameUtils.moves:
                new_game_state, done, score_for_current_move, empty_cells_count, weighted_cell_score = move(self.gamegrid.matrix)
                if new_game_state != self.gamegrid.matrix:
                    scores.append(score_for_current_move)
                else:
                    scores.append(0)

            max_score = max(scores)
            max_score_action_index = scores.index(max_score)
            if sum(scores) == 0:  # if all the moves are leading to 0 then choose random move to move things ahead
                max_score_action_index = random.randint(0, 3)
            self.gamegrid.master.event_generate(GameUtils.actions_name_dict[max_score_action_index])
            time.sleep(0.001)
            moves_count += 1
            evaluation_row = [moves_count, self.gamegrid.score]
            evaluation_list.append(evaluation_row)
        with open('../evaluations/greedy_scores.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(evaluation_list)
        print("Algorithm: greedy basic ==> final Score ==> " + str(self.gamegrid.score))
        self.gamegrid.master.event_generate("<<QUIT>>")
        return self.gamegrid.score

    def execute_with_empty_cell_heuristic(self):
        evaluation_list = []
        header_list = ["Move", "Score"]
        evaluation_list.append(header_list)
        moves_count = 0
        for i in range(400):
            scores = []
            for move in GameUtils.moves:
                new_game_state, done, score_for_current_move, empty_cells_count, weighted_cell_score= move(self.gamegrid.matrix)
                if new_game_state != self.gamegrid.matrix:
                    weighted_score = self.alpha * score_for_current_move + self.beta * empty_cells_count + self.gamma * weighted_cell_score + self.k
                    scores.append(weighted_score)
                else:
                    scores.append(0)
            max_score = max(scores)
            max_score_action_index = scores.index(max_score)
            if sum(scores) == 0:  # if all the moves are same then choose random move to move things ahead
                max_score_action_index = random.randint(0, 3)
            self.gamegrid.master.event_generate(GameUtils.actions_name_dict[max_score_action_index])
            time.sleep(0.001)
            moves_count += 1
            evaluation_row = [moves_count, self.gamegrid.score]
            evaluation_list.append(evaluation_row)
        with open('../evaluations/greedy_scores_with_empty_cell_heuristics.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(evaluation_list)
        print("Algorithm: greedy with empty cell heuristics ==> final Score ==> " + str(self.gamegrid.score))
        self.gamegrid.master.event_generate("<<QUIT>>")
        return self.gamegrid.score

    def execute_with_weighted_cell_heuristic(self):
        evaluation_list = []
        header_list = ["Move", "Score"]
        evaluation_list.append(header_list)
        moves_count = 0
        for i in range(400):
            scores = []
            for move in GameUtils.moves:
                new_game_state, done, score_for_current_move, empty_cells_count, weighted_cell_score= move(self.gamegrid.matrix)
                if new_game_state != self.gamegrid.matrix:
                    weighted_score = self.alpha * score_for_current_move + self.beta * empty_cells_count + self.gamma * weighted_cell_score + self.k
                    scores.append(weighted_score)
                else:
                    scores.append(0)
            # flatten_indexs = np.argwhere(scores == np.amax(scores)).flatten()
            max_score = max(scores)
            max_score_action_index = scores.index(max_score)
            if sum(scores) == 0:  # if all the moves are same then choose random move to move things ahead
                max_score_action_index = random.randint(0, 3)
            self.gamegrid.master.event_generate(GameUtils.actions_name_dict[max_score_action_index])
            time.sleep(0.001)
            moves_count += 1
            evaluation_row = [moves_count, self.gamegrid.score]
            evaluation_list.append(evaluation_row)
        with open('../evaluations/greedy_scores_with_weighted_sum_heuristics.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(evaluation_list)
        print("Algorithm: greedy with empty and weighted sum heuristics ==> final Score ==> " + str(self.gamegrid.score))
        self.gamegrid.master.event_generate("<<QUIT>>")
        return self.gamegrid.score

