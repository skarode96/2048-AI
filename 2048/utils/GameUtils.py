from game import logic
import random

class GameUtils:
    actions_name = ["<<UP>>", "<<DOWN>>", "<<LEFT>>", "<<RIGHT>>"]
    moves = [logic.up, logic.down, logic.left, logic.right]
    actions_name_dict = {
        0: "<<UP>>",
        1: "<<DOWN>>",
        2: "<<LEFT>>",
        3: "<<RIGHT>>"
    }

    def __init__(self):
        self.name = "GameUtils"
        self.actions_name_dict = GameUtils.actions_name_dict
        self.moves = GameUtils.moves

    def get_random_move_name(self):
        random_move_index = random.randint(0, 3)
        return self.actions_name_dict[random_move_index]

    def get_random_move_function(self):
        random_move_index = random.randint(0, 3)
        return self.moves[random_move_index]