import puzzle
import logic
import random
import time

actions_name = ["<<UP>>", "<<DOWN>>", "<<LEFT>>", "<<RIGHT>>"]
actions_func = [logic.up, logic.down, logic.left, logic.right]

gamegrid = puzzle.GameGrid()


def random_algo():
    for i in range(100):
        random_action = random.randint(0, 3)
        gamegrid.master.event_generate(actions_name[random_action])
        time.sleep(0.01)
    print("final Score : " + str(gamegrid.score))


def greedy_algo():
    for i in range(100):
        scores = []
        for action in actions_func:
            game, done, local_score = action(gamegrid.matrix)
            scores.append(local_score)
        max_score = max(scores)
        index = scores.index(max_score)
        if sum(scores) == 0:
            index = random.randint(0, 3)
        gamegrid.master.event_generate(actions_name[index])
        time.sleep(0.01)
    print("final Score : " + str(gamegrid.score))


# random_algo()
greedy_algo()
# gamegrid.mainloop()
