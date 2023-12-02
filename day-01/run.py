# Read input from file
input = open("input.txt", "r").read()

# Convert lines to list
lines = input.strip().split("\n")


def part_1(lines):
    # Extract numbers
    numbers = []
    for line in lines:
        numbers.append("".join([c for c in line if c.isdigit()]))

    # Extract first and last digit
    digits = []
    for number in numbers:
        digits.append(number[0] + number[-1])

    # Convert to int
    digits = [int(d) for d in digits]

    # Sum values
    return sum(digits)


def part_2(lines):
    numbers = []

    for line in lines:
        digits = []

        # Spelled numbers to convert
        spelledMap = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
        }
        spelled = [c for c in line]

        for i in range(len(spelled)):
            for j in range(len(spelled)):
                word = "".join(spelled[i : j + 1])

                if word == "":
                    continue

                # Normal digits
                if word.isdigit():
                    digits.append(word)
                    break

                # Spelled digits
                if word in spelledMap:
                    digits.append(str(spelledMap[word]))
                    break

        # Extract first and last digit
        numbers.append(digits[0] + digits[-1])

    # Convert to int
    numbers = [int(n) for n in numbers]

    # Sum values
    return sum(numbers)


print("Part 1:", part_1(lines))
print("Part 2:", part_2(lines))
