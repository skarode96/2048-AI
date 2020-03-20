from unittest import TestCase
import logic

class Test(TestCase):
    def test_cover_up(self):
        new_state = logic.cover_up([[2, 3, 0, 2], [0, 3, 0, 0], [2, 0, 0, 2], [0, 0, 0, 1]])
        print(new_state)

    def test_merge(self):
        new_state = logic.merge([[2, 3, 2, 0], [3, 0, 0, 0], [2, 2, 0, 0], [1, 0, 0, 0]])
        print(new_state)

