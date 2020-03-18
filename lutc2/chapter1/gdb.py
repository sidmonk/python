from tkinter import *
from tkinter.messagebox import showerror
import shelve
# from persona import *
fields = ('name', 'job', 'pay')
shelvename = 'per'
entries = {}


def createWindow():
    window = Tk()
    global entries
    window.title('People shelve')
    fr = Frame(window)
    fr.pack()
    for ix, field in enumerate(('key', ) + fields):
        labl = Label(fr, text=field)
        ent = Entry(fr)
        labl.grid(row=ix, column=0)
        ent.grid(row=ix, column=1)
        entries[field] = ent
    Button(window, text='Find', command=find).pack(side=LEFT)
    Button(window, text='Update', command = update).pack(side=LEFT)
    Button(window, text='Quit', command=window.quit).pack(side=RIGHT)
    return window


def find():
    key = entries['key'].get()
    try:
        record = db[key]
    except:
        showerror(title='Error', message='Нет такого')
    else:
        for field in fields:
            entries[field].delete(0, END)
            entries[field].insert(0, repr(getattr(record, field)))

def update():
    key = entries['key'].get()
    if key in db:
        record = db[key]
    else:
        record = Person(name='?')
    for field in fields:
        setattr(record, field, eval(entries[field].get()))
    db[key] = record


with shelve.open(shelvename) as db:
    window = createWindow()
    window.mainloop()