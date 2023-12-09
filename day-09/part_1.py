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
            diff = abs(items[i] - items[i - 1])
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

    for numbers in values:
        print(numbers)

    return values[-1][-1]


lines = input.splitlines()
total = 0
for line in lines:
    items = list(map(lambda x: int(x), filter(lambda x: x.isdigit(), line.split(" "))))
    total += extrapolate(items)

print("Part 1: ", total)
