from pprint import pprint
import time
import os

# Read input from file
input = open("test4.txt", "r").read()


def clear():
    os.system("cls||clear")


def find_start(input):
    for i, row in enumerate(input):
        for j, col in enumerate(row):
            if col == "S":
                return (i, j)


def filter_out_of_bounds(input, moves):
    # Filter out invalid moves
    moves = filter(lambda x: x[0] >= 0 and x[1] >= 0, moves)
    moves = filter(lambda x: x[0] < len(input) and x[1] < len(input[0]), moves)
    moves = filter(
        lambda x: input[x[0]][x[1]] != "+" and input[x[0]][x[1]] != ".", moves
    )
    moves = list(moves)

    return moves


def available_moves(input, pos):
    moves = []
    row, col = pos

    match input[row][col]:
        case "|":
            moves.append((row + 2, col))
            moves.append((row - 2, col))
        case "-":
            moves.append((row, col + 2))
            moves.append((row, col - 2))
        case "L":
            moves.append((row - 2, col))
            moves.append((row, col + 2))
        case "J":
            moves.append((row - 2, col))
            moves.append((row, col - 2))
        case "7":
            moves.append((row, col - 2))
            moves.append((row + 2, col))
        case "F":
            moves.append((row, col + 2))
            moves.append((row + 2, col))

    # Filter
    moves = filter_out_of_bounds(input, moves)

    # pprint(f"Available moves from {pos} ({input[row][col]}): {moves}")

    return moves


def connected_pipes(input, pos):
    row, col = pos
    possibilites = [
        (row + 2, col),
        (row - 2, col),
        (row, col + 2),
        (row, col - 2),
    ]
    possibilites = filter_out_of_bounds(input, possibilites)

    connected = []

    for p in possibilites:
        moves = available_moves(input, p)
        connected_moves = list(filter(lambda x: x == pos, moves))

        if len(connected_moves) > 0:
            connected.append(p)

    return connected


lines = input.splitlines()
pipes = [list(line) for line in lines]
new_pipes = []

# Append in-between pipes
for row in pipes:
    new_row = []
    for col in row:
        new_row.append(col)
        new_row.append("-")
    new_pipes.append(new_row)
    new_pipes.append(["-"] * len(new_row))


pipes = new_pipes

for line in pipes:
    print(" ".join(line))

print("---------------")

starting_pos = find_start(pipes)
moves = connected_pipes(pipes, starting_pos)
moves = list(map(lambda x: (x, 1), moves))
highest_idx = 0

while len(moves) > 0:
    (current_pos, idx), moves = moves[-1], moves[:-1]
    # print("Current pos:", current_pos, pipes[current_pos[0]][current_pos[1]])
    next_moves = connected_pipes(pipes, current_pos)
    next_moves = list(map(lambda x: (x, idx + 1), next_moves))
    moves.extend(next_moves)

    # Taint current pos
    pipes[current_pos[0]][current_pos[1]] = str("+")

    if idx > highest_idx:
        highest_idx = idx

    clear()
    print("---------------")
    for line in pipes:
        print(" ".join(line))
    time.sleep(0.2)

print("Highest idx:", highest_idx)
