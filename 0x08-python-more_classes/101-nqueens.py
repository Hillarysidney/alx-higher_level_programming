#!/usr/bin/python3
"""Solution for the N-queens puzzle.
Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.
Examples:
    $ ./101-nqueens.py N
N must be an integer greater than or equal to 4.
Attributes:
    card (list): List of lists representing the chessboard.
    solutions (list): List of lists containing solutions.
Solutions are represented in the format [[o, g], [o, g], [o, g], [o, g]]
where `o` and `g` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys


def init_board(n):
    """Starting an `n`x`n` sized chessboard with 0's."""
    card = []
    [card.append([]) for t in range(n)]
    [row.append(' ') for t in range(n) for row in card]
    return (card)


def board_deepcopy(card):
    """Bring a deepcopy of a chessboard."""
    if isinstance(card, list):
        return list(map(board_deepcopy, card))
    return (card)


def get_solution(card):
    """Bring the list of lists representation of a solved chessboard."""
    solves = []
    for o in range(len(card)):
        for g in range(len(card)):
            if card[o][g] == "Q":
                solves.append([o, g])
                break
    return (solves)


def xout(card, row, col):
    """X out spots on a chessboard.
    All spots where non-attacking queens can no
    longer be played are X-ed out.
    Args:
        card (list): Current working chessboard.
        row (int): Row where a queen was last played.
        col (int): Column where a queen was last played.
    """
    # X out all forward spots
    for g in range(col + 1, len(card)):
        card[row][g] = "x"
    # X out all backwards spots
    for g in range(col - 1, -1, -1):
        card[row][g] = "x"
    # X out all spots below
    for o in range(row + 1, len(card)):
        card[o][col] = "x"
    # X out all spots above
    for o in range(row - 1, -1, -1):
        card[o][col] = "x"
    # X out all spots diagonally down to the right
    g = col + 1
    for o in range(row + 1, len(card)):
        if g >= len(card):
            break
        card[o][g] = "x"
        g += 1
    # X out all spots diagonally up to the left
    g = col - 1
    for o in range(row - 1, -1, -1):
        if g < 0:
            break
        card[o][g]
        g -= 1
    # X out all spots diagonally up to the right
    g = col + 1
    for o in range(row - 1, -1, -1):
        if g >= len(card):
            break
        card[o][g] = "x"
        g += 1
    # X out all spots diagonally down to the left
    g = col - 1
    for o in range(row + 1, len(card)):
        if g < 0:
            break
        card[o][g] = "x"
        g -= 1


def recursive_solve(card, row, queens, solutions):
    """Recursively solve an N-queens puzzle.
    Args:
        card (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    if queens == len(card):
        solutions.append(get_solution(card))
        return (solutions)

    for g in range(len(card)):
        if card[row][g] == " ":
            tmp_board = board_deepcopy(card)
            tmp_board[row][g] = "Q"
            xout(tmp_board, row, g)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    card = init_board(int(sys.argv[1]))
    solutions = recursive_solve(card, 0, 0, [])
    for sol in solutions:
        print(sol)
