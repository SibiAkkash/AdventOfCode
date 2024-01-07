def parse_card(card: str) -> tuple[set[int], list[int]]:
    if not card:
        return set(), []

    card_no_str, nums = card.split(": ")

    winning_nums_str, card_nums_str = nums.split(" | ")

    winning_nums = set(map(int, winning_nums_str.strip().split()))
    card_nums = list(map(int, card_nums_str.strip().split()))

    return winning_nums, card_nums


def get_copy_cards_nos(
    card_no: int, winning_nums: set[int], card_nums: list[int]
) -> list[int]:
    num_matches = 0

    for num in card_nums:
        num_matches += 1 if num in winning_nums else 0

    if num_matches == 0:
        return []

    return list(range(card_no + 1, card_no + num_matches + 1))


def card_points(winning_nums: set[int], card_nums: list[int]) -> int:
    num_matches = 0

    for num in card_nums:
        num_matches += 1 if num in winning_nums else 0

    if num_matches == 0:
        return 0

    return 2 ** (num_matches - 1)


sample_input = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

# total = 0


# print(total)

# cards = list(filter(lambda card: card.strip(), sample_input.split("\n")))
with open("./input.txt", "r") as input_file:
    cards = [line.strip() for line in input_file.readlines()]

# index = card number
# value = num instances of that card
num_instances_of_cards: list[int] = [0]

for idx, card in enumerate(cards):
    card_no = idx + 1

    if card_no >= len(num_instances_of_cards):
        num_instances_of_cards.append(1)
    else:
        num_instances_of_cards[card_no] += 1

    multiplier = num_instances_of_cards[card_no]

    won_cards = get_copy_cards_nos(card_no, *parse_card(card))

    for won_card in won_cards:
        # its the first time we're seeing this card number
        # add it to the list
        if won_card >= len(num_instances_of_cards):
            num_instances_of_cards.append(1 * multiplier)
        else:
            num_instances_of_cards[won_card] += 1 * multiplier


print(sum(num_instances_of_cards))
