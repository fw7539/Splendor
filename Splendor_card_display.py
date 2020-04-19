"""
    Splendor Card display information

    This file is intended to be customized for different python graphics packages
    (e.g. tkinter or pygame)

    To be imported by both server and client
"""
#  Constants
board_height = 800
board_width = 800

card_height = 150
card_width = 100
card_cols = 4
card_rows = 3
card_gap = 10

#  pile[i].append((id, x, y, card_width, card_height, card_backs[i], i, j))

class Card_display():
    def __init__(self, id, x, y, card_width, card_height, fill_color, row=-1, col=-1):
        self.id = id
        self.x = x
        self.y = y
        self.card_width = card_width
        self.card_height = card_height
        self.fill_color = fill_color
        self.row = row
        self.col = col
        #  need a self.id as well

    def __repr__(self):
        return f'Card_display(id={self.id}, x={self.x}, y={self.y}, card_width={self.card_width}, ' \
               f'card_height={self.card_height}, fill_color={self.fill_color}, row={self.row}, col={self.col})'

    def card_click_callback(self, event):
        print("clicked card grid [%d, %d] at event coords (%d, %d), color %s"%(self.row, self.col, event.x, event.y, self.fill_color))
