#!/usr/bin/python
import sys, random
from Tkinter import *

global kanji
global canvas

def next():
    r = random.randint(0,len(kanji) - 1)
    display(canvas, r)
    
def display(canvas, index):
    big = ('Meiryo', 40, 'normal')
    small = ('Meiryo', 18, 'normal')
    k = kanji[index][0]
    disp = ''
    for h in kanji[index][1:]:
        disp += '%s\n'%(h)
    canvas.delete('all')
    canvas.create_text((10,10), text=k, font=big, tags='kanji', anchor='nw')
    canvas.create_text((100,100), text=disp, font=small, anchor='nw', tags='hiragana')

def main():
    """Runs when the file is run from the commandline
    """
    
    f = open(sys.argv[1])
    s = f.read().split('\n')[:-1] # last line is empty
    global kanji
    global canvas
    kanji = []
    for k_set in s:
        kanji.append(k_set.split(' '))
    
    m = Tk()

    wh = m.winfo_screenheight()
    ww = m.winfo_screenwidth()
    
    
    
    nxt = Button(m, text='Next', command=next)
    nxt.pack()
    c = Canvas(m, height=400, width=400)
    c.pack()
    canvas = c
    c.mainloop()

    
if __name__ == '__main__':

    main()
    
