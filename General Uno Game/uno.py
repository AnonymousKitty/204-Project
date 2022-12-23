'''
Catarina Borges
2022/10/14
Uno game V1
'''
import player
import card
import random
import playerAI
# import unoRules

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
            power = "wild pickup"
            num = -1
        else:
            num = -1
    else:
        num = -1

    final_card = card.Card(num, color, power)
    return final_card

# generate 7 initial cards for each player (4 Players)
def pick_hand():
    hand = []
    for num in range(2):
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

def check_card(player, card_place, top_card):
    player_card = player.get_card(card_place)
    if player_card.get_type() == 'wild' or player_card.get_type() == 'wild pickup':
        color = -1
        while color >3 or color <0:
            print("What color would you like to change to?")
            color = int(input("Type 0 for RED, 1 for BLUE, 2 for GREEN, or 3 for YELLOW:"))
            print(color)
        player_card.change_color(color)
        return  card_place
    if player_card.get_number() == top_card.get_number() and player_card.get_number() != -1:
        return card_place
    elif player_card.get_type() == top_card.get_type() and player_card.get_type() != "None":
        return  card_place
    elif player_card.get_color() == top_card.get_color():
        return  card_place

    return -2
'''
This is test code
for i in opponent_decks:
    print("\n\n")
    for m in range(7):
        print(i.get_name(), "card", (m + 1), "is", i.get_card(m).get_string())
'''

#start the game
top_card = (pick_card())
while top_card.get_type() == "wild" or top_card.get_type() == "wild pickup":
    top_card = (pick_card())

def make_move(top_card, player_going):
    print("\n\n")
    itterate_cards(player_going)
    print("\n\nThe top card is", top_card.get_string())
    card_played = -2
    while card_played < -1 or card_played > (player_going.get_num_cards() - 1):
        card_played = int(input("\nWhich card would you like to play? (Type 0 if you would like to pick up a card)\n")) - 1
        if card_played != -1:
            card_played = check_card(player_going, card_played, top_card)
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
rev = False
duplicate = 0
while game_going:
    if top_card.get_type() == 'wild' or top_card.get_type() == 'None' or top_card.check_played() == True:
        top_card = make_move(top_card, players[player_going])
    else:
        # wild pickup, pickup, reverse, skip
        if top_card.get_type() == 'wild pickup':
            canPlay = False
            for i in players[player_going].get_all_cards():
                if i.get_type() == 'wild pickup':
                    canPlay = True
                    break
            if canPlay == False:
                pickup_cards = 4 + 4*duplicate
                for i in range(pickup_cards):
                    picked_up = pick_card()
                    print("You picked up a ", picked_up.get_string())
                    players[player_going].add_card(picked_up)
                    duplicate = 0
                print("You Picked up a total of", pickup_cards, "cards... T-T")
                top_card.change_played()
            else:
                new_top_card = make_move(top_card, players[player_going])
                if new_top_card == top_card:
                    pickup_cards = 4 + 4*duplicate -1
                    for i in range(pickup_cards):
                        picked_up = pick_card()
                        print("You picked up a ", picked_up.get_string())
                        players[player_going].add_card(picked_up)
                        duplicate = 0
                    print("You Picked up a total of", pickup_cards + 1, "cards... T-T")
                    top_card.change_played()
                else:
                    top_card = new_top_card
                    duplicate += 1
        if top_card.get_type() == 'pickup':
            if top_card.get_type() == 'pickup':
                canPlay = False
                for i in players[player_going].get_all_cards():
                    if i.get_type() == 'pickup':
                        canPlay = True
                        break
                if canPlay == False:
                    pickup_cards = 2 + 2 * duplicate
                    for i in range(pickup_cards):
                        picked_up = pick_card()
                        print("You picked up a ", picked_up.get_string())
                        players[player_going].add_card(picked_up)
                        duplicate = 0
                    print("You Picked up a total of", pickup_cards, "cards... T-T")
                    top_card.change_played()
                else:
                    new_top_card = make_move(top_card, players[player_going])
                    if new_top_card == top_card:
                        pickup_cards = 2 + 2 * duplicate - 1
                        for i in range(pickup_cards):
                            picked_up = pick_card()
                            print("You picked up a ", picked_up.get_string())
                            players[player_going].add_card(picked_up)
                            duplicate = 0
                        print("You Picked up a total of", pickup_cards + 1, "cards... T-T")
                        top_card.change_played()
                    else:
                        top_card = new_top_card
                        duplicate += 1
        if top_card.get_type() == 'reverse':
            if rev == True:
                rev = False
            else:
                rev = True
            top_card.change_played()
        if top_card.get_type() == 'skip':
            print("Player", player_number+1, "was skipped.")
            top_card.change_played()
        print("imagine this actually worked...")


    if players[player_going].get_num_cards() == 0:
        game_going = False
        break
    if rev == False:
        if player_going<3:
            player_going +=1
        else:
            player_going = 0
    if rev == True:
        if player_going >0:
            player_going -= 1
        else:
            player_going = 3

print("Congratulations Player", player_going)
