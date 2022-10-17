'''
Player class
'''

# Each player has 1 hand with x amount of cards

# Each player has 1 player to the right (right), one player to the left (left) and one player in front (front) of them

class Player:
    cards = []
    num_of_cards = 0
    name = ""
    def __init__(self, cards, name):
        self.cards = cards
        self.num_of_cards = len(cards)
        self.name = name

    def get_card(self, card_num):
        return self.cards[card_num]

    def get_name (self):
        return self.name

    def get_num_cards(self):
        return self.num_of_cards

    def add_card(self, new_card):
        self.cards.append(new_card)
        self.num_of_cards += 1

    def use_card(self, used_card):
        if used_card == 0:
            self.cards = self.cards[1:]
        else:
            temp_cards_1 = self.cards[0:used_card]
            if used_card < self.num_of_cards:
                temp_cards_2 = self.cards[used_card + 1:]
                self.cards = temp_cards_1 + temp_cards_2
            else:
                self.cards = temp_cards_1
        self.num_of_cards -= 1
