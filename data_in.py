#! /usr/bin/python
from Tkinter import *

class Reader():
    
    def __init__(self):
        self.root = Tk()
        self.root.title('datain')

        self.init_boxes()
        self.init_buttons()

        mainloop()
        
    def init_boxes(self):
        self.one = Entry(self.root)
        self.one.bind('<Tab>', self.fst)
        self.one.bind('<Button-1>', self.onefoc)
        self.one.pack()
        
        self.two = Entry(self.root)
        self.two.bind('<Tab>', self.snd)
        self.two.bind('<Return>', self.srt)
        self.two.bind('<Button-1>', self.twofoc)
        self.two.pack()

        self.thr = Entry(self.root)
        self.thr.bind('<Tab>', self.trd)
        self.thr.bind('<Return>', self.tre)
        self.thr.bind('<Button-1>', self.thrfoc)
        self.thr.pack()

        self.fr = Entry(self.root)
        self.fr.bind('<Tab>', self.fth)
        self.fr.bind('<Return>', self.fte)
        self.fr.bind('<Button-1>', self.frfoc)
        self.fr.pack()

    def init_buttons(self):
        print 'not done'

    def onefoc(self, event):
        print 'mouse on one'
    
    def fst(self, event):
        print 'tab on first focus'

    def srt(self, event):
        print 'ret on 2'

    def snd(self, event):
        print 'tab on 2'
        
    def twofoc(self, event):
        print 'mouse 2'

    def trd(self, event):
        print 'tab 3'
        
    def tre(self, event):
        print 'ret 3'

    def thrfoc(self, event):
        print 'mouse 3'

    def fth(self, event):
        print 'tab 4'

    def fte(self, event):
        print 'ret 4'

    def frfoc(self, event):
        print 'mouse 4'


if __name__ == '__main__':
    Reader()
