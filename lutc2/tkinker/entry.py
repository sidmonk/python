from tkinter import *
from tkinter.messagebox import showinfo

def reply(name):
    if name:
        showinfo(title='Reply', message=f'Hello, {name}')
        ent.delete(first=0, last=END)

top = Tk()
Label(top, text="Enter your name:").pack(side=TOP)
ent = Entry(top)
ent.pack(side=TOP)
btn = Button(top, text="Submit", command=(lambda: reply(ent.get())))
btn.pack(side=TOP)

top.mainloop()