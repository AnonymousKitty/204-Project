'''
Catarina Borges
2022/10/14
Uno game V1
'''
import player
import card
import random

#Randomizer
def pick_card():
    power = random.randint(-4, 9)
    if power<0:
        if power== -1:
            power = "wild"
        elif power == -2:
            power = "rev"
        elif power== -3:
            power = "pickup"
        elif power == -4:
            power = "skip"
    else:
        power = "None"
    if power != "wild":
        color = random.randint(0,3)
    else:
        color = -1
    if power == "None":
        num = random.randint(0,9)
    elif power == "wild":
        if random.randint(0,1) == 1:
            num = 4
        else:
            num = -1
    else:
        num = -1

    final_card = card.Card(num, color, power)
    return final_card

# generate 7 initial cards for each player (4 Players)
hand1 = []
for num in range(7):
    hand1.append(pick_card())
for i in hand1:
    print(i.get_card_string())
