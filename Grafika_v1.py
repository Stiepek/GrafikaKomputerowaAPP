from tkinter import *
from functools import partial

def Bresenham(x1, y1, x2, y2):
    tab = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1
    sx = -1 if x1 > x2 else 1
    sy = -1 if y1 > y2 else 1

    if dx > dy:
        err = dx / 2.0
        while x != x2:
            tab.append((x, y))
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != y2:
            tab.append((x, y))
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy

    tab.append((x2, y2))

    return tab


def Prosta(number1, number2, number3, number4):
    w = number1.get()
    z = number2.get()
    q = number3.get()
    t = number4.get()

    x1 = int(w)
    y1 = int(z)
    x2 = int(q)
    y2 = int(t)

    nowytab = Bresenham(x1, y1, x2, y2)
    print(nowytab)

    canvas = Canvas(root,width=400,height=400)
    #canvas.create_line(x1, y1, x2, y2)
    canvas.create_line(2, 2, 2, 400, arrow=LAST)
    canvas.create_line(2, 2, 400, 2, arrow=LAST)

    for d in nowytab:
        canvas.create_line(d[0], d[1], d[0]+1, d[1], fill="#000000")
        canvas.pack(fill=BOTH, expand=1)
        canvas.place(x=20,y=60)


root = Tk()
root.title('Grafika Komputerowa APP')

number1 = StringVar()
number2 = StringVar()
number3 = StringVar()
number4 = StringVar()

content1 = Label(root,text='Wprowadź punkt początkowy    x=           y= ')
content1.place(x=10,y=10)
content2 = Label(root,text='Wprowadź punkt końcowy         x=           y= ')
content2.place(x=10,y=35)

iksy1 = Entry(root, width=3, textvariable=number1)
iksy1.place(x=195,y=10)

igrek1 = Entry(root, width=3, textvariable=number2)
igrek1.place(x=242,y=10)

iksy2 = Entry(root, width=3, textvariable=number3)
iksy2.place(x=195,y=35)

igrek2 = Entry(root, width=3, textvariable=number4)
igrek2.place(x=242,y=35)

prostaWithArguments = partial(Prosta, number1, number2, number3, number4)

action = Button(root,text='Draw',width=20, command=prostaWithArguments)
action.place(x=200,y=470)
clear = Button(root,text='Exit',width=20, command=root.destroy)
clear.place(x=50,y=470)

root.geometry("450x500")
mainloop()
