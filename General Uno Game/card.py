'''
Card Class
'''

class Card:
    cardnumber = -1
    cardcolor = -1
    cardtype = "None"

    def __init__(self, num, color, type):
        self.cardnumber = num
        self.cardcolor = color
        self.cardtype = type

    def color_string(self):
        if self.cardcolor == 0:
            return "RED"
        elif self.cardcolor == 1:
            return "BLUE"
        elif self.cardcolor == 2:
            return "GREEN"
        elif self.cardcolor == 3:
            return "YELLOW"
        else:
            return ""

    def type_string(self):
        if self.cardtype != "None":
            if self.cardtype == "wild":
                if self.cardnumber == 4:
                    return "pick up 4 wild"
            return self.cardtype
        else:
            return str(self.cardnumber)

    def get_card_string(self):
        return ""+ self.color_string()+ " "+ self.type_string()+ " card"

# A card is either a wild card (wild) or has a color designated to it

# A card is either a power card (power) or has a number designated to it

# A power card (power) can either be a skip card (skip), a wild card (wild), a +2 card (pickup), or a reverse card (rev)

# A wild card can either be regular (0) or be a pickup 4 (4)

