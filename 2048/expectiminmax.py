import math
import itertools
from game import logic

MERGE_FUNCTIONS = {
    '<<LEFT>>': logic.left,
    '<<RIGHT>>': logic.right,
    '<<UP>>': logic.up,
    '<<DOWN>>': logic.down,
}


def get_moves(board):
    results = []
    for move, action in MERGE_FUNCTIONS.items():
        tempBoard, _, _, _, _ = action(board)
        result = move, expectiminmax_search(tempBoard, 4)
        results.append(result)
    return results


def evaluation(board):

    if not move_exists(board):
        return -float("inf")

    flattened_board = []
    for i, col in enumerate(zip(*board)):
        flattened_board.extend(reversed(col) if i % 2 == 0 else col)

    m = max(flattened_board)
    return sum(x / 10 ** n for n, x in enumerate(flattened_board)) - math.pow((board[3][0] != m) * abs(board[3][0] - m), 2)


def expectiminmax_search(board, depth, move=False):

    if depth == 0 or (move and not move_exists(board)):
        return evaluation(board)

    alpha = evaluation(board)
    if move:
        for _, action in MERGE_FUNCTIONS.items():
            child, _, _, _, _ = action(board)
            alpha = max(alpha, expectiminmax_search(child, depth - 1))
    else:
        alpha = 0
        zeros = [(i, j) for i, j in itertools.product(range(4), range(4)) if board[i][j] == 0]
        for i, j in zeros:
            c1 = [[x for x in row] for row in board]
            c2 = [[x for x in row] for row in board]
            c1[i][j] = 2
            c2[i][j] = 4
            alpha += (0.9 * expectiminmax_search(c1, depth - 1, True) / len(zeros) + 0.1 * expectiminmax_search(c2, depth - 1, True) / len(zeros))
    return alpha


def move_exists(board):
    for row in board:
        for x, y in zip(row[:-1], row[1:]):
            if x == y or x == 0 or y == 0:
                return True
    return False
