'''
Card Class
'''

class Card:
    card_number = -1
    card_color = -1
    card_type = "None"
    played_out = False

    def __init__(self, num, color, type):
        self.card_number = num
        self.card_color = color
        self.card_type = type

    def color_string(self):
        if self.card_color == 0:
            return "RED "
        elif self.card_color == 1:
            return "BLUE "
        elif self.card_color == 2:
            return "GREEN "
        elif self.card_color == 3:
            return "YELLOW "
        else:
            return ""

    def type_string(self):
        if self.card_type != "None":
            if self.card_type == "wild pickup":
                return "pick up 4 wild "
            return (self.card_type+ " ")
        else:
            return ("" + str(self.card_number)+ " ")

    def get_string(self):
        return ""+ self.color_string()+ self.type_string()+ "card"

    def get_type(self):
        return self.card_type

    def get_number(self):
        return self.card_number

    def get_color(self):
        return self.card_color

    def change_color(self, color):
        if self.get_type() == "wild" or self.get_type() == "wild pickup":
            self.card_color = color
        else:
            print('error')

    def check_played(self):
        return self.played_out

    def change_played(self):
        self.played_out = True
# A card is either a wild card (wild) or has a color designated to it

# A card is either a power card (power) or has a number designated to it

# A power card (power) can either be a skip card (skip), a wild card (wild), a +2 card (pickup), or a reverse card (rev)

# A wild card can either be regular (0) or be a pickup 4 (4)

