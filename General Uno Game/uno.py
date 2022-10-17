'''
Catarina Borges
2022/10/14
Uno game V1
'''
import player
import card
import random
import playerAI
import unoRules

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
def pick_hand():
    hand = []
    for num in range(7):
        hand.append(pick_card())
    return hand


player_number = int(input("Please pick a player by typing a number between 1-4.\n"))
while player_number<1 or player_number>4:
    player_number = int(input("Please pick a player by typing a number between 1-4.\n"))

player1 = player.Player(pick_hand(), "Player 1")
player2 = player.Player(pick_hand(), "Player 2")
player3 = player.Player(pick_hand(), "Player 3")
player4 = player.Player(pick_hand(), "Player 4")

opponent_decks = []
if player_number == 1:
    player_hand = player1
    opponent_decks = [player2, player3, player4]
    players = [player_hand, player2, player3, player4]
elif player_number == 2:
    player_hand = player2
    opponent_decks = [player1, player3, player4]
    players = [player1, player_hand, player3, player4]
elif player_number == 3:
    player_hand = player3
    opponent_decks = [player1, player2, player4]
    players = [player1, player2, player_hand, player4]
else:
    player_hand = player4
    opponent_decks = [player1, player2, player3]
    players = [player1, player2, player3, player_hand]

def itterate_cards(hand):
    for i in range(hand.get_num_cards()):
        print("Your card", (i+1), "is", hand.get_card(i).get_string())

'''
This is test code
for i in opponent_decks:
    print("\n\n")
    for m in range(7):
        print(i.get_name(), "card", (m + 1), "is", i.get_card(m).get_string())
'''

#start the game
top_card = (pick_card())
while top_card.get_type == "wild":
    top_card = (pick_card())

def make_move(top_card, player_going):
    print("\n\n")
    itterate_cards(player_going)
    print("\n\nThe top card is", top_card.get_string())
    card_played = -2
    while card_played < -1 or card_played > (player_going.get_num_cards() - 1):
        card_played = int(input("\nWhich card would you like to play? (Type 0 if you would like to pick up a card)\n")) - 1
    if card_played == -1:
        picked_up = pick_card()
        print("You picked up a ", picked_up.get_string())
        player_going.add_card(picked_up)
        return top_card
    print("You played " + player_going.get_card(card_played).get_string())
    new_top_card = player_going.get_card(card_played)
    player_going.use_card(card_played)
    return new_top_card

game_going = True
player_going = 1
while game_going:
    top_card = make_move(top_card, players[player_going])
    if player_going<3:
        player_going +=1
    else:
        player_going = 0
