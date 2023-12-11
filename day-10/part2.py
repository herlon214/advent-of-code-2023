from pprint import pprint
import time
import os

markers = ["~", "?", "o"]

# Read input from file
input = open("test5.txt", "r").read()


def viz(pipes, erase=False):
    if erase:
        clear()

    for line in pipes:
        print(" ".join(line))

    time.sleep(0.1)


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

    if len(moves) == 2:
        return moves

    # pprint(f"Available moves from {pos} ({input[row][col]}): {moves}")

    return []


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


def extract_half_moves(current_pos, next_moves):
    half_moves = map(
        lambda x: (x[0] - current_pos[0], x[1] - current_pos[1]), next_moves
    )
    half_moves = list(map(lambda x: (x[0] // 2, x[1] // 2), half_moves))

    return half_moves


def magic_wand(input, current_pos, marker="~"):
    next_moves = [current_pos]
    seen = {}
    count = 0

    while len(next_moves) > 0:
        current_pos, next_moves = next_moves[0], next_moves[1:]
        moves = [
            # Top
            (current_pos[0] - 1, current_pos[1]),
            # Bottom
            (current_pos[0] + 1, current_pos[1]),
            # Left
            (current_pos[0], current_pos[1] - 1),
            # Right
            (current_pos[0], current_pos[1] + 1),
        ]

        # Filter out invalid moves
        moves = filter(lambda x: x[0] >= 0 and x[1] >= 0, moves)
        moves = filter(lambda x: x[0] < len(input) and x[1] < len(input[0]), moves)
        moves = list(
            filter(
                lambda x: input[x[0]][x[1]] != "+" and input[x[0]][x[1]] not in markers,
                moves,
            )
        )
        moves = list(filter(lambda x: x not in seen, moves))

        # Taint current pos
        if input[current_pos[0]][current_pos[1]] == ".":
            count += 1
        input[current_pos[0]][current_pos[1]] = marker

        # Append next moves
        next_moves.extend(moves)

        # Update seen
        for move in moves:
            seen[move] = True

        # viz(input)

    return count


lines = input.splitlines()
pipes = [list(line) for line in lines]
new_pipes = []

# Append in-between pipes
for row in pipes:
    new_row = []
    for col in row:
        new_row.append(col)
        new_row.append(" ")
    new_pipes.append(new_row)
    new_pipes.append([" "] * len(new_row))


pipes = new_pipes

for line in pipes:
    print(" ".join(line))

print("---------------")

starting_pos = find_start(pipes)
moves = connected_pipes(pipes, starting_pos)
half_moves = extract_half_moves(starting_pos, moves)

# Taint
pipes[starting_pos[0]][starting_pos[1]] = str("+")
for move in half_moves:
    pipes[starting_pos[0] + move[0]][starting_pos[1] + move[1]] = str("+")


moves = list(map(lambda x: (x, 1), moves))
highest_idx = 0

while True:
    (current_pos, idx), moves = moves[-1], moves[:-1]
    if current_pos == starting_pos:
        break
    # print("Current pos:", current_pos, pipes[current_pos[0]][current_pos[1]])
    next_moves = connected_pipes(pipes, current_pos)
    half_moves = extract_half_moves(current_pos, next_moves)
    next_moves = list(map(lambda x: (x, idx + 1), next_moves))

    if len(next_moves) > 0:
        moves.extend(next_moves)

        print("Moves", len(moves))

        # Taint current pos
        pipes[current_pos[0]][current_pos[1]] = str("+")
        for move in half_moves:
            pipes[current_pos[0] + move[0]][current_pos[1] + move[1]] = str("+")

    if idx > highest_idx:
        highest_idx = idx

    viz(pipes, erase=True)


# Apply magick wand around the starting pos
moves = [
    # Top left
    (starting_pos[0] - 1, starting_pos[1] - 1),
    # Top
    (starting_pos[0] - 1, starting_pos[1]),
    # Top right
    (starting_pos[0] - 1, starting_pos[1] + 1),
    # Left
    (starting_pos[0], starting_pos[1] - 1),
    # Right
    (starting_pos[0], starting_pos[1] + 1),
    # Bottom left
    (starting_pos[0] + 1, starting_pos[1] - 1),
    # Bottom
    (starting_pos[0] + 1, starting_pos[1]),
    # Bottom right
    (starting_pos[0] + 1, starting_pos[1] + 1),
]

# Filter out invalid moves
moves = filter_out_of_bounds(pipes, moves)
moves = list(filter(lambda x: pipes[x[0]][x[1]] != "+", moves))

for i, move in enumerate(moves):
    if pipes[move[0]][move[1]] in markers:
        continue

    print("---------------")
    print("Magic wand at:", move)
    count = magic_wand(
        pipes, move, marker=markers[i % len(markers)]
    )  # Divide by 2 because we doubled the space
    print("Total count:", count)
