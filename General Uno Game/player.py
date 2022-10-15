'''
Player class
'''

# Each player has 1 hand with x amount of cards

# Each player has 1 player to the right (right), one player to the left (left) and one player in front (front) of them

class Player:
    cards = []
    card_number = 0
    def __init__(self, cards):
        self.cards = cards
        self.card_number = len(cards)
