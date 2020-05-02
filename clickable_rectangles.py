import tkinter
from Splendor_cards import *
from Splendor_card_display import *
import random

class Canvas(tkinter.Canvas):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.shapes_listening_for_callbacks=[]
        self.bind('<Button-1>', self.onClick)
        # self.bind('<B1-Motion>', self.onDrag)
    '''
    ('<B1-Motion>', "'LEFT drag %3d, %3d' % (e.x, e.y)"),
    ('<B3-Motion>', "'%3d, %3d drag RIGHT' % (e.x, e.y)")
    '''

    def create_rectangle(self, *args, **kw):
        return WidgetWrapper(self, super().create_rectangle(*args, **kw))

    def create_text(self, *args, **kw):
        return WidgetWrapper(self, super().create_text(*args, **kw))

    def onClick(self, event):
        if event.x is None:
            return
        click_x, click_y = event.x, event.y
        for rect, callback in self.shapes_listening_for_callbacks:
            x1, y1, x2, y2 = self.bbox(rect.id)
            if x1 <= click_x <= x2 and y1 <= click_y <= y2:
                event.x = click_x - x1
                event.y = click_y - y1
                if callback(rect) == 'break':
                    return 'break'


    def onDrag(self, event):
        if event.x is None:
            return
        click_x, click_y = event.x, event.y
        for rect, callback in self.shapes_listening_for_callbacks:
            x1, y1, x2, y2 = self.bbox(rect.id)
            if x1 <= click_x <= x2 and y1 <= click_y <= y2:
                rect.move(event.x, event.y)


#  call this Sprite?  or SpriteWrapper?  WidgetWrapper? It covers more than Rectangles.
class WidgetWrapper:
    __slots__=('canvas','id', 'text_sprites')
    def __init__(self, canvas, id_):
        self.canvas=canvas
        self.id=id_

    def bindToClick(self, function):
        self.canvas.shapes_listening_for_callbacks.append((self, function))

    def bindToDrag(self, function):
        self.canvas.shapes_listening_for_callbacks.append((self, function))
        # FIXME:  you should be able to register click and drag events separately

    def config(self, **kw):
        self.canvas.itemconfig(self.id, **kw)

    def bbox(self):
        return self.canvas.bbox(self.id)

    def move(self, x, y):
        self.canvas.move(self.id, x, y)
        if (hasattr(self, 'text_sprites')):
            debug_print('multi_sprite', f"calling text_sprites.move({x},{y})")
            self.text_sprites.move(x, y)


    #def draw_text_on_rectangle(rect:Rectangle, *texts):
    def draw_text_on_widget(self, *texts):
        bbox=self.bbox()
        canvas=self.canvas

        debug_print('rectangle_display', "inside draw_text..., type of self is: ", type(self), " bbox is: ", bbox)

        bottom_left_corner=(bbox[0]+11, bbox[3]-10) #  bbox returns 1 outside the object
                                                    #  added back a "reasonable indent", trial/error values
        ids=[]

        for text in texts:
            new_id=canvas.create_text(bottom_left_corner, text=text, anchor='sw', font=('helvetica', 16))
            ids.append(new_id)
            bbox=new_id.bbox()

            debug_print('rectangle_display', "text loop, text is '", text, "', id is ", new_id, "type of self is: ", type(self), " bbox is: ", bbox)

            bottom_left_corner = bbox[0]+1, bbox[1]+1 # TOP left corner of the text box, which will be the bottom left corner
            # of the next textbox up.
        self.text_sprites = MultiSprite(canvas, ids)
        debug_print('multi_sprite', "MultiSprite returned ", self.text_sprites)

    def add_text_to_widget(self, text, x, y, font=('helvetica', 14), anchor='nw'):
        # TODO:  change x, y into optional parameters that will mimic draw_text_on_widget behavior
        bbox=self.bbox()
        canvas=self.canvas

        debug_print('widget_add_text', f"text: '{text}', ({x}, {y})")

        top_left_corner = (bbox[0]+1, bbox[1]+1)    #  bbox returns 1 outside the object
        position = (bbox[0]+1+x, bbox[1]+1+y)       #  bbox returns 1 outside the object

        if hasattr(self, 'text_sprites'):
            ids = self.text_sprites.get_ids()
            debug_print('widget_add_text', f"text_sprites exists ids: {ids}")
        else:
            ids = []
            debug_print('widget_add_text', f"text_sprites exists ids: {ids}")

        new_id=canvas.create_text(position, text=text, anchor=anchor, font=font)
        ids.append(new_id)
        self.text_sprites = MultiSprite(canvas, ids)
        debug_print('multi_sprite', "MultiSprite returned ", self.text_sprites)


