from game import puzzle
import time
import random
import csv
from utils.GameUtils import GameUtils
import constants as c

class GreedyAlgorithm:
    def __init__(self):
        self.name = "GreedyAlgorithm"
        self.gamegrid = puzzle.GameGrid()

    def execute_with_basic_heuristic(self):
        evaluation_list = []
        header_list = ["Move", "Score"]
        evaluation_list.append(header_list)
        moves_count = 0
        for i in range(400):
            scores = []
            for move in GameUtils.moves:
                new_game_state, done, score_for_current_move, empty_cells_count, weighted_cell_score = move(self.gamegrid.matrix)
                scores.append(score_for_current_move)
            max_score = max(scores)
            max_score_action_index = scores.index(max_score)
            if sum(scores) == 0:  # if all the moves are leading to 0 then choose random move to move things ahead
                max_score_action_index = random.randint(0, 3)
            self.gamegrid.master.event_generate(GameUtils.actions_name_dict[max_score_action_index])
            time.sleep(0.01)
            moves_count += 1
            evaluation_row = [moves_count, self.gamegrid.score]
            evaluation_list.append(evaluation_row)
        with open('../evaluations/greedy_scores.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(evaluation_list)
        print("Algorithm: greedy ==> final Score ==> " + str(self.gamegrid.score))
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
                weighted_score = c.Alpha * score_for_current_move + c.Beta * empty_cells_count + c.K
                scores.append(weighted_score)
            max_score = max(scores)
            max_score_action_index = scores.index(max_score)
            if sum(scores) / scores[0] == 4:  # if all the moves are same then choose random move to move things ahead
                max_score_action_index = random.randint(0, 3)
            self.gamegrid.master.event_generate(GameUtils.actions_name_dict[max_score_action_index])
            time.sleep(0.01)
            moves_count += 1
            evaluation_row = [moves_count, self.gamegrid.score]
            evaluation_list.append(evaluation_row)
        with open('../evaluations/greedy_scores_with_heuristics.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(evaluation_list)
        print("Algorithm: greedy with heuristics ==> final Score ==> " + str(self.gamegrid.score))
        self.gamegrid.master.event_generate("<<QUIT>>")
        return self.gamegrid.score