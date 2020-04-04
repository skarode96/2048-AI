import puzzle
import logic
import random
import time
from puzzle import GameGrid
from expectiminmax import get_moves
import csv

MCT_SEARCH_DEPTH = 300

actions_name = ["<<UP>>", "<<DOWN>>", "<<LEFT>>", "<<RIGHT>>"]
moves = [logic.up, logic.down, logic.left, logic.right]

action_name_dict = {
    0: "<<UP>>",
    1: "<<DOWN>>",
    2: "<<LEFT>>",
    3: "<<RIGHT>>"
}

action_func_dict = {
    0: logic.up,
    1: logic.down,
    2: logic.left,
    3: logic.right
}


def get_random_move_name():
    random_move_index = random.randint(0, 3)
    return action_name_dict[random_move_index]


def get_random_move_function():
    random_move_index = random.randint(0, 3)
    return action_func_dict[random_move_index]


def random_algo():
    gamegrid = puzzle.GameGrid()
    evaluation_list = []
    header_list = ["Move", "Score"]
    evaluation_list.append(header_list)
    moves_count = 0
    for i in range(1000):
        gamegrid.master.event_generate(get_random_move_name())
        time.sleep(0.01)
        moves_count += 1
        evaluation_row = [moves_count, gamegrid.score]
        evaluation_list.append(evaluation_row)
    with open('../evaluations/random_scores.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(evaluation_list)
    print("Algorithm: random ==> final Score ==> " + str(gamegrid.score))
    gamegrid.master.event_generate("<<QUIT>>")


def greedy_algo():
    gamegrid = puzzle.GameGrid()
    evaluation_list = []
    header_list = ["Move", "Score"]
    evaluation_list.append(header_list)
    moves_count = 0
    for i in range(1000):
        scores = []
        for move in moves:
            new_game_state, done, score_for_current_move, empty_cells_count = move(gamegrid.matrix)
            scores.append(score_for_current_move)
        max_score = max(scores)
        max_score_action_index = scores.index(max_score)
        if sum(scores) == 0:  # if all the moves are leading to 0 then choose random move to move things ahead
            max_score_action_index = random.randint(0, 3)
        gamegrid.master.event_generate(action_name_dict[max_score_action_index])
        time.sleep(0.01)
        moves_count += 1
        evaluation_row = [moves_count, gamegrid.score]
        evaluation_list.append(evaluation_row)
    with open('../evaluations/greedy_scores.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(evaluation_list)
    print("Algorithm: greedy ==> final Score ==> " + str(gamegrid.score))
    gamegrid.master.event_generate("<<QUIT>>")


def greedy_algo_with_empty_cell_heuristics():
    gamegrid = puzzle.GameGrid()
    evaluation_list = []
    header_list = ["Move", "Score"]
    evaluation_list.append(header_list)
    moves_count = 0
    for i in range(1000):
        scores = []
        for move in moves:
            new_game_state, done, score_for_current_move, empty_cells_count = move(gamegrid.matrix)
            weighted_score = 0.5 * score_for_current_move + 0.5 * empty_cells_count + 1
            scores.append(weighted_score)
        max_score = max(scores)
        max_score_action_index = scores.index(max_score)
        if sum(scores) / scores[
            0] == 4:  # if all the moves are leading to 0 then choose random move to move things ahead
            max_score_action_index = random.randint(0, 3)
        gamegrid.master.event_generate(action_name_dict[max_score_action_index])
        time.sleep(0.01)
        moves_count += 1
        evaluation_row = [moves_count, gamegrid.score]
        evaluation_list.append(evaluation_row)
    with open('../evaluations/greedy_scores_with_heuristics.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(evaluation_list)
    print("Algorithm: greedy with heuristics ==> final Score ==> " + str(gamegrid.score))
    gamegrid.master.event_generate("<<QUIT>>")


def is_all_mcts_heuristics_equal(result_scores):
    return sum(result_scores) / 4 == result_scores[0]


def mcts_algo():
    gamegrid = puzzle.GameGrid()
    evaluation_list = []
    header_list = ["Move", "Score"]
    evaluation_list.append(header_list)
    moves_count = 0
    for i in range(1000):
        heuristics = list()
        for move in moves:
            heuristic_for_move = monte_carlo_search_score(gamegrid, move)
            heuristics.append(heuristic_for_move)
        if is_all_mcts_heuristics_equal(heuristics):
            gamegrid.master.event_generate(get_random_move_name())

        max_heuristic_index = heuristics.index(max(heuristics))
        gamegrid.master.event_generate(action_name_dict[max_heuristic_index])
        time.sleep(0.01)
        moves_count += 1
        evaluation_row = []
        evaluation_row.append(moves_count)
        evaluation_row.append(gamegrid.score)
        evaluation_list.append(evaluation_row)
    gamegrid.master.event_generate("<<QUIT>>")
    with open('../evaluations/mcts_scores.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(evaluation_list)
    print("Algorithm: MCTS ==> final Score ==> " + str(gamegrid.score))


def monte_carlo_search_score(gamegrid, move):
    scores = list()
    new_game_state, done, score_for_current_move, empty_cells_count = move(gamegrid.matrix)
    scores.append(score_for_current_move)
    for i in range(MCT_SEARCH_DEPTH):
        random_move = get_random_move_function()
        new_game_state, done, score_for_current_move, empty_cells_count = random_move(new_game_state)
        scores.append(score_for_current_move)
    return sum(scores) / len(scores)


def expectiminimax_algo():
    start_time = time.time()
    moves_count = 0
    board = GameGrid(expectiminmax=True)
    evaluation_list = []
    header_list = ["Move", "Score"]
    evaluation_list.append(header_list)
    while moves_count < 1000:
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
