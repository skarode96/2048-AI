import puzzle
import logic
import random
import time

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
    for i in range(100):
        gamegrid.master.event_generate(get_random_move_name())
        time.sleep(0.01)
    gamegrid.master.event_generate("<<QUIT>>")
    print("Algorithm: random ==> final Score ==> " + str(gamegrid.score))


def greedy_algo():
    gamegrid = puzzle.GameGrid()
    for i in range(100):
        scores = []
        for move in moves:
            new_game_state, done, score_for_current_move = move(gamegrid.matrix)
            scores.append(score_for_current_move)
        max_score = max(scores)
        max_score_action_index = scores.index(max_score)
        if sum(scores) == 0:  # if all the moves are leading to 0 then choose random move to move things ahead
            max_score_action_index = random.randint(0, 3)
        gamegrid.master.event_generate(action_name_dict[max_score_action_index])
        time.sleep(0.01)
    gamegrid.master.event_generate("<<QUIT>>")
    print("Algorithm: greedy ==> final Score ==> " + str(gamegrid.score))


def is_all_heuristics_equal(result_scores):
    return sum(result_scores)/4 == result_scores[0]


def mcts_algo():
    gamegrid = puzzle.GameGrid()
    for i in range(100):
        heuristics = list()
        for move in moves:
            heuristic_for_move = monte_carlo_search_score(gamegrid, move)
            heuristics.append(heuristic_for_move)
        if is_all_heuristics_equal(heuristics):
            gamegrid.master.event_generate(get_random_move_name())

        max_heuristic_index = heuristics.index(max(heuristics))
        gamegrid.master.event_generate(action_name_dict[max_heuristic_index])
        time.sleep(0.01)
    gamegrid.master.event_generate("<<QUIT>>")
    print("Algorithm: MCTS ==> final Score ==> " + str(gamegrid.score))


def monte_carlo_search_score(gamegrid, move):
    scores = list()
    new_game_state, done, score_for_current_move = move(gamegrid.matrix)
    scores.append(score_for_current_move)
    for i in range(MCT_SEARCH_DEPTH):
        random_move = get_random_move_function()
        new_game_state, done, score_for_current_move = random_move(new_game_state)
        scores.append(score_for_current_move)

    return sum(scores) / len(scores)
