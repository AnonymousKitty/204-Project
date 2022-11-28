
from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood

# Encoding that will store all of your constraints
E = Encoding()

# Set the properties of Uno cards
NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
COLORS = ['RED','GREEN','BLUE','YELLOW']
TYPES = ['regular', 'reverse', 'skip', 'wild', 'wild pick up']
#position in hand or top card of pile
POSITIONS = [1, 2, 3, 'top']
#whether other players have 3 cards
NUMOFCARDS = [True, False]
# NUMOFCARDS is True when the player has more than 3 cards in their hand, and false when they have 3 or less cards in their hand

#Propositions for the game 
PROPOSITIONS = []

@proposition(E)
class NumberColorType:

    def __init__(self, number, color, type, position):
        self.number = number
        self.color = color
        self.type = type
        self.position = position

    def __repr__(self):
        return f"card@{self.position}=[{self.number},{self.color},{self.type}]"

#create all of the needed propositions for NumberColourType
for type in TYPES:
  if type == 'regular':
    for number in NUMBERS:
      for position in POSITIONS:
        for color in COLORS:
          PROPOSITIONS.append(NumberColorType(number, color, 'regular', position))
  else if (type == "wild" | type == "wild pick up"):
    for position in POSITIONS
      color = None
      number = None
      PROPOSITIONS.append(NumberColorType(number, color, type, position))
  else:
    for color in COLORS:
      for position in POSITIONS:
        PROPOSITIONS.append(NumberColorType(None, color, type, position))
    
    
#for whether or not players have 3 cards or not
@proposition(E)
class NumOfCards:
  def __init__(self, player2, player3, player4):
    self.player2 = player2
    self.player3 = player3
    self.player4 = player4
    
  def __repr__(self):
    return f"P2={self.player2}, P3={self.player3}, P4={self.player4}"

#create all possibilities other players have 3 cards or not
for numOfCardsP2 in NUMOFCARDS:
  for numOfCardsP3 in NUMOFCARDS:
    for numOfCardsP4 in NUMOFCARDS:
      PROPOSITIONS.append(NumOfCards(numOfCardsP2, numOfCardsP3, numOfCardsP4))

# Different classes for propositions are useful because this allows for more dynamic constraint creation
# for propositions within that class. For example, you can enforce that "at least one" of the propositions
# that are instances of this class must be true by using a @constraint decorator.
# other options include: at most one, exactly one, at most k, and implies all.
# For a complete module reference, see https://bauhaus.readthedocs.io/en/latest/bauhaus.html
@constraint.at_least_one(E)
# Build an example full theory for your setting and return it.
#
#  There should be at least 10 variables, and a sufficiently large formula to describe it (>50 operators).
#  This restriction is fairly minimal, and if there is any concern, reach out to the teaching staff to clarify
#  what the expectations are.

def example_theory():
    # Add custom constraints by creating formulas with the variables you created.
  
    # If the palyer has a card that is the same color as the top card, it can be played
  for pro in PROPOSITIONS:
    for position in POSITIONS:
      for number in NUMBER:
        for type in TYPE:
          if color1 == color2:
            E.add_constraint()
            
      
    E.add_constraint((a | b) & ~x)
    # Implication
    E.add_constraint(y >> z)
    # Negate a formula
    E.add_constraint(~(x & y))
    # You can also add more customized "fancy" constraints. Use case: you don't want to enforce "exactly one"
    # for every instance of BasicPropositions, but you want to enforce it for a, b, and c.:
    constraint.add_exactly_one(E, a, b, c)

    return E


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
    for v,vn in zip([a,b,c,x,y,z], 'abcxyz'):
        # Ensure that you only send these functions NNF formulas
        # Literals are compiled to NNF here
        print(" %s: %.2f" % (vn, likelihood(T, v)))
    print()
