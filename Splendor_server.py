import tkinter as tk
from Splendor_cards import *
from Splendor_card_display import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
import random
from enum import Enum
import socket
import threading
import random


root = tk.Tk()


def key(event):
    print("pressed", repr(event.char))

def callback(event):
    print("callback: clicked at", event.x, event.y)

#  This doesn't work for rectangles - they aren't tk Widgets
def global_card_click_callback(self, event, card):
    print("clicked card grid [%d, %d] at event coords (%d, %d), color %s"%(self.row, self.col, event.x, event.y, self.fill_color))
    print("Card is: ", card)

screen_objects = dict()

DISPLAY_INFO = 0
CARD_INFO = 1

overlap_delta = 0
def click_callback(event):
    print("clic_callback: clicked at", event.x, event.y)
    overlap = canvas.find_overlapping(event.x-overlap_delta, event.y-overlap_delta, event.x+overlap_delta, event.y+overlap_delta)
    if overlap is not None:
        for sprite_id in overlap:
            print("found sprite ID: ", sprite_id)
            print("Card display:", screen_objects[sprite_id][DISPLAY_INFO])
            card = screen_objects[sprite_id][CARD_INFO]
            print("Card:", card)
            #  Change the color from card back to card front for this sprite
            canvas.itemconfig(sprite_id, fill=card_fronts[card.gem_produced])


canvas = tk.Canvas(root, width=board_width, height=board_width)
root.bind("<Key>", key)
canvas.bind("<Button-1>", click_callback)
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
        id = canvas.create_rectangle(x, y, x+card_width, y+card_height, outline="black", fill=card_backs[i], width=2)
        card_disp = Card_display(id, x, y, card_width, card_height, card_backs[1], i, j)
        pile[i].append(card_disp)

        print("before popping card_stacks[%d] length is %d"%(i, len(card_stacks[i])))
        #  FLAG:  need to select the card at random
        rand_index = random.randint(0, len(card_stacks[i])-1)
        #this_card = card_stacks[i].pop()
        this_card = card_stacks[i].pop(rand_index)
        print("after popping card_stacks[%d] length is %d"%(i, len(card_stacks[i])))
        print("this card is ", this_card)

        screen_objects[id] = (card_disp, this_card)

    #  the method below doesn't work when the cards are represented by rectangles.
    #  Rectangles are not Widgets, they are just drawings - represented by an int, not an Object
        #  In theory, if I made the cards Labels or Canvases the code below would work
        #  bind a click event for this object (a placed card) with an Obj ID and a Card class instance

        x += card_width + card_gap
    y += card_height + card_gap
    x = pile_start_loc_x

print("Card pile: ", pile)

'''  Comment this out for now:
for i, card in enumerate(cardsL1):
    print("Card", i, "is", card)
'''

#  what is the difference between <1> and "<Button-1>"
#  Does it matter whether this is here or earlier in the file?
#canvas.bind("<1>", click_callback)

'''  Change the colors with a click now
# try changing colors of the cards
print("Changing color of cards")
front_colors = list(card_fronts.values())
for i in range(len(front_colors)):
    print(front_colors[i])

count = 0
for i in range(card_rows):
    for j in range(card_cols):
        print(pile[i][j])
        print("i = %d, j = %d, len(front_colors) = %d, front_colors[%d] = "%(i, j, len(front_colors),
                                                                           count % len(front_colors),
#                                                                            front_colors[i+j % len(front_colors)]
                                                                           ))
        print(front_colors[count % len(front_colors)])
        pile[i][j].fill_color = front_colors[count % len(front_colors)]
        canvas.itemconfig(pile[i][j].id, fill=pile[i][j].fill_color)
        print(pile[i][j])
        count += 1
'''

print("Printing pile:")
print(pile)

#  Socket code - comment out for now, working on graphics
"""
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
"""

root.mainloop()