class MultiSprite:
    def __init__(self, canvas, ids):
        self.canvas=canvas
        self.ids=ids

        for sprite_id in self.ids:
            debug_print('multi_sprite', "in __repr, type of sprite_id is ", type(sprite_id), "s_id is ", sprite_id)

    def move(self, x, y):
        for sprite_id in self.ids:
            self.canvas.move(sprite_id.id, x, y)

    def get_ids(self):
        return self.ids

    def __repr__(self):
        rv = ""
        for sprite_id in self.ids:
            debug_print('multi_sprite', "in __repr, type of sprite_id is ", type(sprite_id), "s_id is ", sprite_id)
            rv += str(sprite_id.id) + ", "
        return rv

class Card:
    def __init__(self, data, canvas, x, y):
        self.data = data
        self.canvas = canvas
        self.x = x
        self.y = y
        #  will get a widget id in show()
        self.show()

    def show(self):
        x, y = self.x, self.y
        my_card_height = card_height * 0.6
        card_widget = self.canvas.create_rectangle(x, y, x + card_width, y + my_card_height,
                                                   outline="black", fill=card_fronts[self.data.gem_produced], width=2)
        # FIXME:  There is a way to tell the height of a font programmatically.  Can have
        #  the code here center the font in its region of the card without guess&check
        if (self.data.victory_points > 0):
            card_widget.add_text_to_widget(str(self.data.victory_points), edge_offset * 2, edge_offset,
                                           font=('helvetica', 32))
        card_widget.add_text_to_widget(self.data.gem_produced, card_width - 2 * edge_offset, 2 * edge_offset,
                                       font=('helvetica', 20), anchor='ne')
        #  Used to have victory point and card type location reversed.  Current way matches board game.
        # rect2.add_text_to_widget('Diamond', edge_offset, edge_offset*2, font=('helvetica', 20))
        # rect2.add_text_to_widget('2', card_width * 3 / 4, edge_offset, font=('helvetica', 32))

        self.widget = card_widget

        #  Now fill in the card cost information on the card - x, y are now card-relative, not canvas-relative
        #  FIXME:  wouldn't hurt to make this its own method
        x, y = cost_start_x, cost_start_y
        debug_print('show', "data is: ", self.data, "cost is: ", self.data.cost)
        for name, value in self.data.cost.items():
            #  this did not work - the field width is font dependent; have to use
            #  fixed width fonts for this.  Instead will put the # before the name
            # rect2.add_text_to_widget(f"{name:{cost_field_width}s}:{value:2d}", x, y)
            #  only display a resource if this card has a cost for that resource
            if (value > 0):
                card_widget.add_text_to_widget(f"{value:2d} {name}", x, y)
                debug_print('show', f"placing value [{name}, {value}] at location ({x},{y})")

            # increment location of position either way, so the cost for each resource is always in the same location
            y += 20

            # wrap the resource cost list when it gets too close to the bottom of the card
            #  FIXME:  remove magic numbers when the look of the thing is right
            if (y > 0.8 * my_card_height):
                y = cost_start_y
                x += card_width / 2 + edge_offset



active_debug_levels = (
    # 'multi_sprite',
    # 'rectangle_display',
    # 'widget_add_text',
    'show',
    'card_pile',
    'drag_event',
)
DEBUG_SEARCH_HERE = active_debug_levels

def debug_print(debug_level, *args, **kwargs):
    if (debug_level in active_debug_levels):
        print(debug_level, ":", *args, **kwargs)



