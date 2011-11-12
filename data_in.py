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
        self.to_write = []
        self.current = [[] for i in range(4)]
    
    def init_buttons(self):
        self.next = Button(self.root, text='Next', callback=self.next_entry)
        self.next.pack()

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

    def next_entry(self):
        if is_disabled(self.one):
            self.one.config(state='enabled')
        self.to_write.append(self.current)
        self.current = [[] for i in range(4)]
        self.one.focus_set()
        
    def next_box(self, cur_box, box_no):
        self.save_box_contents(cur_box, box_no)

    def save_box_contents(self, box, box_no):
        data = box.get()
        if data != '':
            self.current[box_no].append(data)
        self.clear_box(box)
        print self.current

    def clear_box(self, box):
        box.delete(0, END)

    def is_disabled(self, obj):
        return True if obj.state == 'disabled' or obj.state == 'hidden' else False

    def init_buttons(self):
        print 'not done'

    def mouse_on_one(self, event):
        print 'mouse on one'
    
    def ret_on_one(self, event):
        print 'ret 1'
        self.next_box(self.one, 0)
        self.one.config(state='disabled')
        self.two.focus_set()
               
    def tab_on_one(self, event):
        print 'tab on first focus'
        self.next_box(self.one, 0)

    def ret_on_two(self, event):
        print 'ret on 2'
        self.save_box_contents(self.two, 1)
       
    def tab_on_two(self, event):
        print 'tab on 2'
        self.next_box(self.two, 1)
        
    def mouse_on_two(self, event):
        print 'mouse 2'

    def trd(self, event):
        print 'tab 3'
        self.next_box(self.thr, 2)
        
    def tre(self, event):
        print 'ret 3'
        self.save_box_contents(self.thr, 2)

    def thrfoc(self, event):
        print 'mouse 3'

    def fth(self, event):
        print 'tab 4'
        self.save_box_contents(self.fr, 3)
        self.next_entry()

    def fte(self, event):
        print 'ret 4'
        self.save_box_contents(self.fr, 3)


    def frfoc(self, event):
        print 'mouse 4'
        
if __name__ == '__main__':
    Reader()
