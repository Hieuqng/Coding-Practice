import argparse
import time


def is_valid(board, move, n):
    r, c = move
    return 0 <= r < n and 0 <= c < n and board[r][c] is None


def valid_moves(board, r, c, n):
    deltas = [
        (1, 2),
        (2, 1),
        (-1, 2),
        (2, -1),
        (1, -2),
        (-2, 1),
        (-1, -2),
        (-2, -1)
    ]

    all_moves = [(r + r_delta, c + c_delta) for r_delta, c_delta in deltas]
    return [move for move in all_moves if is_valid(board, move, n)]


def find_knight_tour(n):
    count = 0
    for i in range(n):
        for j in range(n):
            board = [[None for _ in range(n)] for _ in range(n)]
            board[i][j] = 0
            count += find_knight_tour_aux(board, [(i, j)], n)
    return count


def find_knight_tour_aux(board, tour, n):
    if len(tour) == n * n:
        return 1

    else:
        count = 0
        last_r, last_c = tour[-1]
        for r, c in valid_moves(board, last_r, last_c, n):
            tour.append((r, c))
            board[r][c] = len(tour)
            count += find_knight_tour_aux(board, tour, n)
            tour.pop()
            board[r][c] = None
    return count


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('size', action='store', help='size of the squared board', type=int)

    args = parser.parse_args()
    n = args.size
    start = time.time()
    num_tours = find_knight_tour(n)
    end = time.time()
    print(f'Number of tours of size {n}: {num_tours} ... % {(end-start) * 1000}')
