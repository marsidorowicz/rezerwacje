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
        self.authenticated = False

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
        self.Reservation_button = ttk.Button(self.button_frame, text='''Dodaj rezerwację''',
                                             command=lambda: ReservationWindow())
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


class ReservationWindow(Toplevel):

    def save(self):
        self.name = self.TEntry1.get()
        self.surname = self.TEntry1_3.get()
        self.month = self.TEntry1_4.get()
        print("Imię: {}".format(self.name))
        print("Nazwisko: {}".format(self.surname))
        print("Miesiąc: {}".format(self.month))
        print(self.TEntry1_5.get())

    def test(self):
        self.TEntry1.delete(0, END)
        self.TEntry1_3.delete(0, END)
        self.TEntry1_4.delete(0, END)
        print("Imię: {}".format(self.name))
        print("Nazwisko: {}".format(self.surname))
        print("Miesiąc: {}".format(self.month))

    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)
        self.authenticated = False
        self.geometry("1000x500")
        self.title("Dodaj rezerwację")
        self.grab_set()
        self.takefocus = True
        self.focus_set()
        '''This class configures and populates the toplevel window.
                   top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
        [('selected', _compcolor), ('active', _ana2color)])

        # window setup
        self.geometry("1004x683+294+166")
        self.minsize(120, 1)
        self.maxsize(1924, 1061)
        self.resizable(1, 1)
        self.title("New rootlevel")
        self.configure(background="#d9d9d9")

        # var
        self.name = None
        self.surname = None
        self.month = None

        self.Frame1 = tk.Frame(self)
        self.Frame1.place(relx=0.159, rely=0.015, relheight=0.974
                          , relwidth=0.833)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")

        self.TEntry1 = ttk.Entry(self.Frame1)
        self.TEntry1.place(relx=0.12, rely=0.03, relheight=0.047, relwidth=0.211)

        self.TEntry1.configure(takefocus="")
        self.TEntry1.configure(cursor="ibeam")

        self.TEntry1_3 = ttk.Entry(self.Frame1)
        self.TEntry1_3.place(relx=0.12, rely=0.105, relheight=0.047
                             , relwidth=0.212)
        self.TEntry1_3.configure(takefocus="")
        self.TEntry1_3.configure(cursor="ibeam")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.012, rely=0.03, height=31, width=64)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Imię''')

        self.Label1_4 = tk.Label(self.Frame1)
        self.Label1_4.place(relx=0.012, rely=0.105, height=31, width=64)
        self.Label1_4.configure(activebackground="#f9f9f9")
        self.Label1_4.configure(activeforeground="black")
        self.Label1_4.configure(background="#d9d9d9")
        self.Label1_4.configure(disabledforeground="#a3a3a3")
        self.Label1_4.configure(foreground="#000000")
        self.Label1_4.configure(highlightbackground="#d9d9d9")
        self.Label1_4.configure(highlightcolor="black")
        self.Label1_4.configure(text='''Nazwisko''')

        self.Label1_5 = tk.Label(self.Frame1)
        self.Label1_5.place(relx=0.012, rely=0.18, height=31, width=64)
        self.Label1_5.configure(activebackground="#f9f9f9")
        self.Label1_5.configure(activeforeground="black")
        self.Label1_5.configure(background="#d9d9d9")
        self.Label1_5.configure(disabledforeground="#a3a3a3")
        self.Label1_5.configure(foreground="#000000")
        self.Label1_5.configure(highlightbackground="#d9d9d9")
        self.Label1_5.configure(highlightcolor="black")
        self.Label1_5.configure(text='''Miesiąc''')

        self.TEntry1_4 = ttk.Entry(self.Frame1)
        self.TEntry1_4.place(relx=0.12, rely=0.18, relheight=0.047
                             , relwidth=0.213)
        self.TEntry1_4.configure(takefocus="")
        self.TEntry1_4.configure(cursor="ibeam")

        self.Label1_6 = tk.Label(self.Frame1)
        self.Label1_6.place(relx=0.012, rely=0.256, height=32, width=64)
        self.Label1_6.configure(activebackground="#f9f9f9")
        self.Label1_6.configure(activeforeground="black")
        self.Label1_6.configure(background="#d9d9d9")
        self.Label1_6.configure(disabledforeground="#a3a3a3")
        self.Label1_6.configure(foreground="#000000")
        self.Label1_6.configure(highlightbackground="#d9d9d9")
        self.Label1_6.configure(highlightcolor="black")
        self.Label1_6.configure(text='''Przyjazd''')

        self.TEntry1_5 = ttk.Entry(self.Frame1)
        self.TEntry1_5.place(relx=0.12, rely=0.256, relheight=0.048
                             , relwidth=0.213)
        self.TEntry1_5.configure(takefocus="")
        self.TEntry1_5.configure(cursor="ibeam")

        self.TEntry1_5 = ttk.Entry(self.Frame1)
        self.TEntry1_5.place(relx=0.12, rely=0.331, relheight=0.048
                             , relwidth=0.213)
        self.TEntry1_5.configure(takefocus="")
        self.TEntry1_5.configure(cursor="ibeam")

        self.TEntry1_5 = ttk.Entry(self.Frame1)
        self.TEntry1_5.place(relx=0.12, rely=0.406, relheight=0.048
                             , relwidth=0.213)
        self.TEntry1_5.configure(takefocus="")
        self.TEntry1_5.configure(cursor="ibeam")

        self.TEntry1_5 = ttk.Entry(self.Frame1)
        self.TEntry1_5.place(relx=0.12, rely=0.481, relheight=0.048
                             , relwidth=0.213)
        self.TEntry1_5.configure(takefocus="")
        self.TEntry1_5.configure(cursor="ibeam")

        self.TEntry1_5 = ttk.Entry(self.Frame1)
        self.TEntry1_5.place(relx=0.12, rely=0.556, relheight=0.048
                             , relwidth=0.213)
        self.TEntry1_5.configure(takefocus="")
        self.TEntry1_5.configure(cursor="ibeam")

        self.TEntry1_5 = ttk.Entry(self.Frame1)
        self.TEntry1_5.place(relx=0.12, rely=0.632, relheight=0.048
                             , relwidth=0.213)
        self.TEntry1_5.configure(takefocus="")
        self.TEntry1_5.configure(cursor="ibeam")

        self.Label1_7 = tk.Label(self.Frame1)
        self.Label1_7.place(relx=0.012, rely=0.331, height=32, width=64)
        self.Label1_7.configure(activebackground="#f9f9f9")
        self.Label1_7.configure(activeforeground="black")
        self.Label1_7.configure(background="#d9d9d9")
        self.Label1_7.configure(disabledforeground="#a3a3a3")
        self.Label1_7.configure(foreground="#000000")
        self.Label1_7.configure(highlightbackground="#d9d9d9")
        self.Label1_7.configure(highlightcolor="black")
        self.Label1_7.configure(text='''Wyjazd''')

        self.Label1_7 = tk.Label(self.Frame1)
        self.Label1_7.place(relx=0.012, rely=0.406, height=32, width=64)
        self.Label1_7.configure(activebackground="#f9f9f9")
        self.Label1_7.configure(activeforeground="black")
        self.Label1_7.configure(background="#d9d9d9")
        self.Label1_7.configure(disabledforeground="#a3a3a3")
        self.Label1_7.configure(foreground="#000000")
        self.Label1_7.configure(highlightbackground="#d9d9d9")
        self.Label1_7.configure(highlightcolor="black")
        self.Label1_7.configure(text='''Kwota całk''')

        self.Label1_7 = tk.Label(self.Frame1)
        self.Label1_7.place(relx=0.012, rely=0.481, height=32, width=64)
        self.Label1_7.configure(activebackground="#f9f9f9")
        self.Label1_7.configure(activeforeground="black")
        self.Label1_7.configure(background="#d9d9d9")
        self.Label1_7.configure(disabledforeground="#a3a3a3")
        self.Label1_7.configure(foreground="#000000")
        self.Label1_7.configure(highlightbackground="#d9d9d9")
        self.Label1_7.configure(highlightcolor="black")
        self.Label1_7.configure(text='''Kwota ra''')

        self.Label1_7 = tk.Label(self.Frame1)
        self.Label1_7.place(relx=0.012, rely=0.556, height=32, width=64)
        self.Label1_7.configure(activebackground="#f9f9f9")
        self.Label1_7.configure(activeforeground="black")
        self.Label1_7.configure(background="#d9d9d9")
        self.Label1_7.configure(disabledforeground="#a3a3a3")
        self.Label1_7.configure(foreground="#000000")
        self.Label1_7.configure(highlightbackground="#d9d9d9")
        self.Label1_7.configure(highlightcolor="black")
        self.Label1_7.configure(text='''Booking''')

        self.Label1_7 = tk.Label(self.Frame1)
        self.Label1_7.place(relx=0.012, rely=0.632, height=32, width=74)
        self.Label1_7.configure(activebackground="#f9f9f9")
        self.Label1_7.configure(activeforeground="black")
        self.Label1_7.configure(background="#d9d9d9")
        self.Label1_7.configure(disabledforeground="#a3a3a3")
        self.Label1_7.configure(foreground="#000000")
        self.Label1_7.configure(highlightbackground="#d9d9d9")
        self.Label1_7.configure(highlightcolor="black")
        self.Label1_7.configure(text='''Booking VAT''')

        self.TEntry1_6 = ttk.Entry(self.Frame1)
        self.TEntry1_6.place(relx=0.12, rely=0.707, relheight=0.048
                             , relwidth=0.213)
        self.TEntry1_6.configure(takefocus="")
        self.TEntry1_6.configure(cursor="ibeam")

        self.TEntry1_6 = ttk.Entry(self.Frame1)
        self.TEntry1_6.place(relx=0.12, rely=0.782, relheight=0.048
                             , relwidth=0.213)
        self.TEntry1_6.configure(takefocus="")
        self.TEntry1_6.configure(cursor="ibeam")

        self.Label1_8 = tk.Label(self.Frame1)
        self.Label1_8.place(relx=0.012, rely=0.707, height=32, width=84)
        self.Label1_8.configure(activebackground="#f9f9f9")
        self.Label1_8.configure(activeforeground="black")
        self.Label1_8.configure(background="#d9d9d9")
        self.Label1_8.configure(disabledforeground="#a3a3a3")
        self.Label1_8.configure(foreground="#000000")
        self.Label1_8.configure(highlightbackground="#d9d9d9")
        self.Label1_8.configure(highlightcolor="black")
        self.Label1_8.configure(text='''Podatek miejski''')

        self.Label1_8 = tk.Label(self.Frame1)
        self.Label1_8.place(relx=0.012, rely=0.782, height=32, width=74)
        self.Label1_8.configure(activebackground="#f9f9f9")
        self.Label1_8.configure(activeforeground="black")
        self.Label1_8.configure(background="#d9d9d9")
        self.Label1_8.configure(disabledforeground="#a3a3a3")
        self.Label1_8.configure(foreground="#000000")
        self.Label1_8.configure(highlightbackground="#d9d9d9")
        self.Label1_8.configure(highlightcolor="black")
        self.Label1_8.configure(text='''Koszty''')

        self.TEntry1_7 = ttk.Entry(self.Frame1)
        self.TEntry1_7.place(relx=0.12, rely=0.857, relheight=0.048, relwidth=0.213)
        self.TEntry1_7.configure(takefocus="")
        self.TEntry1_7.configure(cursor="ibeam")

        self.TEntry1_7 = ttk.Entry(self.Frame1)
        self.TEntry1_7.place(relx=0.12, rely=0.932, relheight=0.048, relwidth=0.213)
        self.TEntry1_7.configure(takefocus="")
        self.TEntry1_7.configure(cursor="ibeam")

        self.Label1_8 = tk.Label(self.Frame1)
        self.Label1_8.place(relx=0.012, rely=0.857, height=32, width=74)
        self.Label1_8.configure(activebackground="#f9f9f9")
        self.Label1_8.configure(activeforeground="black")
        self.Label1_8.configure(background="#d9d9d9")
        self.Label1_8.configure(disabledforeground="#a3a3a3")
        self.Label1_8.configure(foreground="#000000")
        self.Label1_8.configure(highlightbackground="#d9d9d9")
        self.Label1_8.configure(highlightcolor="black")
        self.Label1_8.configure(text='''Prezent''')

        self.Label1_8 = tk.Label(self.Frame1)
        self.Label1_8.place(relx=0.012, rely=0.932, height=32, width=74)
        self.Label1_8.configure(activebackground="#f9f9f9")
        self.Label1_8.configure(activeforeground="black")
        self.Label1_8.configure(background="#d9d9d9")
        self.Label1_8.configure(disabledforeground="#a3a3a3")
        self.Label1_8.configure(foreground="#000000")
        self.Label1_8.configure(highlightbackground="#d9d9d9")
        self.Label1_8.configure(highlightcolor="black")
        self.Label1_8.configure(text='''Sprzątanie''')

        self.Label1_8 = tk.Label(self.Frame1)
        self.Label1_8.place(relx=0.347, rely=0.03, height=32, width=74)
        self.Label1_8.configure(activebackground="#f9f9f9")
        self.Label1_8.configure(activeforeground="black")
        self.Label1_8.configure(background="#d9d9d9")
        self.Label1_8.configure(disabledforeground="#a3a3a3")
        self.Label1_8.configure(foreground="#000000")
        self.Label1_8.configure(highlightbackground="#d9d9d9")
        self.Label1_8.configure(highlightcolor="black")
        self.Label1_8.configure(text='''Apartament''')

        self.Label1_8 = tk.Label(self.Frame1)
        self.Label1_8.place(relx=0.347, rely=0.105, height=32, width=74)
        self.Label1_8.configure(activebackground="#f9f9f9")
        self.Label1_8.configure(activeforeground="black")
        self.Label1_8.configure(background="#d9d9d9")
        self.Label1_8.configure(disabledforeground="#a3a3a3")
        self.Label1_8.configure(foreground="#000000")
        self.Label1_8.configure(highlightbackground="#d9d9d9")
        self.Label1_8.configure(highlightcolor="black")
        self.Label1_8.configure(text='''Depozyt''')

        self.Label1_8 = tk.Label(self.Frame1)
        self.Label1_8.place(relx=0.347, rely=0.18, height=32, width=74)
        self.Label1_8.configure(activebackground="#f9f9f9")
        self.Label1_8.configure(activeforeground="black")
        self.Label1_8.configure(background="#d9d9d9")
        self.Label1_8.configure(cursor="fleur")
        self.Label1_8.configure(disabledforeground="#a3a3a3")
        self.Label1_8.configure(foreground="#000000")
        self.Label1_8.configure(highlightbackground="#d9d9d9")
        self.Label1_8.configure(highlightcolor="black")
        self.Label1_8.configure(text='''Dokument''')

        self.TEntry1_9 = ttk.Entry(self.Frame1)
        self.TEntry1_9.place(relx=0.455, rely=0.03, relheight=0.047, relwidth=0.212)
        self.TEntry1_9.configure(takefocus="")
        self.TEntry1_9.configure(cursor="ibeam")

        self.TEntry1_10 = ttk.Entry(self.Frame1)
        self.TEntry1_10.place(relx=0.455, rely=0.105, relheight=0.047, relwidth=0.212)
        self.TEntry1_10.configure(takefocus="")
        self.TEntry1_10.configure(cursor="ibeam")

        self.TEntry1_11 = ttk.Entry(self.Frame1)
        self.TEntry1_11.place(relx=0.455, rely=0.18, relheight=0.047, relwidth=0.212)
        self.TEntry1_11.configure(takefocus="")
        self.TEntry1_11.configure(cursor="ibeam")

        self.TEntry1_12 = ttk.Entry(self.Frame1)
        self.TEntry1_12.place(relx=0.455, rely=0.256, relheight=0.047, relwidth=0.212)
        self.TEntry1_12.configure(takefocus="")
        self.TEntry1_12.configure(cursor="ibeam")

        self.Label1_9 = tk.Label(self.Frame1)
        self.Label1_9.place(relx=0.347, rely=0.256, height=32, width=74)
        self.Label1_9.configure(activebackground="#f9f9f9")
        self.Label1_9.configure(activeforeground="black")
        self.Label1_9.configure(background="#d9d9d9")
        self.Label1_9.configure(disabledforeground="#a3a3a3")
        self.Label1_9.configure(foreground="#000000")
        self.Label1_9.configure(highlightbackground="#d9d9d9")
        self.Label1_9.configure(highlightcolor="black")
        self.Label1_9.configure(text='''Opłacone?''')

        self.TEntry1_10 = ttk.Entry(self.Frame1)
        self.TEntry1_10.place(relx=0.455, rely=0.331, relheight=0.047, relwidth=0.213)
        self.TEntry1_10.configure(takefocus="")
        self.TEntry1_10.configure(cursor="ibeam")

        self.Label1_10 = tk.Label(self.Frame1)
        self.Label1_10.place(relx=0.347, rely=0.331, height=32, width=74)
        self.Label1_10.configure(activebackground="#f9f9f9")
        self.Label1_10.configure(activeforeground="black")
        self.Label1_10.configure(background="#d9d9d9")
        self.Label1_10.configure(disabledforeground="#a3a3a3")
        self.Label1_10.configure(foreground="#000000")
        self.Label1_10.configure(highlightbackground="#d9d9d9")
        self.Label1_10.configure(highlightcolor="black")
        self.Label1_10.configure(text='''Dopłata''')

        self.Home = ttk.Button(self, text='''Wczytaj''')
        self.Home.place(relx=0.01, rely=0.015, height=34, width=137)
        self.Reservation = ttk.Button(self, text='''Zapisz''', command=self.save)
        self.Reservation.place(relx=0.01, rely=0.088, height=34, width=137)
        self.Button1_2 = ttk.Button(self, text='''Anuluj''', command=self.destroy)
        self.Button1_2.place(relx=0.01, rely=0.161, height=34, width=137)
        self.Reservation = ttk.Button(self, text='''Test''', command=self.test)
        self.Reservation.place(relx=0.01, rely=0.234, height=34, width=137)


