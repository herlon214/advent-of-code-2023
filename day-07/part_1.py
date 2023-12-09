from pprint import pprint
from functools import cmp_to_key

# Read input from file
input = open("input.txt", "r").read()

# Card power
FIVE_OF_A_KIND = 7
FOUR_OF_A_KIND = 6
FULL_HOUSE = 5
THREE_OF_A_KIND = 4
TWO_PAIR = 3
ONE_PAIR = 2
HIGH_CARD = 1

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

powers = [2**i for i in range(len(cards))]


def hand_compare(hand_a, hand_b):
    hand_strength_a = evaluate_hand(hand_a[0])
    hand_strength_b = evaluate_hand(hand_b[0])

    if hand_strength_a > hand_strength_b:
        return 1
    if hand_strength_a < hand_strength_b:
        return -1

    for hand_a, hand_b in zip(hand_a[0], hand_b[0]):
        power_a = powers[cards.index(hand_a)]
        power_b = powers[cards.index(hand_b)]
        if power_a > power_b:
            return 1
        elif power_a < power_b:
            return -1

    return 0


def evaluate_hand(hand):
    count = {}

    for card in hand:
        if card in count:
            count[card] += 1
        else:
            count[card] = 1

    inverse_count = {}
    for key, value in count.items():
        if value not in inverse_count:
            inverse_count[value] = [key]
        else:
            inverse_count[value].append(key)

    # Check hand types
    if 5 in inverse_count:
        return FIVE_OF_A_KIND

    if 4 in inverse_count:
        return FOUR_OF_A_KIND

    if 3 in inverse_count and 2 in inverse_count:
        return FULL_HOUSE

    if 3 in inverse_count:
        return THREE_OF_A_KIND

    if 2 in inverse_count and len(inverse_count[2]) == 2:
        return TWO_PAIR

    if 2 in inverse_count:
        return ONE_PAIR

    return HIGH_CARD


def part_1(input):
    lines = input.split("\n")

    sorted_hands_and_bids = []
    for line in lines:
        hand, bid = line.split(" ")

        sorted_hands_and_bids.append((hand, bid))

    sorted_hands_and_bids = sorted(sorted_hands_and_bids, key=cmp_to_key(hand_compare))

    total = 0
    for i, (hand, bid) in enumerate(sorted_hands_and_bids):
        total += (i + 1) * int(bid)

    return total


print("Part 1:", part_1(input))
