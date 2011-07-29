#!/usr/bin/python
import sys, Tkinter

def ask_question():
    """Asks a question of the user about a specific kanji
    """
    print 'bb'


def main():
    """Runs when the file is run from the commandline
    """
    f = open(sys.argv[1])
    s = f.read().split('\n')
    print s
    
    
    
if __name__ == '__main__':

    main()
    
