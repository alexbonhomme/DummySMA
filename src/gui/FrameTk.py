'''
Created on 17 janv. 2014

@author: Alexandre Bonhomme
'''

from Tkinter import Tk, Canvas, NW


class FrameTk(object):

    def __init__(self, height, width, box_size, title = "Tk", bg = None):
        self.BOX_SIZE = box_size

        self.main = Tk()
        self.main.wm_title(title)
        self.canvas = Canvas(self.main, height = height, width = width, bg = bg)
        self.canvas.pack()

    def run(self):
        self.main.mainloop()

    def repeat(self, end, timeMillis, callback):
        def _repeat(end, time, func):
            if end > 0:
                end -= 1
                self.repeat(end, time, func)
                func()
                self._draw()

        self.canvas.after(timeMillis, _repeat, end, timeMillis, callback)

    def after(self, timeMillis, callback):
        def _callback(time, func):
            self.after(time, func)
            func()
            self._draw()

        self.canvas.after(timeMillis, _callback, timeMillis, callback)

    def _draw(self):
        pass

    def drawTkImage(self, x, y, tkimage):
        self.canvas.create_image(x, y, anchor = NW, image = tkimage)

    def drawText(self, x, y, text):
        self.canvas.create_text(x, y, anchor = NW, fill = 'white', text = text)
