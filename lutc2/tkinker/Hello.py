from tkinter import *

root = Tk()                             #создать окно
root1 = Tk()

def Hello(event):
    print('Hello world')

def Rirht(event):
    print('Нажми лучше на левую')

btn = Button(root,                       #родительское окно
             text="Click me",            #надпись на кнопке
             width=25, height=5,         #ширина и высота
             bg="white", fg="black")     #цвет фона и надписи


btn.bind("<Button-1>", Hello)           #при нажатии ЛКМ на кнопку вызывается функция Hello
btn.bind("<Button-3>", Rirht)
# Автоматически размещает виджеты в родительском окне. Имеет параметры side, fill, expand.
# btn.pack(side='right')
#Размещает виджеты на сетке. Основные параметры: row/column – строка/столбец в сетке,
# rowspan/columnspan – сколько строк/столбцов занимает виджет
btn.grid(row=1, column=3)
Button(root, text='2').grid(row = 1, column = 1)
Button(root, text='3').grid(row = 1, column = 2)
Button(root, text='4').grid(row = 2, column = 1, columnspan=2)

Button(root1, text = '1').place(x = 10, y = 10, width = 30)
Button(root1, text = '2').place(x = 45, y = 20, height = 15)
Button(root1, text = '__3__').place(x = 20, y = 40)

root.mainloop()                         #запускает цикл обработки событий. Все прописывать до него 


# Позволяет размещать виджеты в указанных координатах с указанными размерами. Основные параметры: x, y, width, height


root1.mainloop()


