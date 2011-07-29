#!/usr/bin/python
import sys, random
from Tkinter import *
import tkFileDialog

class KanjiTrainer:

    def __init__(self, fname=''):
        self.create_gui()
        if fname:
            self.load_file(fname)
        
    def create_gui(self):
        self.root = Tk()
        self.root.title('Kanji Trainer')
        self.make_buttons()
        self.make_menus()
        self.canvas = Canvas(self.root, height=400, width=400)
        self.canvas.pack()
        self.centre_window()
        mainloop()

    def make_buttons(self):
        nxt = Button(self.root, text='Next', command=self.next)
        nxt.pack()
        rev = Button(self.root, text='Reveal', command=self.reveal)
        rev.pack()

    def make_menus(self):
        menubar = Menu(self.root)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label='Open', command=self.open_file)
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=self.root.quit)
        menubar.add_cascade(label='File', menu=filemenu)

        optmenu = Menu(menubar, tearoff=0)
        optmenu.add_command(label='Properties', command=self.set_props)
        menubar.add_cascade(label='Options', menu=optmenu)

        self.root.config(menu=menubar)
        
    def set_props(self):
        print 'props'

    def centre_window(self):
        window_height = self.root.winfo_screenheight()
        window_width = self.root.winfo_screenwidth()
        h = int(self.canvas.cget('height'))
        w = int(self.canvas.cget('width'))
        x = (window_width/2) - (w/2)
        y = (window_height/2) - (h/2)
        self.root.geometry("%dx%d+%d+%d"%(w,h,x,y))

    def open_file(self):
        f = tkFileDialog.askopenfile()
        self.load_file(f)

    def load_file(self, fle):
        s = fle.read().split('\n')[:-1] # last line is empty
        self.kanji = []
        for k_set in s:
            print k_set
            self.kanji.append(k_set.split(' '))
        
    def next(self):
        self.display(self.canvas, random.randint(0,len(self.kanji) - 1))

    def reveal(self):
        self.canvas.itemconfigure('hiragana', state='normal')
    
    def display(self, canvas, index):
        big = ('Meiryo', 90, 'normal')
        small = ('Meiryo', 18, 'normal')
        cheight = int(canvas.cget('height'))
        cwidth = int(canvas.cget('width'))
        k = self.kanji[index][0]
        disp = ''
        for h in self.kanji[index][1:]:
            disp += '%s\n'%(h)
        canvas.delete('all')
        canvas.create_text(cwidth/2, cheight/4, text=k, font=big, tags='kanji')
        canvas.create_text(cwidth/2, cheight/2 - 20, text=disp, font=small, tags='hiragana', state='hidden', anchor='n')

def main():
    kfile = ''
    try:
        kfile = sys.argv[1]
    except IndexError:
        pass
    
    KanjiTrainer(kfile)

if __name__ == '__main__':
    main()
    
