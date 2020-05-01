import tkinter

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
                event.x = click_x - x1
                event.y = click_y - y1
                if callback(rect)=='break':
                    return 'break'


#  call this Sprite?  or SpriteWrapper?  WidgetWrapper? It covers more than Rectangles.
class WidgetWrapper:
    __slots__=('canvas','id', 'text_sprites')
    def __init__(self, canvas, id_):
        self.canvas=canvas
        self.id=id_

    def bindToClick(self, function):
        self.canvas.shapes_listening_for_callbacks.append((self, function))

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
        #  added back a "reasonble indent", trial/error values
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

    def add_text_to_widget(self, text, x, y):
        # TODO:  change x, y into optional parameters that will mimic draw_text_on_widget behavior
        bbox=self.bbox()
        canvas=self.canvas

        debug_print('rectangle_display', "inside draw_text..., type of self is: ", type(self), " bbox is: ", bbox)

        bottom_left_corner=(bbox[0]+11, bbox[3]-10) #  bbox returns 1 outside the object
                                                    #  added back a "reasonble indent", trial/error values
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


class MultiSprite:
    def __init__(self, canvas, ids):
        self.canvas=canvas
        self.ids=ids

        for sprite_id in self.ids:
            debug_print('multi_sprite', "in __repr, type of sprite_id is ", type(sprite_id), "s_id is ", sprite_id)

    def move(self, x, y):
        for sprite_id in self.ids:
            self.canvas.move(sprite_id.id, x, y)

    def __repr__(self):
        rv = ""
        for sprite_id in self.ids:
            debug_print('multi_sprite', "in __repr, type of sprite_id is ", type(sprite_id), "s_id is ", sprite_id)
            rv += str(sprite_id.id) + ", "
        return rv


active_debug_levels = (
    # 'multi_sprite',
    # 'rectangle_display',
)

def debug_print(debug_level, *args, **kwargs):
    if (debug_level in active_debug_levels):
        print(*args, **kwargs)



if __name__=='__main__':
    window=tkinter.Tk()
    canvas=Canvas(window)
    canvas.pack()
    def say_hello(rect):
        rect.move(10,0)
        print("The rectangle was clicked")
        rect.config(fill='blue')
        rect.move(10,0)


    rect1 = canvas.create_rectangle(80, 60, 300, 200, fill='red')
    rect1.bindToClick(say_hello)
    debug_print('rectangle_display', "type of rect is: ", type(rect1), " bbox is: ", rect1.bbox())
    rect1.draw_text_on_widget('Diamond', '2 VP', '1 Ruby', '1 Onyx', '1 Sapphire')

    # canvas.create_text(200, 80, text='card name').bindToClick(say_hello)
    window.mainloop()
    
