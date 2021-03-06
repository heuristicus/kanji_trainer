#!/usr/bin/python
import sys, random
from Tkinter import *
import tkFileDialog, tkMessageBox

class KanjiTrainer:

    def __init__(self, fname=''):
        self.create_gui()
        if fname:
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
        self.invert_reveal = 0
        self.logic = None
        self.after = None
        self.props = None
        self.paused = False
        self.selection_method = 'STR'

    def make_buttons(self):
        self.step_btn = Button(self.root, text='Step', command=self.step, state='disabled')
        self.step_btn.pack()
        self.pause_btn = Button(self.root, text='Pause', command=self.pause, state='disabled')
        self.pause_btn.pack()
        
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
        self.cancel_after()
        if not self.props:
            self.props = Properties(self, self.root)
        else:
            self.props.display()
        
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
        self.enable_non_context_buttons()
        
        if self.delay_active:
            self.after = self.root.after(self.reveal_delay, self.step)
        fle.close()

    def enable_all_buttons(self):
        obj = self.root.__dict__.get('children')
        for key in obj:
            item = obj[key]
            if item.__class__.__name__ is 'Button':
                item.config(state='normal')
        self.next()

    def enable_non_context_buttons(self):
        """Enable buttons which are not affected by any property being changed"""
        self.step_btn.config(state='normal')
        self.next()

    def enable_context_buttons(self):
        """Enable buttons which are affected by properties being changed"""
        self.pause_btn.config(state='normal' if self.delay_active else 'disabled')
                                        
    def kbd_next(self, event):
        self.cancel_after()
        if not self.logic:
            return
        self.step()
        
    def step(self):
        if self.revealed:
            self.next()
        else:
            self.reveal()
        if self.delay_active:
            self.after = self.start_after(self.reveal_delay, self.step)
            #self.after_start = 

    def pause(self):
        if not self.delay_active:
            return

        if not self.paused:
            self.paused = True
            self.pause_btn.config(text='Unpause')
            self.cancel_after()
        else:
            self.paused = False
            self.pause_btn.config(text='Pause')
            self.start_after(self.reveal_delay, self.step)
                
    def start_after(self, delay, callback):
        return self.root.after(delay, callback)
    
    def cancel_after(self):
        if self.after:
            self.root.after_cancel(self.after)
        
    def next(self):
        self.cancel_after()
        self.revealed = False
        self.display(self.canvas, self.logic.next_item(self.selection_method))

    def reveal(self):
        self.cancel_after()
        self.revealed = True
        if self.invert_reveal == 1:
            self.canvas.itemconfigure('kanji', state='normal')
        else:
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
        
        # State for the text to start in depends on the value set in
        # the properties
        k_state = 'hidden' if self.invert_reveal == 1 else 'normal'
        h_state = 'hidden' if self.invert_reveal == 0 else 'normal'

        canvas.create_text(cwidth/2, cheight/4, text=k, font=big, tags='kanji', state=k_state)
        canvas.create_text(cwidth/2, cheight/2 - 20, text=disp, font=small, tags='hiragana', state=h_state, anchor='n')

