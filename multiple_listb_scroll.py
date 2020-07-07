# from tkinter import *
#
#
# class mainWin:
#     def __init__(self, root):
#         self.root = root
#         self.createWidgets()
#         return None
#
#     def createWidgets(self):
#         self.l1 = Listbox(self.root)
#         self.l1.pack(side=LEFT)
#         self.l2 = Listbox(self.root)
#         self.l2.pack(side=LEFT)
#         for count in range(42):
#             self.l1.insert(END, "l1 " + str(count))
#             self.l2.insert(END, "l2 " + str(count))
#
#         s = Scrollbar(self.root, orient=VERTICAL, command=self.scrollBoth)
#         s.pack(side=LEFT, fill=Y)
#         self.l1.configure(yscrollcommand=s.set)
#         return None
#
#     def scrollBoth(self, *args):
#         apply(self.l1.yview, args)
#         apply(self.l2.yview, args)
#         return None
#
#
# def main():
#     root = Tk()
#     mainWin(root)
#     root.mainloop()
#     return None
#
#
# if __name__ == "__main__":
#     main()

# from tkinter import *
# import tkinter
#
# root=Tk()
# frame1=Frame(root,width=1000,height=1000, bg="green")
# frame1.pack(side=LEFT, expand=True, fill="both")
# canvas= tkinter.Canvas(frame1,bg='yellow',width=900,height=900,scrollregion=(0,0,1000,1000))
# canvas.pack(side=LEFT,expand=True,fill=BOTH)
# hbar=Scrollbar(root,orient=HORIZONTAL)
# hbar.pack(side=BOTTOM,fill=X)
# hbar.config(command=canvas.xview)
# vbar=Scrollbar(root,orient=VERTICAL)
# vbar.pack(side=RIGHT,fill=Y)
# # vbar.config(command=canvas.yview)
# # # # canvas.config(width=300,height=300)
# # # canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set, bg="black", height=500, width=500)
# #
# #
# # root.mainloop()
#
# from tkinter import *
# import tkinter as tk
#
# class MainWindow(Frame):
#     def __init__(self, parent):
#         super().__init__()
#         self.pack(expand=Y,fill=BOTH)
#
#         canvas = tk.Canvas(parent, width=150, height=150)
#         canvas.create_oval(10, 10, 20, 20, fill="red")
#         canvas.create_oval(200, 200, 220, 220, fill="blue")
#         canvas.grid(row=0, column=0)
#
#         scroll_x = tk.Scrollbar(parent, orient="horizontal", command=canvas.xview)
#         scroll_x.grid(row=1, column=0, sticky="ew")
#
#         scroll_y = tk.Scrollbar(parent, orient="vertical", command=canvas.yview)
#         scroll_y.grid(row=0, column=1, sticky="ns")
#
#         canvas.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
#
# root = MainWindow()
# root.mainloop()

# Python Program to make a scrollable frame
# using Tkinter

from tkinter import *


# class ScrollBar:
#
#     # constructor
#     def __init__(self):
#         # create root window
#         root = Tk()
#         root.geometry("900x600+300+300")
#         frame = Frame(root, width=850, height=500, bg="green")
#         frame.pack(side="left", fill=BOTH, expand=True)
#
#         # create a horizontal scrollbar by
#         # setting orient to horizontal
#         h = Scrollbar(frame, orient='horizontal')
#
#         # attach Scrollbar to root window at
#         # the bootom
#         h.pack(side=BOTTOM, fill=X)
#
#         # create a vertical scrollbar-no need
#         # to write orient as it is by
#         # default vertical
#         v = Scrollbar(frame, orient='vertical')
#
#         # attach Scrollbar to root window on
#         # the side
#         v.pack(side=RIGHT, fill=Y)
#
#         # create a Text widget with 15 chars
#         # width and 15 lines height
#         # here xscrollcomannd is used to attach Text
#         # widget to the horizontal scrollbar
#         # here yscrollcomannd is used to attach Text
#         # widget to the vertical scrollbar
#         t = Text(frame, width=15, height=15, wrap=NONE,
#                  xscrollcommand=h.set,
#                  yscrollcommand=v.set)
#
#         # insert some text into the text widget
#         for i in range(20):
#             t.insert(END, "this is some text\n")
#
#         # attach Text widget to root window at top
#         t.pack(side=TOP, fill=X)
#
#         # here command represents the method to
#         # be executed xview is executed on
#         # object 't' Here t may represent any
#         # widget
#         h.config(command=t.xview)
#
#         # here command represents the method to
#         # be executed yview is executed on
#         # object 't' Here t may represent any
#         # widget
#         v.config(command=t.yview)
#
#         # the root window handles the mouse
#         # click event
#         root.mainloop()
#
#     # create an object to Scrollbar class
#
#
# s = ScrollBar()

from tkinter import *

master = Tk()
master.geometry("1000x700")
frame = Frame(master, width=850, height=500, bg="green")
frame.place(relx=0.010, rely=0.010, relwidth=0.980, relheight=0.980)

text1 = []
for i in range(1000):
    b = "ABC"
    text1.append(b)


h = Scrollbar(master, orient='horizontal')
h.pack(side=BOTTOM, fill=X)
v = Scrollbar(master, orient='vertical')
v.pack(side=RIGHT, fill=Y)

w = Text(frame, width=500, height=500, wrap=NONE, xscrollcommand=h.set, yscrollcommand=v.set)
w.insert(END, text1)
w.pack()

h.config(command=w.xview)
v.config(command=w.yview)

mainloop()
