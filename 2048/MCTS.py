import puzzle
import logic
import random

actions_name = ["<<UP>>", "<<DOWN>>", "<<LEFT>>", "<<RIGHT>>"]
actions_func = [logic.up, logic.down, logic.left, logic.right]

class MCTS:
    def __init__(self):
        pass

    def monte_carlo_search(self, gamegrid):
        """play with random moves given a board state and return average score"""
        scores = list()
        for i in range(25):
            # game = Game()
            # score = game.play_random_with_state(board_state, score)
            # scores.append(score)
            #tempGameGrid = puzzle.GameGrid(param = board_state)

            # tempGameGrid.matrix = board_state
            tempGameGrid = gamegrid
            tempGameGrid.master.event_generate(actions_name[random.randint(0, 3)])
            scores.append(tempGameGrid.score)

        return sum(scores) / len(scores)
