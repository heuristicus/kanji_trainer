#! /usr/bin/python
from Tkinter import *

class Reader():

## Make entered data appear to the right or left of the text boxes so the user can see it
## make it so that the number of boxes that appear are pre specified and the user can select how many they want. Automatically initialise callback methods and stuff using lambda functions
## 
    
    def __init__(self):
        self.root = Tk()
        self.root.title('datain')

        self.init_vars()
        self.init_boxes()
        self.init_buttons()

        mainloop()
        
    def init_vars(self):
        self.to_write = [[] for i in range(4)]
    
    def init_boxes(self):
        self.one = Entry(self.root)
        self.one.bind('<Tab>', self.tab_on_one)
        self.one.bind('<Return>', self.ret_on_one)
        self.one.bind('<Button-1>', self.mouse_on_one)
        self.one.pack()
        
        self.two = Entry(self.root)
        self.two.bind('<Tab>', self.tab_on_two)
        self.two.bind('<Return>', self.ret_on_two)
        self.two.bind('<Button-1>', self.mouse_on_two)
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

    def is_disabled(self, obj):
        return True if obj.state == 'disabled' or obj.state == 'hidden' else False

    def init_buttons(self):
        print 'not done'

    def mouse_on_one(self, event):
        print 'mouse on one'
    
    def ret_on_one(self, event):
        print 'ret 1'
        self.to_write[0] = self.one.get()
        self.one.config(state='disabled')
        print self.to_write
        
    def tab_on_one(self, event):
        print 'tab on first focus'

    def ret_on_two(self, event):
        print 'ret on 2'
        self.to_write[1].append(self.two.get())
        self.two.delete(0, END)
        print self.to_write

    def tab_on_two(self, event):
        print 'tab on 2'
        
    def mouse_on_two(self, event):
        print 'mouse 2'

    def trd(self, event):
        print 'tab 3'
        
    def tre(self, event):
        print 'ret 3'
        self.to_write[2].append(self.thr.get())
        self.thr.delete(0, END)
        print self.to_write

    def thrfoc(self, event):
        print 'mouse 3'

    def fth(self, event):
        print 'tab 4'

    def fte(self, event):
        print 'ret 4'
        self.to_write[3].append(self.fr.get())
        self.fr.delete(0, END)
        print self.to_write

    def frfoc(self, event):
        print 'mouse 4'


if __name__ == '__main__':
    Reader()
