import tkinter

class Canvas(tkinter.Canvas):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.shapes_listening_for_callbacks=[]
        self.bind('<Button-1>', self.onClick)

    def create_rectangle(self, *args, **kw):
        return Rectangle(self, super().create_rectangle(*args, **kw))

    def create_text(self, *args, **kw):
        return Rectangle(self, super().create_text(*args, **kw))

    def onClick(self, event):
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
                

class Rectangle:
    __slots__=('canvas','id')
    def __init__(self, canvas, id_):
        self.canvas=canvas
        self.id=id_

    def bindToClick(self, function):
        self.canvas.shapes_listening_for_callbacks.append((self, function))

    def config(self, **kw):
        self.canvas.itemconfig(self.id, **kw)

    def bbox(self):
        return self.canvas.bbox(self.id)

if __name__=='__main__':
    window=tkinter.Tk()
    canvas=Canvas(window)
    canvas.pack()
    def say_hello(rect):
        print("The rectangle was clicked")
        rect.config(fill='blue')


    canvas.create_rectangle(80, 60, 300, 200, fill='red').bindToClick(say_hello)
    window.mainloop()
    
