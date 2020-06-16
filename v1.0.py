import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import *

Font = ("Verdana", 12)


class GUI(Frame):

    def quit(self):
        msg = tk.messagebox.askquestion('Zamknięcie programu', 'Czy jesteś pewien, że chcesz zamknąć program?',
                                        icon='warning')
        if msg == 'yes':
            exit()

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.geometry("1500x600+50+50")
        self.master.title("System obsługi apartamentów")
        self.master.minsize(1500, 600)
        self.master.maxsize(1924, 1061)
        self.master.resizable(1, 1)

        # row and column setup
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.rowconfigure(2, weight=1)
        self.master.rowconfigure(3, weight=1)
        self.master.rowconfigure(4, weight=1)
        self.master.rowconfigure(5, weight=1)
        self.master.rowconfigure(6, weight=1)

        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)
        self.master.columnconfigure(2, weight=1)
        self.master.columnconfigure(3, weight=1)
        self.master.columnconfigure(4, weight=1)
        self.master.columnconfigure(5, weight=10)
        self.master.columnconfigure(6, weight=1)

        self.button_frame = tk.Frame(root)
        self.button_frame.grid(row=0, column=0, columnspan=3, sticky="ew", padx=10)

        # self.text = Text(self.master, width = 20, height = 3)
        # self.text.pack()
        # self.text.insert(END, "Before\ntop window\ninteraction")
        # self.Frame1 = tk.Frame(root)
        # self.Frame1.place(relx=0.159, rely=0.015, relheight=0.974, relwidth=0.832)

        self.Home = ttk.Button(self.button_frame, text='''Podstawowe''')
        self.Home.grid(row=0, column=1, sticky="ew")
        self.Reservation_button = ttk.Button(self.button_frame, text='''Dodaj rezerwację''', command=lambda: ReservationWindow(
            title="ABC"))
        self.Reservation_button.grid(row=1, column=1, sticky="ew")
        self.Quit = ttk.Button(self.button_frame, text='''Zamknij''', command=self.quit)
        self.Quit.grid(row=2, column=1, sticky="ew")

        # Frame reservationList
        # self.text = Text(self.master, width = 20, height = 3)
        # self.text.place(relx=0.22, rely=0.01, height=34, width=137)
        # self.text.insert(END, "Before\ntop window\ninteraction")
        # self.Frame1 = tk.Frame(root)
        # self.Frame1.grid(row=1, column=5)
        self.reservationListV = tk.Variable(master)
        list1 = []
        for i in range(100):
            list1.append(i)
        self.reservationListV.set(("Rezerwacje",))
        self.reservationList = tk.Listbox(root, background="black", fg="white", font=Font)
        [self.reservationList.insert(END, item) for item in list1]
        self.reservationList.grid(row=0, column=2, rowspan=5, columnspan=5, sticky="nsew", pady=50)
        self.scrollbar = Scrollbar(root)
        self.scrollbar.grid(row=0, column=6, rowspan=5, sticky="nse", pady=30)
        self.scrollbar.config(command=self.reservationList.yview)
        self.reservationList.config(border=2, relief='sunken', yscrollcommand=self.scrollbar.set)

        # labels
        label1 = tk.Label(root, text="Szczegóły rezerwacji")
        label1.place(relx=0.10, rely=0.01, height=34, width=137)



class OpenToplevelWindow(Toplevel):

    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)
        self.grab_set()
        self.takefocus = True
        self.focus_set()

        # def replace_text():
        #     app.text.delete(1.0, END)
        #     app.text.insert(END, "Text From\nToplevel")
        #
        # top_button = Button(self, text = "Replace text in main window",
        #                     command=replace_text)
        # top_button.pack()


class ReservationWindow(OpenToplevelWindow):

    def __init__(self, title=None, *args, **kwargs):
        OpenToplevelWindow.__init__(self, title=None, *args, **kwargs)
        self.geometry("1000x500")
        self.title("Dodaj rezerwację")
        self.grab_set()
        self.takefocus = True
        self.focus_set()


if __name__ == "__main__":
    root = Tk()
    app = GUI(root)
    root.mainloop()