from tkinter import *
from tkinter.messagebox import showinfo
from numpy import *
n = 5


class field(Button):
    def __init__(self):
        Button.__init__(self, text=' ', width=2, height=1, command=self.press)

    __chars = ['x', '0']

    def press(self):
        if self['text'] == ' ':
            curr_char = field.__chars.pop(0)
            self['text'] = curr_char
            field.__chars.append(curr_char)
        check(all_fields)


window = Tk()
def newgame(n):
    global all_fields
    all_fields = [[field() for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            all_fields[i][j].grid(row=i, column=j)

def findwin(strings):
    for s in strings:
        if s.find('xxx') != -1:
            showinfo(title='endgame', message="'x' win!")
            newgame(n)
        elif s.find('000') != -1:
            showinfo(title='endgame', message="'0' win!")
            newgame(n)

def check(all_fields):
    matrix = array([[el['text'] for el in i] for i in all_fields])
    findwin([''.join([s for s in i]) for i in matrix])
    findwin([''.join([s for s in i]) for i in matrix.transpose()])
    findwin([''.join([s for s in i]) for i in [matrix.diagonal(i) for i in range(3 - n, n - 3 + 1)]])
    findwin([''.join([s for s in i]) for i in [matrix[:,::-1].diagonal(i) for i in range(3 - n, n - 3 + 1)]])


newgame(n)
window.mainloop()