class Properties():
    
    def __init__(self, parent, root):
        self.parent = parent # reference to the object that spawned this
        self.root = root
        self.prop = Toplevel(root)
        self.prop.resizable(width=False, height=False)
        
        self.app = Button(self.prop, text='Apply', command=self.apply_settings)
        self.app.grid(row=3, columnspan=1, sticky='E')
        self.ok = Button(self.prop, text='OK', command=self.ok, state='disabled')
        self.ok.grid(row=3, column=1, sticky='E')
        self.can = Button(self.prop, text='Cancel', command=self.prop.destroy)
        self.can.grid(row=3, column=2, sticky='E')
        
        validate = (self.prop.register(self.validate_props), '%i')
        self.rve = Entry(self.prop, validate='key', width=5, vcmd=validate, state='disabled')
        self.rve.grid(row=1, column=1, sticky='W')
        self.revdel = Label(self.prop, text='Reveal delay:')
        self.revdel.grid(row=1, column=0, sticky='E')
        self.reveal_chk = IntVar()
        self.auto_rev_chk = Checkbutton(self.prop, text="Automatically reveal", variable=self.reveal_chk, command=self.rev_timer)
        self.auto_rev_chk.grid(row=0, columnspan=2)
        self.reveal_inv = IntVar()
        self.inv_rev = Checkbutton(self.prop, text="Show Hiragana first", variable=self.reveal_inv)
        self.inv_rev.grid(row=2, columnspan=2)

        self.display()

    def display(self):
        """Displays the properties again with the same values after
        the properties window has been closed."""
        if self.prop.state() == "withdrawn":
            self.prop.deiconify()
        else:
            self.prop.geometry('+%d+%d'%(self.root.winfo_rootx(), self.root.winfo_rooty()))

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
        self.parent.invert_reveal = self.reveal_inv.get()
        self.parent.step() # Step to the next thing to start the automatic step going
        self.parent.enable_context_buttons()
        self.prop.withdraw()

    def apply_settings(self):
        if self.reveal_chk.get() is not 0:
            time = self.rve.get()
            try:
                time = int(time)
            except ValueError:
                tkMessageBox.showwarning('Set delay', 'Delay must be a number.', parent=self.prop)
                return
            self.reveal_delay = time * 1000
            self.delay_active = True
            self.ok.config(state='normal')
        else:
            self.reveal_delay = -1
            self.delay_active = False
            self.ok.config(state='normal')

class Logic():
    
    def __init__(self, item_list):
        self.items = item_list
        # List to store number of times each item has been displayed
        self.disp_num = [0] * len(self.items)
        # Number of steps that have passed since each item was displayed
        self.last_displayed = [0] * len(self.items)
        #self.disp_num = [5,4,3,2,1]
        # Item weight
        self.weights = []
        #self.weights = [0,0,0,0,0]
        self.ptr = -1 #pointer for going through list

    def next_item(self, method):
        if method == 'STR':
            return self.straight()
        elif method == 'RND':
            return self.random_item()
        elif method == 'WTD':
            return weighted_item()

    def straight(self):
        # Goes through the list from start to end, and loops.
        self.ptr += 1
        return self.items[self.ptr % len(self.items)]



    def random_item(self):
        return self.items[random.randint(0,len(self.items) - 1)]

    def weighted_item(self):
        self.update_weights()
        #print 'rewt', self.weights
        #print self.disp_num
        # Creates a list to be used to probabilistically select data
        # items. Given the list [[1,2][3,4][5,6][7,8]], will produce
        # [2,6,12,20]. For each index sums the values of all the
        # preceding second list indices in the smaller lists.
        self.stack = [reduce(lambda x, y: x + y, self.weights[:i + 1]) for i, item in enumerate(self.weights)]
        rand = random.randint(0, sum(self.weights) - 1)
        
        disp_item = self.fgt(rand, self.stack)
        self.disp_num[disp_item] += 1

        print ' '.join([item[0] for item in self.items])
        print self.disp_num, '#'
        print self.last_displayed, 'last'
        print self.weights

        self.last_disp_update(disp_item)
        return self.items[disp_item]
    
    def last_disp_update(self, item):
        """Updates the displayed item list to reflect the new state."""
        self.last_displayed = map(lambda x: x + 1, self.last_displayed)
        self.last_displayed[item] = 0

    def fgt(self, number, lst):
        """Find the first index in the list which contains a value
        greater than the number given"""
        for i, item in enumerate(lst):
            if item > number:
                return i
        
    def update_weights(self):
        if not self.weights:
            self.weights = [1] * len(self.items)
        else:
            # Total number of times data items have been displayed
            self.total_displayed = sum(self.disp_num)
            # Update the data list, updating the weight of each data item.
            #print 'inwt', self.weights
            self.weights = map(self.display_based_update, self.disp_num)

    def display_based_update(self, disp_num):
        return self.total_displayed / (disp_num + 1)

def main():
    kfile = ''
    try:
        kfile = sys.argv[1]
    except IndexError:
        pass
    KanjiTrainer(fname=kfile)

if __name__ == '__main__':
    main()
    
