#!/usr/bin/python
import sys, random
from Tkinter import *
import tkFileDialog, tkMessageBox

class KanjiTrainer:

    def __init__(self, fname=''):
        self.create_gui()
        if fname:
            print 'opening'
            self.open_file(fname)
        mainloop()
        
    def create_gui(self):
        self.root = Tk()
        self.root.title('Kanji Trainer')
        
        self.make_buttons()
        self.make_menus()
        self.setup_vars()
        self.canvas = Canvas(self.root, height=400, width=400)
        self.root.bind('<Right>', self.kbd_next)
        self.canvas.pack()
        self.centre_window()

    def setup_vars(self):
        self.delay_active = False
        self.reveal_delay = -1
        self.revealed = False
        self.logic = None
        
    def make_buttons(self):
        nxt = Button(self.root, text='Next', command=self.next, state='disabled')
        nxt.pack()
        rev = Button(self.root, text='Reveal', command=self.reveal, state='disabled')
        rev.pack()
        
    def make_menus(self):
        menubar = Menu(self.root)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label='Open', command=self.open_file)
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=self.root.quit)
        menubar.add_cascade(label='File', menu=filemenu)

        optmenu = Menu(menubar, tearoff=0)
        optmenu.add_command(label='Properties', command=self.display_props)
        menubar.add_cascade(label='Options', menu=optmenu)

        self.root.config(menu=menubar)
        
    def display_props(self):
        Properties(self, self.root)
        
    def centre_window(self):
        window_height = self.root.winfo_screenheight()
        window_width = self.root.winfo_screenwidth()
        h = int(self.canvas.cget('height'))
        w = int(self.canvas.cget('width'))
        x = (window_width/2) - (w/2)
        y = (window_height/2) - (h/2)
        self.root.geometry("%dx%d+%d+%d"%(w,h,x,y))

    def open_file(self, fname=''):
        if not fname:
            f = tkFileDialog.askopenfile()
        else:
            f = open(fname, 'r')
        self.load_file(f)
     
    def load_file(self, fle):
        s = fle.read().split('\n')[:-1] # last line is empty
        kanji = []
        for k_set in s:
            kanji.append(k_set.split(' '))

        self.logic = Logic(kanji)
        self.enable_buttons()

    def enable_buttons(self):
        print 'enabling buttons'
        obj = self.root.__dict__.get('children')
        for key in obj:
            item = obj[key]
            if item.__class__.__name__ is 'Button':
                item.config(state='normal')
                                         
    def kbd_next(self, event):
        print self.delay_active, self.reveal_delay
        if not self.logic:
            return
        if self.revealed:
            self.next()
        else:
            self.reveal()

    def next(self):
        self.revealed = False
        self.display(self.canvas, self.logic.next_kanji())

    def reveal(self):
        self.revealed = True
        self.canvas.itemconfigure('hiragana', state='normal')
    
    def display(self, canvas, kanji):
        big = ('Meiryo', 90, 'normal')
        small = ('Meiryo', 18, 'normal')
        cheight = int(canvas.cget('height'))
        cwidth = int(canvas.cget('width'))
        k = kanji[0]
        disp = ''
        for h in kanji[1:]:
            disp += '%s\n'%(h)
        canvas.delete('all')
        canvas.create_text(cwidth/2, cheight/4, text=k, font=big, tags='kanji')
        canvas.create_text(cwidth/2, cheight/2 - 20, text=disp, font=small, tags='hiragana', state='hidden', anchor='n')

class Properties():
    
    def __init__(self, parent, root):
        self.parent = parent # reference to the object that spawned this
        self.prop = Toplevel(root)
        self.prop.resizable(width=False, height=False)
        
        self.app = Button(self.prop, text='Apply', command=self.apply_settings)
        self.app.grid(row=3, column=1, sticky='E')
        self.app = Button(self.prop, text='OK', command=self.ok)
        self.app.grid(row=3, column=1, sticky='E')
        self.can = Button(self.prop, text='Cancel', command=self.prop.destroy)
        self.can.grid(row=3, column=2)
        
        validate = (self.prop.register(self.validate_props), '%i')
        self.rve = Entry(self.prop, validate='key', width=5, vcmd=validate, state='disabled')
        self.rve.grid(row=1, column=1, sticky='W')
        self.revdel = Label(self.prop, text='Reveal delay:')
        self.revdel.grid(row=1, column=0, sticky='E')
        self.reveal_chk = IntVar()
        self.chk = Checkbutton(self.prop, text="Automatically reveal", variable=self.reveal_chk, command=self.rev_timer)
        self.chk.grid(row=0, columnspan=2)

        self.prop.geometry('+%d+%d'%(root.winfo_rootx(), root.winfo_rooty()))


    def rev_timer(self):
        """Called when the automatically reveal checkbox is ticked in
        order to enable or disable the entry box"""
        cur_state = str(self.rve.config()['state'][-1])
        if cur_state == 'disabled':
            self.rve.config(state='normal')
        else:
            self.rve.config(state='disabled')

    def validate_props(self, i):
        if int(i) > 2:
            return False
        return True

    def ok(self):
        self.parent.reveal_delay = self.reveal_delay
        self.parent.delay_active = self.delay_active
        self.prop.destroy()

    def apply_settings(self):
        if self.reveal_chk.get() is not 0:
            time = self.rve.get()
            try:
                int(time)
            except ValueError:
                tkMessageBox.showwarning('Set delay', 'Delay must be a number.', parent=self.prop)
                return
            self.reveal_delay = time
            self.delay_active = True
        else:
            self.reveal_delay = -1
            self.delay_active = False

class Logic():
    
    def __init__(self, kanji_list):
        self.kanji = kanji_list

    def next_kanji(self):
        return self.kanji[random.randint(0,len(self.kanji) - 1)]

def main():
    kfile = ''
    try:
        kfile = sys.argv[1]
    except IndexError:
        pass
    KanjiTrainer(fname=kfile)

if __name__ == '__main__':
    main()
    
