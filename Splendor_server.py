import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
import random
from enum import Enum
import socket
import threading


root = tk.Tk()

#  Constants
board_height = 800
board_width = 800

card_height = 150
card_width = 100
card_cols = 4
card_rows = 3
card_gap = 10

card_backs = ["green", "gold", "blue"]      #  index is card level

class Gems(Enum):
    D = 'Diamond'
    S = 'Sapphire'
    E = 'Emerald'
    R = 'Ruby'
    O = 'Onyx'

#  The Enumerated type actually makes the code more cumbersome.  Going back to just declaring string constants.
D = 'Diamond'
S = 'Sapphire'
E = 'Emerald'
R = 'Ruby'
O = 'Onyx'


class Card:
    def __init__(self, v=0, g='None', d=0, s=0, e=0, r=0, o=0):
        self.victory_points = v
        self.gem_produced = g
        self.emerald_cost = e
        self.sapphire_cost = s
        self.ruby_cost = r
        self.diamond_cost = d
        self.onyx_cost = o
        #  need a self.id as well

    def __repr__(self):
        return f'Card(v={self.victory_points}, g="{self.gem_produced}", e={self.emerald_cost}, s={self.sapphire_cost}, '\
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
    #Card(0, E, d=0, s=0, e=0, r=0, o=0),
    Card(0, D, s=3),
    Card(0, D, d=0, s=2, e=2, r=0, o=1),
    Card(0, S, s=1, e=3, r=1),
    Card(0, S, e=2, o=2),
    Card(0, S, e=2, o=2),
    Card(0, E, d=2, s=1),           # Card(v=0, g="Emerald", e=0, s=1, r=0, d=2, o=0),
    Card(0, E, d=0, s=1, e=0, r=2, o=2),
    Card(0, E, d=2, s=1),
    Card(0, E, d=1, s=1, e=0, r=1, o=2),
    Card(0, E, d=1, s=3, e=1, r=0, o=0),
    Card(0, E, d=0, s=0, e=0, r=3, o=0),
    Card(0, R, d=1, s=1, o=3),
    Card(0, R, d=4),
    Card(0, O, d=0, s=0, e=1, r=3, o=1),
    Card(0, R, d=2, s=0, e=1, r=0, o=2),
    Card(0, R, d=0, s=2, e=1, r=0, o=0),
    Card(0, E, d=0, s=2, e=0, r=2, o=0),
    Card(1, E, d=0, s=0, e=0, r=0, o=4),
    Card(0, S, d=1, s=0, e=1, r=2, o=1),
    Card(0, D, d=0, s=1, e=2, r=1, o=1),
    Card(0, O, d=1, s=1, e=1, r=1, o=0),
    Card(0, S, d=1, s=0, e=0, r=0, o=2),
    Card(1, S, d=0, s=0, e=0, r=4, o=0),
    Card(0, S, d=0, s=0, e=0, r=0, o=3),
    Card(0, D, d=0, s=0, e=0, r=2, o=1),
    Card(0, D, d=3, s=1, e=0, r=0, o=1),
    Card(1, D, d=0, s=0, e=4, r=0, o=0),
    Card(0, D, d=0, s=2, e=0, r=0, o=2),
    Card(0, O, d=2, s=0, e=2, r=0, o=0),
    Card(0, O, d=0, s=0, e=3, r=0, o=0),
    Card(1, O, d=0, s=0, e=4, r=0, o=0),
    Card(0, S, d=1, s=0, e=1, r=1, o=1),
    Card(0, R, d=3, s=0, e=0, r=0, o=0),
    Card(0, O, d=1, s=2, e=1, r=1, o=0),
    Card(0, R, d=2, s=1, e=1, r=0, o=1),
    Card(0, R, d=2, s=0, e=0, r=2, o=0),
    Card(0, D, d=0, s=1, e=1, r=1, o=1),
    Card(0, R, d=1, s=1, e=1, r=0, o=1),
    Card(0, O, d=0, s=0, e=2, r=1, o=0),
    Card(0, O, d=2, s=2, e=0, r=1, o=0),
    Card(0, E, d=1, s=0, e=1, r=1, o=1),
    Card(0, S, d=1, s=0, e=2, r=2, o=0),
]

