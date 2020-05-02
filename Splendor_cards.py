'''
Splendor Card descriptions

This file contains the description of each card in the Splendor deck, including:
    Card level
    Victory points
    Card cost (in gems)
    Card production (gem type)

The cards are currently organized into decks by Card Level.

I don't think the card color/size information should be stored here, since the
representation of the card back and color will be dependent on the windowing sytem
(e.g. tkinter vs pygame).  That said, the color is likely to be universal (just a string)
so that may be OK to include with the deck, particularly since that is copied from the
game rather than specific to the computer display of the cards.

The constants for card and board size will be left here as comments for reference, bu the
actual variables will be declared in a different file

#  Constants
board_height = 800
board_width = 800

card_height = 150
card_width = 100
card_cols = 4
card_rows = 3
card_gap = 10

'''

'''
class Gems(Enum):
    D = 'Diamond'
    S = 'Sapphire'
    E = 'Emerald'
    R = 'Ruby'
    O = 'Onyx'
'''

#  The Enumerated type actually makes the code more cumbersome.  Going back to just declaring string constants.
D = 'Diamond'
S = 'Sapphire'
E = 'Emerald'
R = 'Ruby'
O = 'Onyx'
G = 'Gold'

resource_limits = {
    D: 7, S: 7, E: 7, R: 7, O: 7, G: 5
}

BG = 0
FG = 1
resource_colors = {
    D: ("SlateGray4", "white"),
    S: ("blue", "white"),
    E: ("green", "white"),
    R: ("red", "white"),
    O: ("brown4", "white"),
    G: ("gold", "black"),
}

card_backs = ["green", "gold", "blue"]  # index is card level

card_fronts = {
    D: "white",
    S: "light blue",
    E: "light green",
    R: "pink",
    O: "tan",
}

gem_types = (D, S, E, R, O,)


class Card_data:
    def __init__(self, v=0, g='None', d=0, s=0, e=0, r=0, o=0):
        self.victory_points = v
        self.gem_produced = g
        self.emerald_cost = e
        self.sapphire_cost = s
        self.ruby_cost = r
        self.diamond_cost = d
        self.onyx_cost = o
        #  version 2:
        self.cost = {E: e, S: s, D: d, R: r, O: o}  # order matters for display
        #  need a self.id as well

    def __repr__(self):
        return f'Card(v={self.victory_points}, g="{self.gem_produced}", e={self.emerald_cost}, s={self.sapphire_cost}, ' \
               f'r={self.ruby_cost}, d={self.diamond_cost}, o={self.onyx_cost})'


multi_line_comment_about_Gem_letters = """
D = 'Diamond'
S = 'Sapphire'
E = 'Emerald'
R = 'Ruby'
O = 'Onyx'
"""

cardsL1 = [
    #  Card(self, points, produces, cost_diamond, cost_sapphire, cost_emerald, cost_ruby, cost_onyx):
    # Card(0, E, d=0, s=0, e=0, r=0, o=0),
    Card_data(0, D, s=3),
    Card_data(0, D, d=0, s=2, e=2, r=0, o=1),
    Card_data(0, S, s=1, e=3, r=1),
    Card_data(0, S, e=2, o=2),
    Card_data(0, S, e=2, o=2),
    Card_data(0, E, d=2, s=1),  # Card(v=0, g="Emerald", e=0, s=1, r=0, d=2, o=0),
    Card_data(0, E, d=0, s=1, e=0, r=2, o=2),
    Card_data(0, E, d=2, s=1),
    Card_data(0, E, d=1, s=1, e=0, r=1, o=2),
    Card_data(0, E, d=1, s=3, e=1, r=0, o=0),
    Card_data(0, E, d=0, s=0, e=0, r=3, o=0),
    Card_data(0, R, d=1, s=1, o=3),
    Card_data(0, R, d=4),
    Card_data(0, O, d=0, s=0, e=1, r=3, o=1),
    Card_data(0, R, d=2, s=0, e=1, r=0, o=2),
    Card_data(0, R, d=0, s=2, e=1, r=0, o=0),
    Card_data(0, E, d=0, s=2, e=0, r=2, o=0),
    Card_data(1, E, d=0, s=0, e=0, r=0, o=4),
    Card_data(0, S, d=1, s=0, e=1, r=2, o=1),
    Card_data(0, D, d=0, s=1, e=2, r=1, o=1),
    Card_data(0, O, d=1, s=1, e=1, r=1, o=0),
    Card_data(0, S, d=1, s=0, e=0, r=0, o=2),
    Card_data(1, S, d=0, s=0, e=0, r=4, o=0),
    Card_data(0, S, d=0, s=0, e=0, r=0, o=3),
    Card_data(0, D, d=0, s=0, e=0, r=2, o=1),
    Card_data(0, D, d=3, s=1, e=0, r=0, o=1),
    Card_data(1, D, d=0, s=0, e=4, r=0, o=0),
    Card_data(0, D, d=0, s=2, e=0, r=0, o=2),
    Card_data(0, O, d=2, s=0, e=2, r=0, o=0),
    Card_data(0, O, d=0, s=0, e=3, r=0, o=0),
    Card_data(1, O, d=0, s=0, e=4, r=0, o=0),
    Card_data(0, S, d=1, s=0, e=1, r=1, o=1),
    Card_data(0, R, d=3, s=0, e=0, r=0, o=0),
    Card_data(0, O, d=1, s=2, e=1, r=1, o=0),
    Card_data(0, R, d=2, s=1, e=1, r=0, o=1),
    Card_data(0, R, d=2, s=0, e=0, r=2, o=0),
    Card_data(0, D, d=0, s=1, e=1, r=1, o=1),
    Card_data(0, R, d=1, s=1, e=1, r=0, o=1),
    Card_data(0, O, d=0, s=0, e=2, r=1, o=0),
    Card_data(0, O, d=2, s=2, e=0, r=1, o=0),
    Card_data(0, E, d=1, s=0, e=1, r=1, o=1),
    Card_data(0, S, d=1, s=0, e=2, r=2, o=0),
]

