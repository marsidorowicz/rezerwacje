import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import *


class GUI(Frame):

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.geometry("1000x1000")
        self.master.title("System obsługi apartamentów")
        self.my_frame = Frame(self.master)
        self.my_frame.pack()

        self.text = Text(self.master, width = 20, height = 3)
        self.text.pack()
        self.text.insert(END, "Before\ntop window\ninteraction")
        # self.Frame1 = tk.Frame(root)
        # self.Frame1.place(relx=0.159, rely=0.015, relheight=0.974, relwidth=0.832)

        self.Home = ttk.Button(root, text='''Podstawowe''')
        self.Home.place(relx=0.01, rely=0.015, height=34, width=137)
        self.Reservation_button = tk.Button(root, text='''Dodaj rezerwację''', command=OpenToplevelWindow)
        self.Reservation_button.place(relx=0.01, rely=0.088, height=34, width=137)
        self.Quit = tk.Button(root, text='''Zamknij''', command=self.quit)
        self.Quit.place(relx=0.01, rely=0.161, height=34, width=137)


class OpenToplevelWindow(Toplevel):

    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)
        self.grab_set()
        self.geometry("1000x1000")
        self.title("Dodaj rezerwację")
        self.takefocus = True
        self.focus_set()

        def replace_text():
            app.text.delete(1.0, END)
            app.text.insert(END, "Text From\nToplevel")

        top_button = Button(self, text = "Replace text in main window",
                            command=replace_text)
        top_button.pack()



if __name__ == "__main__":
    root = Tk()
    app = GUI(root)
    root.mainloop()