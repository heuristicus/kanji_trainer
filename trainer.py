#!/usr/bin/python
import sys, random
from Tkinter import *

global kanji
global canvas

class KanjiTrainer:

    def __init__(self, klist):
        
    
        m = Tk()
        m.title('Kanji Trainer')
        
        wh = m.winfo_screenheight()
        ww = m.winfo_screenwidth()
        
        w = 400
        h = 400
        x = (ww/2) - (w/2)
        y = (wh/2) - (h/2)
        print x, y
        
        m.geometry("%dx%d+%d+%d"%(w,h,x,y))
    
    
        nxt = Button(m, text='Next', command=self.next)
        nxt.pack()
        shw = Button(m, text='Reveal', command=self.reveal)
        shw.pack()
        c = Canvas(m, height=400, width=400)
        c.pack()
        
        self.canvas = c
        c.mainloop()

    def next(self):
        r = random.randint(0,len(kanji) - 1)
        self.display(self.canvas, r)

    def reveal(self):
        self.canvas.itemconfigure('hiragana', state='normal')
    
    def display(self, canvas, index):
        big = ('Meiryo', 90, 'normal')
        small = ('Meiryo', 18, 'normal')
        k = kanji[index][0]
        disp = ''
        for h in kanji[index][1:]:
            disp += '%s\n'%(h)
            canvas.delete('all')
            canvas.create_text((int(canvas.cget('width'))/2,int(canvas.cget('height'))/4), text=k, font=big, tags='kanji')
            canvas.create_text((int(canvas.cget('width'))/2,2*int(canvas.cget('height'))/3), text=disp, font=small, tags='hiragana', state='hidden')

if __name__ == '__main__':
    f = open(sys.argv[1])
    s = f.read().split('\n')[:-1] # last line is empty
    kanji = []
    for k_set in s:
        kanji.append(k_set.split(' '))
            
    KanjiTrainer(kanji)
