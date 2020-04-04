import csv
import time

from expectiminmax import get_moves

from game import puzzle


def expectiminimax_algo():
    start_time = time.time()
    moves_count = 0
    board = puzzle.GameGrid(expectiminmax=True)
    evaluation_list = []
    header_list = ["Move", "Score"]
    evaluation_list.append(header_list)
    while moves_count < 400:
        # Find all moves with the fitness
        # List of Tuples: moves_list = [(move, finess_value), ...]
        moves_list = get_moves(board.matrix)
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
            print("--- Total Execution Time Expectiminimax in minutes: %s ---" % ((time.time() - start_time) / 60.0))
            with open('../evaluations/expectiminmax_scores.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(evaluation_list)
            break
        moves_count += 1
        evaluation_row = [moves_count, board.score]
        evaluation_list.append(evaluation_row)
    board.master.event_generate("<<QUIT>>")
    return board.score
