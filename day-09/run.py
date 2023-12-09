from pprint import pprint

# Read input from file
input = open("input.txt", "r").read()


def extrapolate(numbers):
    values = [numbers]
    stop = False

    while stop == False:
        new_line = []
        items = values[-1]

        only_zeroes = True
        for i in range(len(items) - 1, 0, -1):
            diff = items[i] - items[i - 1]
            new_line.append(diff)

            if diff != 0:
                only_zeroes = False

        new_line.reverse()

        if only_zeroes:
            stop = True

        values.append(new_line)

    # Append one extract 0 to last line
    values[-1].append(0)

    # Reverse the list
    values.reverse()

    for i, numbers in enumerate(values[1:]):
        sum = values[i][-1] + numbers[-1]
        values[i + 1].append(sum)

    return values[-1][-1]


lines = input.splitlines()


def part_1():
    total = 0
    for line in lines:
        items = list(map(lambda x: int(x), filter(lambda x: x != "", line.split(" "))))
        total += extrapolate(items)

    return total


def part_2():
    total = 0
    for line in lines:
        items = list(map(lambda x: int(x), filter(lambda x: x != "", line.split(" "))))
        items.reverse()
        total += extrapolate(items)

    return total


print("Part 1: ", part_1())
print("Part 2: ", part_2())
