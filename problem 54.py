"""
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights
beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens,
then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards
are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	    	Player 2	 	Winner
1	 	5H 5C 6S 7S KD       2C 3S 8S 8D TD    Player 2
        Pair of Fives        Pair of Eights

2	 	5D 8C 9S JS AC       2C 5C 7D 8S QH    Player 1
       Highest card Ace    Highest card Queen

3	 	2D 9C AS AH AC       3D 6D 7D TD QD    Player 2
         Three Aces        Flush with Diamonds

4	 	4D 6S 9H QH QC       3D 6D 7H QD QS    Player 1
        Pair of Queens       Pair of Queens
      Highest card Nine    Highest card Seven

5	 	2H 2D 4C 4D 4S       3C 3D 3S 9S 9D    Player 1
          Full House           Full House
       With Three Fours      With Three Threes

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards
(separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can
assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order,
and in each hand there is a clear winner.

How many hands does Player 1 win?
"""


def get_hand_ranking(hand):
    suits = [card[1] for card in hand]
    values = [value_translations[card[0]] for card in hand]

    suit_set = set(suits)
    value_set = set(values)

    rank_dict = {
        10: (len(suit_set) == 1 and value_set == {10, 11, 12, 13, 14}),
        9: (len(suit_set) == 1 and sorted(values) == list(range(min(values), max(values) + 1))),
        8: (values.count(values[0]) == 4 or values.count(values[1]) == 4),
        7: (len(value_set) == 2),
        6: (len(suit_set) == 1),
        5: (sorted(values) == list(range(min(values), max(values) + 1))),
        4: (values.count(values[0]) == 3 or values.count(values[1]) == 3 or values.count(values[2]) == 3),
        3: (len(value_set) == 3),
        2: (len(value_set) == 4),
        1: True
    }

    higher_card_dict = {
        10: None,
        9: [max(values)],
        8: [max(value_set, key=values.count), min(value_set, key=values.count)],
        7: [max(value_set, key=values.count), min(value_set, key=values.count)],
        6: sorted(values, reverse=True),
        5: sorted(values, reverse=True),
        4: [max(value_set, key=values.count)],
        3: [max(sorted(value_set, reverse=True), key=values.count), max(sorted(value_set), key=values.count),
            min(value_set, key=values.count)],
        2: [pair := max(value_set, key=values.count)] + sorted((value for value in values if value != pair), reverse=True),
        1: sorted(values, reverse=True)
    }

    for rank, condition in rank_dict.items():
        if condition:
            return [rank, higher_card_dict[rank]]


def compare_highest_cards(highest_cards_1, highest_cards_2):
    for i in range(len(highest_cards_1)):
        if highest_cards_1[i] > highest_cards_2[i]:
            return 1

        elif highest_cards_1[i] < highest_cards_2[i]:
            return 2

    return None


with open("problem54hands", "r") as f:
    games = [row.replace("\n", "").split() for row in f]

value_translations = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12,
                      "K": 13, "A": 14}

player_one_wins = 0

for game in games:
    first_hand = game[:5]
    second_hand = game[5:]

    first_hand_ranking = get_hand_ranking(first_hand)[0]
    second_hand_ranking = get_hand_ranking(second_hand)[0]

    if first_hand_ranking > second_hand_ranking:
        player_one_wins += 1

    elif first_hand_ranking == second_hand_ranking:
        first_highest_list = get_hand_ranking(first_hand)[1]
        second_highest_list = get_hand_ranking(second_hand)[1]

        winner = compare_highest_cards(first_highest_list, second_highest_list)

        if winner == 1:
            player_one_wins += 1

print(player_one_wins)