cardsL2 = [
    #  Card(self, points, produces, cost_diamond, cost_sapphire, cost_emerald, cost_ruby, cost_onyx):
    Card_data(2, O, d=5),
    Card_data(1, S, s=2, e=2, r=3),
    Card_data(1, D, e=3, r=2, o=2),
    Card_data(2, S, d=0, s=0, e=5, r=0, o=0),
    Card_data(1, S, d=0, s=2, e=3, r=0, o=3),
    Card_data(3, E, d=0, s=0, e=6, r=0, o=0),
    Card_data(1, E, d=3, s=0, e=2, r=3, o=0),
    Card_data(1, E, d=2, s=3, e=0, r=0, o=2),
    Card_data(1, R, d=0, s=3, e=0, r=2, o=3),
    Card_data(2, R, d=1, s=4, e=2, r=0, o=0),
    Card_data(2, R, d=0, s=0, e=0, r=0, o=5),
    Card_data(1, O, d=3, s=2, e=2, r=0, o=0),
    Card_data(2, E, d=0, s=5, e=3, r=0, o=0),
    Card_data(2, E, d=4, s=2, e=0, r=0, o=1),
    Card_data(2, D, d=0, s=0, e=0, r=5, o=0),
    Card_data(3, S, d=0, s=6, e=0, r=0, o=0),
    Card_data(2, S, d=5, s=3, e=0, r=0, o=0),
    Card_data(3, D, d=6, s=0, e=0, r=0, o=0),
    Card_data(2, D, d=0, s=0, e=1, r=4, o=2),
    Card_data(2, R, d=3, s=0, e=0, r=0, o=5),
    Card_data(3, R, d=9, s=0, e=0, r=6, o=0),
    Card_data(1, D, d=2, s=3, e=0, r=3, o=0),
    Card_data(2, O, d=0, s=1, e=4, r=2, o=0),
    Card_data(2, O, d=0, s=0, e=5, r=3, o=0),
    Card_data(2, D, d=0, s=0, e=0, r=5, o=3),
    Card_data(1, R, d=2, s=0, e=0, r=2, o=3),
    Card_data(2, E, d=0, s=0, e=5, r=0, o=0),
    Card_data(2, E, d=2, s=0, e=0, r=1, o=4),
    Card_data(3, O, d=0, s=0, e=0, r=0, o=6),
]

cardsL3 = [
    #  Card(self, points, produces, cost_diamond, cost_sapphire, cost_emerald, cost_ruby, cost_onyx):
    # Card(2, E, d=0, s=0, e=0, r=0, o=0),
    Card_data(5, D, d=3, s=0, e=0, r=0, o=7),
    Card_data(5, O, d=0, s=0, e=0, r=7, o=3),
    Card_data(3, D, d=0, s=3, e=3, r=5, o=3),
    Card_data(3, E, d=5, s=3, e=0, r=3, o=3),
    Card_data(4, D, d=3, s=0, e=0, r=3, o=6),
    Card_data(4, S, d=6, s=3, e=0, r=0, o=3),
    Card_data(4, O, d=0, s=0, e=3, r=6, o=3),
    Card_data(3, S, d=3, s=0, e=3, r=3, o=5),
    Card_data(4, E, d=3, s=6, e=3, r=0, o=0),
    Card_data(4, E, d=0, s=7, e=0, r=0, o=0),
    Card_data(4, D, d=0, s=0, e=0, r=0, o=7),
    Card_data(5, S, d=7, s=3, e=0, r=0, o=0),
    Card_data(4, S, d=7, s=0, e=0, r=0, o=0),
    Card_data(4, O, d=0, s=0, e=0, r=7, o=0),
    Card_data(3, O, d=3, s=3, e=5, r=3, o=0),
    Card_data(5, E, d=0, s=7, e=3, r=0, o=0),
    Card_data(4, R, d=0, s=0, e=7, r=0, o=0),
    Card_data(5, R, d=0, s=0, e=7, r=3, o=0),
    Card_data(4, R, d=0, s=3, e=6, r=3, o=0),
    Card_data(3, R, d=3, s=5, e=3, r=0, o=3),
]

card_stacks = [cardsL3, cardsL2, cardsL1]
