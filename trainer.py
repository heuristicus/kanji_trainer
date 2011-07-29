#!/usr/bin/python
import sys, random
from Tkinter import *

global kanji
global canvas

def next():
    r = random.randomint(0,len(kanji))
    print r
    display(canvas, r)
    

def display(canvas, index):
    #c.create_text((10,10), text=kanji[index][0], font=ft, tags='kanji')
    for h in kanji[index][1:]:
        print h

def main():
    """Runs when the file is run from the commandline
    """
    ft = ('Meiryo', 40, 'normal')
    f = open(sys.argv[1])
    s = f.read().split('\n')
    global kanji
    global canvas
    kanji = []
    for k_set in s:
        kanji.append(k_set.split(' '))
    
    m = Tk()
    nxt = Button(m, text='Next', command=next)
    nxt.pack()
    c = Canvas(m)
    c.pack()
    canvas = c
    c.create_text((10,10), text=kanji[0][0], font=ft, tags='kanji')
    c.mainloop()
    
if __name__ == '__main__':

    main()
    