cardsL2 = [
    #  Card(self, points, produces, cost_diamond, cost_sapphire, cost_emerald, cost_ruby, cost_onyx):
    Card(2, O, d=5),
    Card(1, S, s=2, e=2, r=3),
    Card(1, D, e=3, r=2, o=2),
    Card(2, S, d=0, s=0, e=5, r=0, o=0),
    Card(1, S, d=0, s=2, e=3, r=0, o=3),
    Card(3, E, d=0, s=0, e=6, r=0, o=0),
    Card(1, E, d=3, s=0, e=2, r=3, o=0),
    Card(1, E, d=2, s=3, e=0, r=0, o=2),
    Card(1, R, d=0, s=3, e=0, r=2, o=3),
    Card(2, R, d=1, s=4, e=2, r=0, o=0),
    Card(2, R, d=0, s=0, e=0, r=0, o=5),
    Card(1, O, d=3, s=2, e=2, r=0, o=0),
    Card(2, E, d=0, s=5, e=3, r=0, o=0),
    Card(2, E, d=4, s=2, e=0, r=0, o=1),
    Card(2, D, d=0, s=0, e=0, r=5, o=0),
    Card(3, S, d=0, s=6, e=0, r=0, o=0),
    Card(2, S, d=5, s=3, e=0, r=0, o=0),
    Card(3, D, d=6, s=0, e=0, r=0, o=0),
    Card(2, D, d=0, s=0, e=1, r=4, o=2),
    Card(2, R, d=3, s=0, e=0, r=0, o=5),
    Card(3, R, d=9, s=0, e=0, r=6, o=0),
    Card(1, D, d=2, s=3, e=0, r=3, o=0),
    Card(2, O, d=0, s=1, e=4, r=2, o=0),
    Card(2, O, d=0, s=0, e=5, r=3, o=0),
    Card(2, D, d=0, s=0, e=0, r=5, o=3),
    Card(1, R, d=2, s=0, e=0, r=2, o=3),
    Card(2, E, d=0, s=0, e=5, r=0, o=0),
    Card(2, E, d=2, s=0, e=0, r=1, o=4),
    Card(3, O, d=0, s=0, e=0, r=0, o=6),
]


cardsL3 = [
    #  Card(self, points, produces, cost_diamond, cost_sapphire, cost_emerald, cost_ruby, cost_onyx):
    #Card(2, E, d=0, s=0, e=0, r=0, o=0),
    Card(5, D, d=3, s=0, e=0, r=0, o=7),
    Card(5, O, d=0, s=0, e=0, r=7, o=3),
    Card(3, D, d=0, s=3, e=3, r=5, o=3),
    Card(3, E, d=5, s=3, e=0, r=3, o=3),
    Card(4, D, d=3, s=0, e=0, r=3, o=6),
    Card(4, S, d=6, s=3, e=0, r=0, o=3),
    Card(4, O, d=0, s=0, e=3, r=6, o=3),
    Card(3, S, d=3, s=0, e=3, r=3, o=5),
    Card(4, E, d=3, s=6, e=3, r=0, o=0),
    Card(4, E, d=0, s=7, e=0, r=0, o=0),
    Card(4, D, d=0, s=0, e=0, r=0, o=7),
    Card(5, S, d=7, s=3, e=0, r=0, o=0),
    Card(4, S, d=7, s=0, e=0, r=0, o=0),
    Card(4, O, d=0, s=0, e=0, r=7, o=0),
    Card(3, O, d=3, s=3, e=5, r=3, o=0),
    Card(5, E, d=0, s=7, e=3, r=0, o=0),
    Card(4, R, d=0, s=0, e=7, r=0, o=0),
    Card(5, R, d=0, s=0, e=7, r=3, o=0),
    Card(4, R, d=0, s=3, e=6, r=3, o=0),
    Card(3, R, d=3, s=5, e=3, r=0, o=3),
]


def key(event):
    print("pressed", repr(event.char))

def callback(event):
    print("clicked at", event.x, event.y)


canvas = tk.Canvas(root, width=board_width, height=board_width)
root.bind("<Key>", key)
canvas.bind("<Button-1>", callback)
canvas.grid()

# put the pile in the middle of the board
pile_width = card_width * card_cols + card_gap * (card_cols - 1)
pile_start_loc_x = (board_width - pile_width) / 2
pile_height = card_height * card_rows + card_gap * (card_rows - 1)
pile_start_loc_y = (board_height - pile_height) / 2

x = pile_start_loc_x
y = pile_start_loc_y

pile = [[] for i in range(card_rows)]
print(pile)

# Display the up cards on the table
for i in range(card_rows):
    for j in range(card_cols):
        pile[i].append({canvas.create_rectangle(x, y, x+card_width, y+card_height, outline="black", fill=card_backs[i], width=2):(x, y, card_width, card_height)})
        x += card_width + card_gap
    y += card_height + card_gap
    x = pile_start_loc_x

print(pile)

for i, card in enumerate(cardsL1):
    print("Card", i, "is", card)


s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 61111
s.bind(('', port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print('Got connection from', addr)
   c.send(b'Thank you for connecting')
   c.close()                # Close the connection

root.mainloop()
