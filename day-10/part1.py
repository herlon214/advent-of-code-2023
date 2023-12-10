from pprint import pprint

# Read input from file
input = open("test3.txt", "r").read()


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
            moves.append((row + 1, col))
            moves.append((row - 1, col))
        case "-":
            moves.append((row, col + 1))
            moves.append((row, col - 1))
        case "L":
            moves.append((row - 1, col))
            moves.append((row, col + 1))
        case "J":
            moves.append((row - 1, col))
            moves.append((row, col - 1))
        case "7":
            moves.append((row, col - 1))
            moves.append((row + 1, col))
        case "F":
            moves.append((row, col + 1))
            moves.append((row + 1, col))

    # Filter
    moves = filter_out_of_bounds(input, moves)

    # pprint(f"Available moves from {pos} ({input[row][col]}): {moves}")

    return moves


def connected_pipes(input, pos):
    row, col = pos
    possibilites = [
        (row + 1, col),
        (row - 1, col),
        (row, col + 1),
        (row, col - 1),
    ]
    possibilites = filter_out_of_bounds(input, possibilites)

    connected = []

    for p in possibilites:
        moves = available_moves(input, p)
        moves = list(filter(lambda x: x == pos, moves))

        if len(moves) > 0:
            connected.append(p)

    return connected


lines = input.splitlines()
pipes = [list(line) for line in lines]

starting_pos = find_start(pipes)
moves = connected_pipes(pipes, starting_pos)
moves = list(map(lambda x: (x, 1), moves))
highest_idx = 0

while len(moves) > 0:
    (current_pos, idx), moves = moves[0], moves[1:]
    # print("Current pos:", current_pos, pipes[current_pos[0]][current_pos[1]])
    next_moves = connected_pipes(pipes, current_pos)
    next_moves = list(map(lambda x: (x, idx + 1), next_moves))
    moves.extend(next_moves)

    # Taint current pos
    pipes[current_pos[0]][current_pos[1]] = str("+")

    if idx > highest_idx:
        highest_idx = idx

pprint(pipes)
print("Highest idx:", highest_idx)