if __name__=='__main__':
    window=tkinter.Tk()
    canvas=Canvas(window, width=board_width*1.5, height=board_height*1)
    canvas.pack()
    def say_hello(rect):
        rect.move(10,0)
        print("The rectangle was clicked")
        rect.config(fill='blue')
        rect.move(10,0)

    def drag_event(event):
        debug_print('drag_event', f"drag event at coords ({event.x}, {event.y})")

    # messing about with what looks good
    my_card_height = card_height * 0.6

    card_x, card_y = card_start_x, card_start_y = 80, 60
    # rect1 = canvas.create_rectangle(card_x, card_y, 300, 200, fill='red')
    rect1 = canvas.create_rectangle(card_x, card_y, card_x + card_width, card_y + my_card_height, fill='red')
    rect1.bindToClick(say_hello)
    debug_print('rectangle_display', "type of rect is: ", type(rect1), " bbox is: ", rect1.bbox())
    rect1.draw_text_on_widget('Diamond', '2 VP', '1 Ruby', '1 Onyx', '1 Sapphire')

    # rect2 = canvas.create_rectangle(380, 260, 600, 400, fill='yellow')
    i=0
    card_gap = card_width // 8
    # TODO:  Could have a ternary operator here that increments y automatically when x is incremented over a line width
    x, y = card_x + card_width + card_gap, card_y  # + (card_height + card_gap) if card_x > board_width # FIXME
    rect2 = canvas.create_rectangle(x, y, x + card_width, y + my_card_height, outline="black", fill=card_backs[i], width=2)
    # TODO:  There is a way to tell the height of a font programmatically.  Can have
    #  the code here center the font in its region of the card without guess&check
    rect2.add_text_to_widget('2', edge_offset*2, edge_offset, font=('helvetica', 32))
    rect2.add_text_to_widget('Diamond', card_width - 2 * edge_offset, 2 * edge_offset, font=('helvetica', 20), anchor='ne')
    # rect2.add_text_to_widget('Diamond', edge_offset, edge_offset*2, font=('helvetica', 20))
    # rect2.add_text_to_widget('2', card_width * 3 / 4, edge_offset, font=('helvetica', 32))

    card = cardsL1[5]
    cost_start_x, cost_start_y = edge_offset // 2, my_card_height // 2
    cost_field_width = 9       #  a guess...
    x, y = cost_start_x, cost_start_y
    for name, value in card.cost.items():
        #  this did not work - the field width is font dependent; have to use
        #  fixed width fonts for this.  Instead will put the # before the name
        # rect2.add_text_to_widget(f"{name:{cost_field_width}s}:{value:2d}", x, y)
        if (value > 0):
            rect2.add_text_to_widget(f"{value:2d} {name}", x, y)
        y += 20
        if (y > 0.8 * my_card_height):
            y = cost_start_y
            x += card_width / 2 + edge_offset

    rect2.bindToClick(say_hello)

    # put all the above in a method of the new Card class - give it a try:

    #  Quick test:
    '''
    Card(cardsL2[14], canvas, x, y)
    x += card_width + card_gap
    Card(cardsL1[5], canvas, x, y)
    '''

    #  start at left edge, one row down from whatever above did
    pile_start_loc_x, pile_start_loc_y = card_start_x, card_y + my_card_height * 1.2
    x, y = pile_start_loc_x, pile_start_loc_y
    pile = [[] for i in range(card_rows)] # TODO:  how do I declare this?  Do I need to?


    def row_to_y(row):
        return row * (my_card_height + card_gap) + pile_start_loc_y # FIXME: fix my_card_height stuff
    def col_to_x(col):
        return col * (card_width + card_gap) + pile_start_loc_x
    # Display the up cards on the table
    for i in range(card_rows):
        for j in range(card_cols):
            rand_index = random.randint(0, len(card_stacks[i]) - 1)
            this_card = card_stacks[i].pop(rand_index)
            debug_print('create_card_stack', "after popping card_stacks[%d] length is %d" % (i, len(card_stacks[i])))
            debug_print('create_card_stack', "this card is ", this_card)

            Card(this_card, canvas, col_to_x(j), row_to_y(i))

            pile[i].append(this_card)

            #        screen_objects[id] = (card_disp, this_card)

            #  the method below doesn't work when the cards are represented by rectangles.
            #  Rectangles are not Widgets, they are just drawings - represented by an int, not an Object
            #  In theory, if I made the cards Labels or Canvases the code below would work
            #  bind a click event for this object (a placed card) with an Obj ID and a Card class instance

    debug_print('card_pile', "Card pile: ", pile)

    # card_disp = Card_display(id, x, y, card_width, card_height, card_backs[1], i, j)
    #
    # canvas.create_text(200, 80, text='card name').bindToClick(say_hello)
    window.mainloop()
    
