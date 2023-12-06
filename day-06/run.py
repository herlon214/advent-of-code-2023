# Read input from file
input = open("input.txt", "r").read()


def estimate_alternatives(time, record):
    estimations = 0

    for i in range(1, time - 1):
        holding = i
        remaining_time = time - i
        result = remaining_time * holding

        if result > record:
            estimations += 1

    return estimations


def best_estimation(times, distances):
    total = 1

    for time, distance in zip(times, distances):
        result = estimate_alternatives(time, distance)
        total *= result

    return total


def part_1(input):
    input = input.split("\n")
    times, distances = input[0].strip(), input[1].strip()
    times = list(
        map(lambda x: int(x), filter(lambda x: x.isdigit(), times.split(" ")[1:]))
    )
    distances = list(
        map(lambda x: int(x), filter(lambda x: x.isdigit(), distances.split(" ")[1:]))
    )

    print("estimating")
    return best_estimation(times, distances)


def part_2(input):
    input = input.split("\n")
    time, distance = input[0].strip(), input[1].strip()
    time = int("".join(list(filter(lambda x: x.isdigit(), time.split(" ")[1:]))))
    distance = int(
        "".join(list(filter(lambda x: x.isdigit(), distance.split(" ")[1:])))
    )

    print("estimating")
    return best_estimation([time], [distance])


print("Part 1:", part_1(input))
print("Part 2:", part_2(input))
