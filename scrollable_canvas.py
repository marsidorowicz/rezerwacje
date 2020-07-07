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
#
# root=Tk()
# root.geometry("1000x800")
# frame=Frame(root,width=800,height=600)
# frame.place(x=0, y=0) #.grid(row=0,column=0)
# canvas=Canvas(frame,bg='#FFFFFF',width=800,height=800,scrollregion=(0,0,1500,1500))
# frame1=Frame(canvas,width=800,height=600)
# frame1.place(x=0, y=0) #.grid(row=0,column=0)
#
#
#

connection = sqlite3.connect('r.sqlite')
cur = connection.cursor()

#
def read_from_database():
    cur.execute("SELECT * FROM reservations")
    return cur.fetchall()
#
#
# def on_mouse_wheel(event):
#
#     # automate Listbox creation
#     print("mouse wheel")
#     for i in range(10):
#         lb[i].yview("scroll", event.delta // 50, "units")
#         lb[i].xview("scroll", event.delta // 50, "units")
#     return "break"
#
#
# data = read_from_database()
#
# x = 0
# for index, dat in enumerate(data):
#     x = len(dat)
# lb = {}
# for i in range(10):
#     listbox = Listbox(frame1, width=14, relief="sunken")
#     listbox.pack(side="left", fill="y", expand=False)
#     lb[i] = listbox
#     for index, dat in enumerate(data):
#         lb[i].insert(index, dat[i])
#         lb[i].bind("<MouseWheel>", on_mouse_wheel)
#
#
#
# def on_vsb(*args):
#
#     # # automate Listbox yview method creation
#     print("vsb")
#     for i in range(10):
#         lb[i].yview(*args)
#
#
# def on_hsb(*args):
#
#     # # automate Listbox yview method creation
#     print("hsb")
#     for i in range(10):
#         print(*args)
#         canvas.xview(*args)
#
#
# hbar=Scrollbar(root,orient=HORIZONTAL, command=on_hsb)
# hbar.pack(side=BOTTOM,fill=X)
# hbar.config(command=canvas.xview)
# vbar=Scrollbar(root,orient=VERTICAL, command=on_vsb)
# vbar.pack(side=RIGHT,fill=Y)
# canvas.config(xscrollcommand=hbar.set)
# canvas.place(relx=0.01, rely=0.01, relwidth=0.980, relheight=0.980)
# w = Text(root, width=500, height=500, wrap=NONE, xscrollcommand=hbar.set)
# w.insert(END, "text111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")
# w.pack(side=LEFT, fill=X)
# root.mainloop()



# from tkinter import *
#
# master = Tk()
# master.geometry("1000x700")
# frame = Frame(master, width=850, height=500, bg="green")
# frame.place(relx=0.010, rely=0.010, relwidth=0.980, relheight=0.980)
# frame1 = Frame(master, width=850, height=500, bg="green")
# frame1.place(relx=0.010, rely=0.010, relwidth=0.980, relheight=0.980)
#
# text1 = []
# for i in range(10):
#     b = "ABC"
#     text1.append(b)
#
#
#
# # h = Scrollbar(master, orient='horizontal')
# # h.pack(side=BOTTOM, fill=X)
# # v = Scrollbar(master, orient='vertical')
# # v.pack(side=RIGHT, fill=Y)
# #
# # w = Text(frame, width=500, height=500, wrap=NONE, xscrollcommand=h.set, yscrollcommand=v.set)
# # w.insert(END, text1)
# # w.pack()
# data = read_from_database()
#
# x = 0
# for index, dat in enumerate(data):
#     x = len(dat)
# lb = {}
# for i in range(10):
#     listbox = Listbox(master, width=14, relief="sunken")
#     listbox.place()
#     h = Scrollbar(master, orient="vertical")
#     h.place(relx=0.980, rely=0.010, relwidth=0.010, relheight=0.999)
#     v = Scrollbar(master, orient="vertical")
#     lb[i] = listbox
#     for index, dat in enumerate(data):
#         lb[i].insert(index, dat[i])
#         lb[i].pack(side=LEFT, fill=Y)
#         # lb[i].bind("<MouseWheel>", on_mouse_wheel)
#
# # h.config(command=w.xview)
# # v.config(command=w.yview)
#
# mainloop()
import tkinter


class One(Frame):

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        frame = Frame(root)
        frame.pack(side = LEFT, fill = BOTH, expand = True, padx = 10, pady = 10)

        self.canvas = Canvas(frame, bg = 'pink')
        self.canvas.pack(side = RIGHT, fill = BOTH, expand = True)

        self.mailbox_frame = Frame(self.canvas, bg = 'purple')

        self.canvas_frame = self.canvas.create_window((0,0),
            window=self.mailbox_frame, anchor = NW)
        #self.mailbox_frame.pack(side = LEFT, fill = BOTH, expand = True)

        mail_scroll = Scrollbar(self.canvas, orient = "vertical",
            command = self.canvas.yview)
        mail_scroll.pack(side = RIGHT, fill = Y)

        self.canvas.config(yscrollcommand = mail_scroll.set)

        self.mailbox_frame.bind("<Configure>", self.OnFrameConfigure)
        self.canvas.bind('<Configure>', self.FrameWidth)

    def FrameWidth(self, event):
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_frame, width = canvas_width)

    def OnFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


root = tkinter.Tk()

o = One(root)