class Authentication:

    user = 'admin'
    passw = 'admin'

    def login_user(self, one=None):

        """Check username and password entered are correct"""
        try:
            if self.username.get() == self.user and self.password.get() == self.passw:
                self.authenticated = True
                self.root1.destroy()
            else:
                '''Prompt user that either id or password is wrong'''
                self.count_login -= 1
                self.message['text'] = 'Hasło niepoprawne! Pozostało {} {}'.format(self.count_login, "prób")
                if self.count_login == 0:
                    self.root1.destroy()
                    sys.exit(1)
        except Exception as e:
            print(e)
            sys.exit(101)

    def __init__(self, root):

        self.authenticated = False
        self.count_login = 3
        self.root1 = root
        self.root1.title('USER AUTHENTICATION')

        '''Make Window 10X10'''

        rows = 0
        while rows < 10:
            self.root1.rowconfigure(rows, weight=1)
            self.root1.columnconfigure(rows, weight=1)
            rows += 1

        '''Username and Password'''

        frame = LabelFrame(self.root1, text='Login')
        frame.grid(row=1, column=1, columnspan=10, rowspan=10)
        Label(frame, text=' Usename ').grid(row=2, column=1, sticky=W)
        self.username = Entry(frame)
        self.username.grid(row=2, column=2)

        Label(frame, text=' Password ').grid(row=5, column=1, sticky=W)
        self.password = Entry(frame, show='*')
        self.password.grid(row=5, column=2)

        '''Message Display'''
        self.message = Label(text='', fg='Red')
        self.message.grid(row=9, column=6)
        # Button
        login_button = ttk.Button(frame, text='LOGIN', command=self.login_user)
        login_button.grid(row=7, column=2)
        self.root1.bind('<Return>', self.login_user)  # invoke makes crash
        # ttk.Button(frame, text='FaceID(Beta)',command = self.face_unlock).grid(row=8, column=2)


if __name__ == "__main__":

    # root1 = Tk()
    # root1.geometry('425x185+700+300')  # uncomment to get AUTHENTICATION
    # application = Authentication(root1)
    # root1.mainloop()

    root = Tk()
    app = GUI(root)
    # if not application.authenticated:
    #     sys.exit()

    root.mainloop()
