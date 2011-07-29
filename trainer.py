#!/usr/bin/python
import sys, random
from Tkinter import *

global kanji
global canvas

class KanjiTrainer:

    def __init__(self, klist):    
        self.root = Tk()
        self.root.title('Kanji Trainer')
        nxt = Button(self.root, text='Next', command=self.next)
        nxt.pack()
        shw = Button(self.root, text='Reveal', command=self.reveal)
        shw.pack()
        self.canvas = Canvas(self.root, height=400, width=400)
        self.canvas.pack()
        self.centre_window()
        self.canvas.mainloop()

    def centre_window(self):
        window_height = self.root.winfo_screenheight()
        window_width = self.root.winfo_screenwidth()
        h = int(self.canvas.cget('height'))
        w = int(self.canvas.cget('width'))
        x = (window_width/2) - (w/2)
        y = (window_height/2) - (h/2)
        self.root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    
    def next(self):
        self.display(self.canvas, random.randint(0,len(kanji) - 1))

    def reveal(self):
        self.canvas.itemconfigure('hiragana', state='normal')
    
    def display(self, canvas, index):
        big = ('Meiryo', 90, 'normal')
        small = ('Meiryo', 18, 'normal')
        cheight = int(canvas.cget('height'))
        cwidth = int(canvas.cget('width'))
        k = kanji[index][0]
        disp = ''
        for h in kanji[index][1:]:
            disp += '%s\n'%(h)
            canvas.delete('all')
            canvas.create_text(cwidth/2, cheight/4, text=k, font=big, tags='kanji')
            canvas.create_text(cwidth/2, 2*cheight/3, text=disp, font=small, tags='hiragana', state='hidden')

if __name__ == '__main__':
    s = open(sys.argv[1]).read().split('\n')[:-1] # last line is empty
    kanji = []
    for k_set in s:
        kanji.append(k_set.split(' '))
    KanjiTrainer(kanji)
