import csv
import time

from game import logic
from game import puzzle
import math
import itertools


class ExpectimaxAlgorithm:
    def __init__(self):
        self.name = "ExpectimaxAlgorithm"
        self.MERGE_FUNCTIONS = {
            '<<LEFT>>': logic.left,
            '<<RIGHT>>': logic.right,
            '<<UP>>': logic.up,
            '<<DOWN>>': logic.down,
        }

    def execute(self):
        start_time = time.time()
        moves_count = 0
        board = puzzle.GameGrid(expectimax=True)
        evaluation_list = []
        header_list = ["Move", "Score"]
        evaluation_list.append(header_list)
        while True:
            # Find all moves with the fitness
            # List of Tuples: moves_with_fitness_dict = [(move, finess_value), ...]
            moves_with_fitness_dict = self.get_moves(board.matrix)
            # Choose the best move with max fitness
            max_fitness = -float("inf")
            move_location = 0
            for index, move in enumerate(moves_with_fitness_dict):
                if move[1] >= max_fitness:
                    max_fitness = move[1]
                    move_location = index
            move = moves_with_fitness_dict[move_location][0]
            # Play given move and Checks if we can add more tiles: if not then game over
            print(board.matrix)
            if not board.play_move(move, self.MERGE_FUNCTIONS):
                print("Game Over")
                max_tile = -float("inf")
                for row in board.matrix:
                    if max(row) >= max_tile:
                        max_tile = max(row)
                    print(*row, sep=' | ')
                print("Total Number of moves: ", moves_count)
                print("Highest Tile is ", max_tile)
                board.update_grid_cells()
                print(
                    "--- Total Execution Time Expectimax in minutes: %s ---" % ((time.time() - start_time) / 60.0))
                with open('../evaluations/expectimax_scores_depth_4.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(evaluation_list)
                break
            moves_count += 1
            evaluation_row = [moves_count, board.score]
            evaluation_list.append(evaluation_row)
        board.master.event_generate("<<QUIT>>")
        return board.score

    def get_moves(self, board):
        results = []
        for move, action in self.MERGE_FUNCTIONS.items():
            tempBoard, _, _, _, _ = action(board)
            result = move, self.expectimax_search(tempBoard, 4)
            results.append(result)
        return results

    def evaluation(self, board):

        if not self.move_exists(board):
            return -float("inf")

        flattened_board = []
        for i, col in enumerate(zip(*board)):
            flattened_board.extend(reversed(col) if i % 2 == 0 else col)

        m = max(flattened_board)
        # Added penalty if the max tile from the board is not at the lowest left corner i.e board[3][0] of the board,
        # Here if the above condition is True (Since, True can also be represented as value 1 in python) then we add
        # the penalty
        penalty = math.pow((board[3][0] != m) * abs(board[3][0] - m), 2)
        weighted_sequence = [x / 10 ** n for n, x in enumerate(flattened_board)]
        return sum(weighted_sequence) - penalty

    def expectimax_search(self, board, depth, move=False):

        if depth == 0 or (move and not self.move_exists(board)):
            return self.evaluation(board)

        fitness = self.evaluation(board)
        if move:
            for _, action in self.MERGE_FUNCTIONS.items():
                child, _, _, _, _ = action(board)
                fitness = max(fitness, self.expectimax_search(child, depth - 1))
        else:
            fitness = 0
            # Find all possible position of tile insertion: ie. tiles which have 0 in it.
            # And for each (i,j)th location of zero tile make create two child
            # c1_expected_2: board with 90% chances of getting 2
            # c2_expected_4: board with 10% chances of getting 4
            empty_positions = [(i, j) for i, j in itertools.product(range(4), range(4)) if board[i][j] == 0]
            for i, j in empty_positions:
                child1_expected_2 = [[x for x in row] for row in board]
                child2_expected_4 = [[x for x in row] for row in board]
                child1_expected_2[i][j] = 2
                child2_expected_4[i][j] = 4
                fitness += (0.9 * self.expectimax_search(child1_expected_2, depth - 1, True) / len(empty_positions)
                        + 0.1 * self.expectimax_search(child2_expected_4, depth - 1, True) / len(empty_positions))
        return fitness

    def move_exists(self, board):
        for row in board:
            for x, y in zip(row[:-1], row[1:]):
                if x == y or x == 0 or y == 0:
                    return True
        return False
