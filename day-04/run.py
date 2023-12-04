# Read input from file
input = open("input.txt", "r").read()


# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
def parse_line(line):
    numbers = line.split(":")[1]
    winning, hand = numbers.split("|")

    # Convert numbers
    winning = filter(lambda x: x.isdigit(), winning.strip().split(" "))
    winning = [int(w) for w in winning]

    # Convert winning to object
    win_target = {}
    for w in winning:
        win_target[w] = w

    # Convert numbers
    hand = filter(lambda x: x.isdigit(), hand.strip().split(" "))
    hand = [int(h) for h in hand]

    # Check how many items in hand are in winning
    total = 0
    for item in hand:
        if item in win_target:
            total += 1

    value = 0
    if total > 0:
        value = 2 ** (total - 1)

    return {"winning": winning, "hand": hand, "points": value, "total": total}


def part_1(input):
    total = 0
    for line in input.split("\n"):
        total += parse_line(line)["points"]

    return total


def part_2(input):
    # Collect hand cards
    hand = []

    for line in input.split("\n"):
        hand.append([parse_line(line)["hand"], 1])

    # Play game
    for i, line in enumerate(input.split("\n")):
        round = parse_line(line)

        for j in range(i + 1, i + round["total"] + 1):
            hand[j][1] += 1 * hand[i][1]

    total = 0
    for h in hand:
        total += h[1]

    return total


print("Part 1: ", part_1(input))
print("Part 2: ", part_2(input))
