from pprint import pprint
from math import lcm

# Read input from file
input = open("input.txt", "r").read()

start = []
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

    # Check if it's a starting node
    if origin[-1] == "A":
        start.append(
            {
                "current_direction": 0,
                "current_node": origin,
                "starting_node": origin,
                "at_the_end": False,
                "end_steps": 0,
                "steps": 0,
            }
        )


steps = 0
while True:
    # Iterate over all the starting nodes
    for index, node in enumerate(start):
        if node["at_the_end"]:
            continue

        directions = lines[0]
        current_direction = node["current_direction"]
        current_node = node["current_node"]
        at_the_end = node["at_the_end"]

        # Check if found the end
        if current_node[-1] == "Z":
            at_the_end = True

        # Update node
        if directions[current_direction] == "L":
            current_node = graph[current_node][0]
        else:
            current_node = graph[current_node][1]

        # Update direction
        current_direction = (current_direction + 1) % len(directions)

        # Update node info
        start[index]["current_direction"] = current_direction
        start[index]["current_node"] = current_node
        start[index]["at_the_end"] = at_the_end
        if at_the_end:
            start[index]["end_steps"] = steps

    # Check if all the nodes are at the end
    nodes_at_the_end = 0
    for node in start:
        if node["at_the_end"]:
            nodes_at_the_end += 1

    if nodes_at_the_end == len(start):
        break

    # Update steps
    steps += 1

# Calculate the LCM of all the end steps
end_steps = []
for node in start:
    end_steps.append(node["end_steps"])

print("Part 2: " + str(lcm(*end_steps)))
