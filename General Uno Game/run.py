from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood

# Encoding that will store all of your constraints
E = Encoding()

# Set the properties of Uno cards
NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, None]
COLORS = ['RED', 'GREEN', 'BLUE', 'YELLOW']
TYPES = ['regular', 'reverse', 'skip', 'wild', 'wild pick up']
# position in hand or top card of pile
POSITIONS = [1, 2, 3, 'top']
# whether other players have 3 cards
# NUMOFCARDS is True when the player has more than 3 cards in their hand, and false when they have 3 or less cards in their hand
NUMOFCARDS = [True, False]
# places players can exist. Using term "Direction" instead of P1/P2/P3 because of the need to specify when a player in place 'a' has more or less than 3 cards
DIRECTION = ['Left', 'Front', 'Right']

# Propositions for the game
PROPOSITIONS = []

class Unique(object):
  def __hash__(self):
    return hash(str(self))
  def __eq__(self, other):
    return hash(self) == hash(other)
  def __repr__(self):
    return str(self)
  def __str__(self):
    assert False, "You need to define the __str__ function on a proposition class"

@proposition(E)
class NumberColorType(Unique):
    # Creates a possible card type
    def __init__(self, number, color, type, position):
        self.number = number
        self.color = color
        self.type = type
        self.position = position

    def __repr__(self):
        return f"card@{self.position}=[{self.number},{self.color},{self.type}]"


# create ALL of the needed propositions for card types
for number in NUMBERS:
    for color in COLORS:
        for type in TYPES:
            for position in POSITIONS:
                PROPOSITIONS.append(NumberColorType(number, color, type, position))


@proposition(E)
class NumOfCards(Unique):
    # for whether or not players have 3 cards or not
    def __init__(self, player, bool):
        self.player = player
        self.hasMoreThanThree = bool

    def __repr__(self):
        return f"player@{self.player}={self.hasMoreThanThree}"


# create all possibilities other players have 3 cards or not
for player in DIRECTION:
    for bool in NUMOFCARDS:
        PROPOSITIONS.append(NumOfCards(player, bool))

for positions in POSITIONS:
  constraint.add_exactly_one(E, [NumberColorType(number, color, type)])

# other options include: at most one, exactly one, at most k, and implies all.
# For a complete module reference, see https://bauhaus.readthedocs.io/en/latest/bauhaus.html
@constraint.at_least_one(E)
# Build an example full theory for your setting and return it.
#
#  There should be at least 10 variables, and a sufficiently large formula to describe it (>50 operators).
#  This restriction is fairly minimal, and if there is any concern, reach out to the teaching staff to clarify
#  what the expectations are.
# CONSTRAINTS

# A card need to be a valid card if: 
# 1) the card is a "regular" card with a number and aacolor
# 2) the card is a "wild" or "wild pick up" card with neither number nor color
# 3) the card is a "reverse" or "skip" card with a color but no number
# Add custom constraints by creating formulas with the variables you created.

for position in POSITIONS:
  for number in NUMBERS:
      for type in TYPES:
        if type == 'regular':
          if number != None:
            constraint.add_exactly_one(E, [NumberColorType(number, color, type, position) for color in COLORS) 
        else if type == 'wild' or type == 'wild pick up':
          if number == None:
            constraint.add_exactly_one(E, [NumberColorType(number, None, type, position)]) 
        else:
          if number == None:
            constraint.add_exactly_one(E, [NumberColorType(number, color, type, position)] for color in COLORS) 
              


            
def example_theory():
    # If the palyer has a card that is the same color as the top card, it can be played

    pass
    #E.add_constraint((a | b) & ~x)
    # Implication
    #E.add_constraint(y >> z)
    # Negate a formula
    #E.add_constraint(~(x & y))
    # You can also add more customized "fancy" constraints. Use case: you don't want to enforce "exactly one"
    # for every instance of BasicPropositions, but you want to enforce it for a, b, and c.:
    #constraint.add_exactly_one(E, a, b, c)

    #return E


if __name__ == "__main__":

    T = example_theory()
    # Don't compile until you're finished adding all your constraints!
    T = T.compile()
    # After compilation (and only after), you can check some of the properties
    # of your model:
    print("\nSatisfiable: %s" % T.satisfiable())
    print("# Solutions: %d" % count_solutions(T))
    print("   Solution: %s" % T.solve())

    print("\nVariable likelihoods:")
    for v, vn in zip([a, b, c, x, y, z], 'abcxyz'):
        # Ensure that you only send these functions NNF formulas
        # Literals are compiled to NNF here
        print(" %s: %.2f" % (vn, likelihood(T, v)))
    print()
