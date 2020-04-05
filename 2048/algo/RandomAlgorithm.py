from game import puzzle
import time
import random
import csv
from utils.GameUtils import GameUtils

class RandomAlgorithm:
    def __init__(self):
        self.name = "RandomAlgorithm"
        self.gamegrid = puzzle.GameGrid()

    def execute(self):
        evaluation_list = []
        header_list = ["Move", "Score"]
        evaluation_list.append(header_list)
        moves_count = 0
        for i in range(400):
            self.gamegrid.master.event_generate(GameUtils().get_random_move_name())
            time.sleep(0.001)
            moves_count += 1
            evaluation_row = [moves_count, self.gamegrid.score]
            evaluation_list.append(evaluation_row)
        with open('../evaluations/random_play_scores.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(evaluation_list)
        print("Algorithm: random ==> final Score ==> " + str(self.gamegrid.score))
        self.gamegrid.master.event_generate("<<QUIT>>")
        return self.gamegrid.score