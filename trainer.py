#!/usr/bin/python
import sys
from Tkinter import *

def next():
    print 'asdfasf'

def main():
    """Runs when the file is run from the commandline
    """
    ft = ('Meiryo', 40, 'normal')
    f = open(sys.argv[1])
    s = f.read().split('\n')
    kanji = []
    for k_set in s:
        kanji.append(k_set.split(' '))
    
    m = Tk()
    nxt = Button(m, text='Next', command=next)
    nxt.pack()
    c = Canvas(m)
    c.pack()
    c.create_text((10,10), text=kanji[0][0], anchor='nw', font=ft)
    c.mainloop()
    
if __name__ == '__main__':

    main()
    
