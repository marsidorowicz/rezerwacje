# from tkinter import *
# root=Tk()
# root.geometry("600x600")
# frame=Frame(root)
# frame.pack(expand=True) #.grid(row=0,column=0)
# canvas=Canvas(frame,bg='#FFFFFF',width=800,height=800,scrollregion=(0,0,300,300))
# hbar=Scrollbar(canvas,orient=HORIZONTAL)
# hbar.pack(side=BOTTOM,fill=X)
# hbar.config(command=canvas.xview)
# vbar=Scrollbar(canvas,orient=VERTICAL)
# vbar.pack(side=RIGHT,fill=Y)
# vbar.config(command=canvas.yview)
# canvas.config(width=300,height=300)
# canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
# canvas.pack(side=LEFT,expand=True,fill=BOTH)
#
# text1 = []
# for i in range(1000):
#     b = "ABC"
#     text1.append(b)
#
# w = Text(canvas, width=900, height=900, wrap=NONE, xscrollcommand=hbar.set, yscrollcommand=vbar.set)
# w.insert(END, text1)
# w.pack()
#
#
# root.mainloop()

from tkinter import *
import  sqlite3

root=Tk()
frame=Frame(root,width=300,height=300)
frame.pack(expand=True, fill=BOTH) #.grid(row=0,column=0)
canvas=Canvas(frame,bg='#FFFFFF',width=500,height=500,scrollregion=(0,0,1500,1500))




connection = sqlite3.connect('r.sqlite')
cur = connection.cursor()


def read_from_database():
    cur.execute("SELECT * FROM reservations")
    return cur.fetchall()


def on_mouse_wheel(event):

    # automate Listbox creation
    for i in range(10):
        lb[i].yview("scroll", event.delta // 50, "units")
    return "break"


data = read_from_database()

x = 0
for index, dat in enumerate(data):
    x = len(dat)
print(x)
lb = {}
for i in range(10):
    listbox = Listbox(canvas, width=14, relief="sunken")
    listbox.pack(side="left", fill="y", expand=False)
    lb[i] = listbox
    for index, dat in enumerate(data):
        lb[i].insert(index, dat[i])
        lb[i].bind("<MouseWheel>", on_mouse_wheel)



def on_vsb(*args):

    # # automate Listbox yview method creation
    for i in range(10):
        lb[i].yview(*args)


hbar=Scrollbar(frame,orient=HORIZONTAL)
hbar.pack(side=BOTTOM,fill=X)
hbar.config(command=canvas.xview)
vbar=Scrollbar(canvas,orient=VERTICAL, command=on_vsb)
vbar.pack(side=RIGHT,fill=Y)
canvas.config(width=500,height=500)
canvas.config(xscrollcommand=hbar.set)
canvas.pack(side=LEFT,expand=True,fill=BOTH)
root.mainloop()