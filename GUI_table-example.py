import sqlite3
import tkinter
from tkinter import *


class Records:
    # class created to see records that have been previously inputted#
    def __init__(self, master):
        self.master = master
        self.master.geometry('250x200+100+200')
        self.master.title('Records')
        self.connection = sqlite3.connect('r.sqlite')
        self.cur = self.connection.cursor()
        self.dateLabel = Label(self.master, text="Date", width=10)
        self.dateLabel.grid(row=0, column=0)
        self.BMILabel = Label(self.master, text="BMI", width=10)
        self.BMILabel.grid(row=0, column=1)
        self.stateLabel = Label(self.master, text="Status", width=10)
        self.stateLabel.grid(row=0, column=2)
        self.showallrecords()

    def showallrecords(self):
        data = self.readfromdatabase()
        for index, dat in enumerate(data):
            Label(self.master, text=dat[0]).grid(row=index + 1, column=0)
            Label(self.master, text=dat[1]).grid(row=index + 1, column=1)
            Label(self.master, text=dat[2]).grid(row=index + 1, column=2)

    def readfromdatabase(self):
        self.cur.execute("SELECT * FROM reservations")
        return self.cur.fetchall()


root = tkinter.Tk()
root.geometry("900x300")
Records(root)
root.mainloop()