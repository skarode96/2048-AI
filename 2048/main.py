import puzzle
import logic
import random
import time

actions_name = ["<<UP>>", "<<DOWN>>", "<<LEFT>>", "<<RIGHT>>"]
moves = [logic.up, logic.down, logic.left, logic.right]

action_dict = {
    0: "<<UP>>",
    1: "<<DOWN>>",
    2: "<<LEFT>>",
    3: "<<RIGHT>>"
}


def get_random_move():
    random_move_index = random.randint(0, 3)
    return action_dict[random_move_index]


gamegrid = puzzle.GameGrid()


def random_algo():
    for i in range(100):
        gamegrid.master.event_generate(get_random_move())
        time.sleep(0.01)
    print( "Algorithm: random ==> final Score ==> " +  str(gamegrid.score))


def greedy_algo():
    for i in range(100):
        scores = []
        for move in moves:
            new_game_state, done, score_for_current_move = move(gamegrid.matrix)
            scores.append(score_for_current_move)
        max_score = max(scores)
        max_score_action_index = scores.index(max_score)
        if sum(scores) == 0:  # if all the moves are leading to 0 then choose random move to move things ahead
            max_score_action_index = random.randint(0, 3)
        gamegrid.master.event_generate(action_dict[max_score_action_index])
        time.sleep(0.01)
    print("Algorithm: greedy ==> final Score ==> " + str(gamegrid.score))

# random_algo()
# greedy_algo()
# gamegrid.mainloop()
