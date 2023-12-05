from pprint import pprint
import math

# Read input from file
input = open("input.txt", "r").read()

conversion_table = {}
source_destination = {}
destination_source = {}


def parse_map(line):
    line = line.split(" ")

    data = {
        "destination": int(line[0]),
        "source_start": int(line[1]),
        "range": int(line[2]),
    }

    data = {
        "destination": data["destination"],
        "source_start": range(
            data["source_start"], data["source_start"] + data["range"]
        ),
        "range": data["range"],
    }

    return data


def parse_chunk(lines):
    name = lines[0].split(" ")[0].split("-")
    source = name[0]
    destination = name[2]
    source_destination[source] = destination
    destination_source[destination] = source

    for line in lines[1:]:
        map = parse_map(line)

        if conversion_table.get(source) is None:
            conversion_table[source] = []

        conversion_table[source].append(map)


def recursive_lookup(source, number, target):
    # print("Source:", source, "Number:", number, "Target:", target)

    if conversion_table.get(source) is None:
        return number

    for map in conversion_table[source]:
        if number in map["source_start"]:
            diff = map["source_start"][0] - number

            return recursive_lookup(target[source], map["destination"] - diff, target)

    return recursive_lookup(target[source], number, target)


def part_1(input):
    # Create conversion table
    chunk = []
    lines = input.split("\n")
    for line in lines[2:]:
        if line == "":
            parse_chunk(chunk)
            chunk = []

            continue

        chunk.append(line)

    # Convert last chunk
    parse_chunk(chunk)

    # Lookup seeds
    seeds = lines[0].split(":")[1].strip().split(" ")
    lowest = math.inf
    for seed in seeds:
        seed = int(seed)
        destination = recursive_lookup("seed", seed, source_destination)

        if destination < lowest:
            lowest = destination

    return lowest


print("Part 1:", part_1(input))
