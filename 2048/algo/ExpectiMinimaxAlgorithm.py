import csv
import time

from game import logic
from game import puzzle
import math
import itertools


class ExpectiMinimaxAlgorithm:
    def __init__(self):
        self.name = "ExpectiMinimaxAlgorithm"
        self.MERGE_FUNCTIONS = {
            '<<LEFT>>': logic.left,
            '<<RIGHT>>': logic.right,
            '<<UP>>': logic.up,
            '<<DOWN>>': logic.down,
        }

    def execute(self):
        start_time = time.time()
        moves_count = 0
        board = puzzle.GameGrid(expectiminmax=True)
        evaluation_list = []
        header_list = ["Move", "Score"]
        evaluation_list.append(header_list)
        while moves_count < 400:
            # Find all moves with the fitness
            # List of Tuples: moves_list = [(move, finess_value), ...]
            moves_list = self.get_moves(board.matrix)
            # Choose the best move with max fitness
            max_fitness = -float("inf")
            move_location = 0
            for index, move in enumerate(moves_list):
                if move[1] >= max_fitness:
                    max_fitness = move[1]
                    move_location = index
            move = moves_list[move_location][0]
            # Play given move and Checks if we can add more tiles: if not then game over
            if not board.play_move(move):
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
                    "--- Total Execution Time Expectiminimax in minutes: %s ---" % ((time.time() - start_time) / 60.0))
                with open('../../evaluations/expectiminmax_scores.csv', 'w', newline='') as file:
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
            result = move, self.expectiminmax_search(tempBoard, 4)
            results.append(result)
        return results

    def evaluation(self, board):

        if not self.move_exists(board):
            return -float("inf")

        flattened_board = []
        for i, col in enumerate(zip(*board)):
            flattened_board.extend(reversed(col) if i % 2 == 0 else col)

        m = max(flattened_board)
        return sum(x / 10 ** n for n, x in enumerate(flattened_board)) - math.pow(
            (board[3][0] != m) * abs(board[3][0] - m), 2)

    def expectiminmax_search(self, board, depth, move=False):

        if depth == 0 or (move and not self.move_exists(board)):
            return self.evaluation(board)

        alpha = self.evaluation(board)
        if move:
            for _, action in self.MERGE_FUNCTIONS.items():
                child, _, _, _, _ = action(board)
                alpha = max(alpha, self.expectiminmax_search(child, depth - 1))
        else:
            alpha = 0
            zeros = [(i, j) for i, j in itertools.product(range(4), range(4)) if board[i][j] == 0]
            for i, j in zeros:
                c1 = [[x for x in row] for row in board]
                c2 = [[x for x in row] for row in board]
                c1[i][j] = 2
                c2[i][j] = 4
                alpha += (0.9 * self.expectiminmax_search(c1, depth - 1, True) / len(
                    zeros) + 0.1 * self.expectiminmax_search(c2, depth - 1, True) / len(zeros))
        return alpha

    def move_exists(self, board):
        for row in board:
            for x, y in zip(row[:-1], row[1:]):
                if x == y or x == 0 or y == 0:
                    return True
        return False
