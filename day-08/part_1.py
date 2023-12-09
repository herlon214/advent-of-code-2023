# Read input from file
input = open("input.txt", "r").read()

start = "AAA"
end = "ZZZ"

graph = {}

lines = input.splitlines()
for line in lines[1:]:
    if line == "":
        continue

    origin, destinations = line.split(" = ")
    destination_a, destination_b = destinations.split(", ")
    destination_a, destination_b = destination_a[1:], destination_b[:-1]

    graph[origin] = [destination_a, destination_b]


directions = lines[0]
current_direction = 0
current_node = start
steps = 0
while current_direction > -1:
    # Check if found the end
    if current_node == end:
        print("Found the end in " + str(steps) + " steps")
        break

    # Update node
    if directions[current_direction] == "L":
        current_node = graph[current_node][0]
    else:
        current_node = graph[current_node][1]

    # Update direction
    current_direction = (current_direction + 1) % len(directions)

    # Update steps
    steps += 1
