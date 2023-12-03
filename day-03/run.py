# Read input from file
input = open("input.txt", "r").read()

used_ranges = []


def extract_number(lines, line_index, initial_index):
    if initial_index == -1 or lines[line_index][initial_index].isdigit() == False:
        return None

    # Go backwards until find a non-digit
    # thats' where the number starts
    for i in range(initial_index, -2, -1):
        if i == -1:
            start = i + 1
            break

        if lines[line_index][i].isdigit() == False:
            start = i + 1
            break

    # Go forwards until find a non-digit
    # thats' where the number ends
    for i in range(initial_index, len(lines[line_index]) + 1):
        if i == len(lines[line_index]):
            end = i
            break

        if lines[line_index][i].isdigit() == False:
            end = i
            break

    # Check if number was already used
    for used_range in used_ranges:
        if (
            line_index == used_range[0]
            and start >= used_range[1]
            and end <= used_range[2]
        ):
            return None

    # Update used ranges
    used_ranges.append((line_index, start, end))

    return int(lines[line_index][start:end])


def part_1(data):
    # Convert lines to list
    lines = data.strip().split("\n")

    total = 0

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            # Check if it's a symbol
            if char.isdigit() == False and char != ".":
                # print("--------------------")
                # print("found symbol:", char, "at", i, j)

                # Top left
                topleft = extract_number(lines, i - 1, j - 1)
                if topleft is not None:
                    total += topleft
                    # print("topleft:", topleft)

                # Top
                top = extract_number(lines, i - 1, j)
                if top is not None:
                    total += top
                    # print("top:", top)

                # Top right
                topright = extract_number(lines, i - 1, j + 1)
                if topright is not None:
                    total += topright
                    # print("topright:", topright)

                # Left
                left = extract_number(lines, i, j - 1)
                if left is not None:
                    total += left
                    # print("left:", left)

                # Right
                right = extract_number(lines, i, j + 1)
                if right is not None:
                    total += right
                    # print("right:", right)

                # Bottom left
                bottomleft = extract_number(lines, i + 1, j - 1)
                if bottomleft is not None:
                    total += bottomleft
                    # print("bottomleft:", bottomleft)

                # Bottom
                bottom = extract_number(lines, i + 1, j)
                if bottom is not None:
                    total += bottom
                    # print("bottom:", bottom)

                # Bottom right
                bottomright = extract_number(lines, i + 1, j + 1)
                if bottomright is not None:
                    total += bottomright
                    # print("bottomright:", bottomright)

    return total


def part_2(data):
    # Convert lines to list
    lines = data.strip().split("\n")

    total = 0

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            # Check if it's a symbol
            if char.isdigit() == False and char != ".":
                # print("--------------------")
                # print("found symbol:", char, "at", i, j)

                part_numbers = []

                # Top left
                topleft = extract_number(lines, i - 1, j - 1)
                if topleft is not None:
                    part_numbers.append(topleft)

                # Top
                top = extract_number(lines, i - 1, j)
                if top is not None:
                    part_numbers.append(top)

                # Top right
                topright = extract_number(lines, i - 1, j + 1)
                if topright is not None:
                    part_numbers.append(topright)

                # Left
                left = extract_number(lines, i, j - 1)
                if left is not None:
                    part_numbers.append(left)

                # Right
                right = extract_number(lines, i, j + 1)
                if right is not None:
                    part_numbers.append(right)

                # Bottom left
                bottomleft = extract_number(lines, i + 1, j - 1)
                if bottomleft is not None:
                    part_numbers.append(bottomleft)

                # Bottom
                bottom = extract_number(lines, i + 1, j)
                if bottom is not None:
                    part_numbers.append(bottom)

                # Bottom right
                bottomright = extract_number(lines, i + 1, j + 1)
                if bottomright is not None:
                    part_numbers.append(bottomright)

                if len(part_numbers) == 2:
                    total += part_numbers[0] * part_numbers[1]

    return total


print("Part 1:", part_1(input))


# Reset used ranges
used_ranges = []
print("Part 2:", part_2(input))
