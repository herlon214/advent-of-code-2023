# Read input from file
input = open("input.txt", "r").read()

# Convert lines to list
lines = input.strip().split("\n")


def part_1(lines):
    max_round = {"green": 13, "blue": 14, "red": 12}
    game_ids = []

    for line in lines:
        game, info = line.split(":")
        game = int(game.split(" ")[1])
        rounds = info.split(";")
        rounds = [round.split(",") for round in rounds]

        possible = False
        for cubes in rounds:
            plays = {}
            for cube in cubes:
                cube = cube.strip().split(" ")
                plays[cube[1]] = int(cube[0])

            if (
                plays.get("green", 0) > max_round["green"]
                or plays.get("blue", 0) > max_round["blue"]
                or plays.get("red", 0) > max_round["red"]
            ):
                possible = False
                break

            # Check if possible
            possible = True

        # Store game id if possible
        if possible:
            game_ids.append(game)

    return sum(game_ids)


def part_2(lines):
    powers = []

    for line in lines:
        game, info = line.split(":")
        game = int(game.split(" ")[1])
        rounds = info.split(";")
        rounds = [round.split(",") for round in rounds]

        colors_min = {"green": 0, "blue": 0, "red": 0}
        for cubes in rounds:
            plays = {}
            for cube in cubes:
                cube = cube.strip().split(" ")
                plays[cube[1]] = int(cube[0])

            # Update min colors
            for color, value in plays.items():
                colors_min[color] = max(colors_min[color], value)

        powers.append(colors_min["green"] * colors_min["blue"] * colors_min["red"])

    return sum(powers)


print("Part 1: ", part_1(lines))
print("Part 2: ", part_2(lines))
