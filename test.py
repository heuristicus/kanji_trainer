#!/usr/bin/python
from Tkinter import *

class Test():
    
    def __init__(self):
        self.root = Tk()
        self.entry = Entry(self.root, validate='key', vcmd=self.validate)
        self.entry.pack()
        mainloop()
        
    def validate(self):
        print 'validating'
        value = self.entry.get()
        self.entry.delete(0)
        return True

if __name__ == '__main__':
    Test()
