import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import *
import sqlite3
from datetime import *
import datetime

# conn = sqlite3.connect("r.db")
# c = conn.cursor()

Font = ("Verdana", 12)


class Records:
    # class created to see records that have been previously inputted#
    def __init__(self, master, yscrollcommand=None):
        self.master = master
        self.connection = sqlite3.connect('r.sqlite')
        self.cur = self.connection.cursor()
        self.dateLabel = Label(self.master, text="Imię", width=10, background="black", fg="white")
        self.dateLabel.grid(row=0, column=0)
        self.BMILabel = Label(self.master, text="Nazwisko", width=10, background="black", fg="white")
        self.BMILabel.grid(row=0, column=1)
        self.stateLabel = Label(self.master, text="Miesiąc", width=10, background="black", fg="white")
        self.stateLabel.grid(row=0, column=2)
        self.showallrecords()

    def showallrecords(self):
        data = self.readfromdatabase()
        for index, dat in enumerate(data):
            Label(self.master, text=dat[0], bg="black", fg="white").grid(row=index + 1, column=0)
            Label(self.master, text=dat[1], bg="black", fg="white").grid(row=index + 1, column=1)
            Label(self.master, text=dat[2], bg="black", fg="white").grid(row=index + 1, column=2)

    def readfromdatabase(self):
        self.cur.execute("SELECT * FROM reservations")
        return self.cur.fetchall()


class ScrollableFrame(ttk.Frame):

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(-1 * (event.delta // 120), "units")

    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.canvas = tk.Canvas(self)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")


class GUI(Frame):

    @staticmethod
    def quit1():
        msg = tk.messagebox.askquestion('Zamknięcie programu', 'Czy jesteś pewien, że chcesz zamknąć program?',
                                        icon='warning')
        if msg == 'yes':
            exit()

    def showallrecords(self):
        data = self.readfromdatabase()
        for index, dat in enumerate(data):
            pass
            # Label(self.master, text=dat[0]).grid(row=index + 1, column=0)
            # Label(self.master, text=dat[1]).grid(row=index + 1, column=1)
            # Label(self.master, text=dat[2]).grid(row=index + 1, column=2)
            # Label(self.frame, text=dat[0], bg="black", fg="white").place(x=1, y=(1+(index*100)), height=34,
            #                                                              width=100)
            # Label(self.frame, text=dat[1], bg="green", fg="white").place(x=150, y=(1+(index*100)), height=34,
            #                                                              width=100)
            # Label(self.frame, text=dat[2], bg="yellow", fg="white").place(x=300, y=(1+(index*100)), height=34,
            #                                                              width=100)

    def readfromdatabase(self):
        self.cur.execute("SELECT * FROM reservations")
        return self.cur.fetchall()

    def test1(self):
        self.Frame1.destroy()
        self.Frame1 = tk.Frame(root)
        self.Frame1.place(relx=0.159, rely=0.015, relheight=0.974, relwidth=0.833)
        # Example(self.Frame1).pack()
        self.connection = sqlite3.connect('r.sqlite')
        self.cur = self.connection.cursor()

        self.frame = ScrollableFrame(self.Frame1)
        data = self.readfromdatabase()
        for index, dat in enumerate(data):
            Label(self.frame, text=dat[0], bg="black", fg="white").place(x=1, y=(1+(index*100)), height=34,
                                                                         width=100)
            Label(self.frame, text=dat[1], bg="green", fg="white").place(x=150, y=(1+(index*100)), height=34,
                                                                         width=100)
            Label(self.frame, text=dat[2], bg="yellow", fg="white").place(x=300, y=(1+(index*100)), height=34,
                                                                         width=100)
        # for dat in data:
        #     print(dat)
        #     Label(self.frame.scrollable_frame, text=dat, bg="black", fg="white").pack(side="left")
        data = self.readfromdatabase()
        for index, dat in enumerate(data):
            print(index)
            # ttk.Label(self.frame.scrollable_frame, text=dat[0]+" "+dat[1]+ " "+dat[2]+ " "+str(dat[3])+" "+str(dat[4])+" "+str(dat[5])).pack(side="top", fill="both")
        self.frame.place(relx=0.159, rely=0.015, relheight=0.974, relwidth=0.833)

        self.showallrecords()

    def test2(self):
        self.Frame1.destroy()
        self.Frame1 = tk.Frame(root, background="black")
        self.Frame1.place(relx=0.159, rely=0.015, relheight=0.974, relwidth=0.833)
        Records(self.Frame1)

    # def readfromdatabase(self):
    #     self.cur.execute("SELECT * FROM reservations")
    #     return self.cur.fetchall()
    #
    # def showallrecords(self):
    #     data = self.readfromdatabase()
    #     for index, dat in enumerate(data):
    #
    #         Label(self.Frame1, text=dat[0], bg="black", fg="white").place(x=1, y=(1+(index*100)), height=34,
    #                                                                      width=100)
    #         Label(self.Frame1, text=dat[1], bg="green", fg="white").place(x=150, y=(1+(index*100)), height=34,
    #                                                                      width=100)
    #         Label(self.Frame1, text=dat[2], bg="yellow", fg="white").place(x=300, y=(1+(index*100)), height=34,
    #                                                                      width=100)

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.geometry("1500x600+50+50")
        self.master.title("System obsługi apartamentów")
        self.master.minsize(1500, 600)
        self.master.maxsize(1924, 1061)
        self.master.resizable(1, 1)
        self.authenticated = False
        self.frame = None

        self.Frame1 = tk.Frame(root, background="black")
        self.Frame1.place(relx=0.159, rely=0.015, relheight=0.974, relwidth=0.833)
        # self.scrollbar = Scrollbar(self.Frame1)
        # self.scrollbar.place(relx=0.980, rely=0.01, relheight=0.974, relwidth=0.213)

        # self.text = Text(self.master, width = 20, height = 3)
        # self.text.pack()
        # self.text.insert(END, "Before\ntop window\ninteraction")
        # self.Frame1 = tk.Frame(root)
        # self.Frame1.place(relx=0.159, rely=0.015, relheight=0.974, relwidth=0.832)
        #
        # self.Home = ttk.Button(self.button_frame, text='''Podstawowe''')
        # self.Home.grid(row=0, column=1, sticky="ew")
        # self.Reservation_button = ttk.Button(self.button_frame, text='''Dodaj rezerwację''',
        #                                      command=lambda: ReservationWindow())
        # self.Reservation_button.grid(row=1, column=1, sticky="ew")
        # self.Quit = ttk.Button(self.button_frame, text='''Zamknij''', command=self.quit)
        # self.Quit.grid(row=2, column=1, sticky="ew")

        # dodane z rezerwacji
        self.Home = ttk.Button(root, text='''Strona główna''', command=self.test2)
        self.Home.place(relx=0.01, rely=0.015, height=34, width=137)
        self.Reservation_button = ttk.Button(root, text='''Dodaj rezerwację''', command=lambda: ReservationWindow())
        self.Reservation_button.place(relx=0.01, rely=0.088, height=34, width=137)
        self.Button1_2 = ttk.Button(root, text='''Test''', command=self.test1)
        self.Button1_2.place(relx=0.01, rely=0.161, height=34, width=137)
        self.Quit = ttk.Button(root, text='''Zamknij''', command=self.quit1)
        self.Quit.place(relx=0.01, rely=0.234, height=34, width=137)

        # Frame reservationList
        # Records(self.Frame1)
        # self.frame = ScrollableFrame(self.Frame1)
        #
        #
        # # for i in range(50):
        # #     ttk.Label(self.frame.scrollable_frame, text="Sample scrolling label").pack()
        # self.connection = sqlite3.connect('r.sqlite')
        # self.cur = self.connection.cursor()


                # Label(self.frame, text=dat[0], bg="black", fg="white").place(relx=0.000, rely=0.050+i, height=34, width=100)
                # Label(self.frame, text=dat[1], bg="black", fg="white").place(relx=0.080, rely=0.050+i, height=34, width=100)
                # Label(self.frame, text=dat[2], bg="black", fg="white").place(relx=0.160, rely=0.050+i, height=34, width=100)
            # Label(self.frame, text=dat[1], bg="black", fg="white").grid(row=index + 1, column=1)
            # Label(self.frame, text=dat[2], bg="black", fg="white").grid(row=index + 1, column=2)

        # self.frame.pack(fill="both", expand=True)
        # self.showallrecords()



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

    def tsget(self):
        print("Timestamp function")

        # current date and time
        now = datetime.datetime.now()

        print("timestamp =", now)

        # dt_object = datetime.fromtimestamp(timestamp)
        # dt_object = datetime.fromtimestamp(timestamp)

        # print("dt_object =", dt_object)
        # print("type(dt_object) =", type(dt_object))
        return now

    def save(self):

        conn = sqlite3.connect("r.sqlite")
        try:

            # Var get value from entries
            name = self.TEntry_name.get()
            self.name = name.upper()
            surname = self.TEntry_surname.get()
            self.surname = surname.upper()
            month = self.TEntry_month.get()
            self.month = month.upper()
            self.arrival_date = self.TEntry_arrival.get()
            self.departure_date = self.TEntry_departure.get()
            self.price_total = self.TEntry_price_total.get()
            self.price_ra = self.TEntry_price_ra.get()
            self.exp_booking = self.TEntry_exp_booking.get()
            self.exp_VAT = self.TEntry_exp_vat.get()
            self.city_tax = self.TEntry_city_tax.get()
            self.exp = self.TEntry_exp.get()
            self.gift_price = self.TEntry_gift_price.get()
            self.clean_price = self.TEntry_clean_price.get()
            place = self.TEntry_place.get()
            self.place = place.upper()
            self.deposit = self.TEntry_deposit.get()
            invoice = self.TEntry_invoice.get()
            self.invoice = invoice.upper()
            paid = self.TEntry_paid.get()
            self.paid = paid.upper()
            self.remaining_pay = self.TEntry_remaining_pay.get()
            self.commission = self.TEntry_commision.get()
            x = self.tsget()
            self.ts = x

            print("tsget value is: {}".format(x))

            # write values to database
            conn = sqlite3.connect("r.sqlite")
            c = conn.cursor()
            print("Connected to SQLite")
            c.execute("CREATE TABLE IF NOT EXISTS reservations (name TEXT, surname TEXT, month TEXT, "
                      "arrival_date TEXT, departure_date TEXT, price_total FLOAT, price_ra FLOAT, "
                      "exp_booking FLOAT, exp_VAT FLOAT, city_tax FLOAT, exp FLOAT, gift_price FLOAT, "
                      "clean_price FLOAT, place TEXT, deposit FLOAT, invoice TEXT, paid TEXT, remaining_pay FLOAT, "
                      "commission FLOAT, ts TEXT PRIMARY KEY NOT NULL)")
            if self.name or self.surname:
                c.execute("INSERT INTO reservations (name, surname, month, arrival_date, departure_date, price_total, "
                          "price_ra, exp_booking, exp_VAT, city_tax, exp, gift_price, clean_price, place, deposit, "
                          "invoice, paid, remaining_pay, commission, ts) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, "
                          "?, ?, ?, ?, ?, ?, ?, ?)",
                          (self.name, self.surname, self.month, self.arrival_date, self.departure_date,
                           self.price_total,
                           self.price_ra, self.exp_booking, self.exp_VAT, self.city_tax, self.exp, self.gift_price,
                           self.clean_price, self.place, self.deposit, self.invoice, self.paid, self.remaining_pay,
                           self.commission, self.ts))

            # run timestamp function
            c.connection.commit()
            c.close()
        except sqlite3.Error as error:
            print("Error while working with SQLite", error)
        finally:
            if conn:
                conn.close()
                print("sqlite connection is closed")

    @staticmethod
    def test():

        # # Test write and read and print
        conn = sqlite3.connect("r.sqlite")
        c = conn.cursor()
        # c.execute("CREATE TABLE IF NOT EXISTS reservations (name TEXT, surname TEXT, month TEXT, "
        #           "arrival_date TEXT, departure_date TEXT, price_total FLOAT, price_ra FLOAT, "
        #           "exp_booking FLOAT, exp_VAT FLOAT, city_tax FLOAT, exp FLOAT, gift_price FLOAT, "
        #           "clean_price FLOAT, place TEXT, deposit FLOAT, invoice TEXT, paid TEXT, remaining_pay FLOAT, "
        #           "ts INTEGER)")
        #
        # c.connection.commit()

        # print("Database read and print")
        for name, surname, month, arrival_date, departure_date, price_total, price_ra, exp_booking, \
            exp_VAT, city_tax, exp, gift_price, clean_price, place, deposit, invoice, paid, remaining_pay,\
                commission, ts in c.execute("SELECT * from reservations ORDER BY ts"):

            # print(id1, name, surname, month)
            rows = c.fetchall()
            for row in rows:
                print(row)

        c.close()
        # conn = sqlite3.connect("r.db")
        # c = conn.cursor()
        # c.execute("SELECT * FROM reservations")
        # rows = c.fetchall()
        # for row in rows:
        #     print(row)

    @staticmethod
    def callback(p):
        if str.isalpha(p) or p == "":
            return True
        else:
            return False

    @staticmethod
    def callback1(p):
        if str.isdigit(p) or p == "":
            return True
        else:
            return False

    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)

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
        self.style.map('.', background=[('selected', _compcolor), ('active', _ana2color)])

        # key validation
        self.validate_allow_letters = (self.register(self.callback))
        self.validate_allow_numeric = (self.register(self.callback1))

        # window setup
        self.authenticated = False
        self.title("Dodaj rezerwację")
        self.grab_set()
        self.takefocus = True
        self.focus_set()
        self.geometry("1004x683+294+166")
        self.minsize(1004, 683)
        self.maxsize(1924, 1061)
        self.resizable(1, 1)
        self.configure(background="#d9d9d9")

        # var
        self.name = None
        self.surname = None
        self.month = None
        self.arrival_date = None
        self.departure_date = None
        self.price_total = None
        self.price_ra = None
        self.exp_booking = None
        self.exp_VAT = None
        self.city_tax = None
        self.exp = None
        self.gift_price = None
        self.clean_price = None
        self.place = None
        self.deposit = None
        self.invoice = None
        self.paid = None
        self.remaining_pay = None
        self.commission = None
        self.ts = None

        # Frame settins
        self.Frame1 = tk.Frame(self)
        self.Frame1.place(relx=0.159, rely=0.015, relheight=0.974, relwidth=0.833)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.TEntry_name = ttk.Entry(self.Frame1, validate="all", validatecommand=(self.validate_allow_letters, '%P'))
        self.TEntry_name.place(relx=0.12, rely=0.03, relheight=0.047, relwidth=0.211)
        self.TEntry_name.configure(takefocus="")
        self.TEntry_name.configure(cursor="ibeam")

        self.TEntry_surname = ttk.Entry(self.Frame1, validate="all", validatecommand=(self.validate_allow_letters,
                                                                                      '%P'))
        self.TEntry_surname.place(relx=0.12, rely=0.105, relheight=0.047, relwidth=0.212)
        self.TEntry_surname.configure(takefocus="")
        self.TEntry_surname.configure(cursor="ibeam")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.012, rely=0.03, height=31, width=64)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
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

        self.TEntry_month = ttk.Entry(self.Frame1, validate="all", validatecommand=(self.validate_allow_letters, '%P'))
        self.TEntry_month.place(relx=0.12, rely=0.18, relheight=0.047, relwidth=0.213)
        self.TEntry_month.configure(takefocus="")
        self.TEntry_month.configure(cursor="ibeam")

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

        self.TEntry_arrival = ttk.Entry(self.Frame1, validate="all", validatecommand=(self.validate_allow_numeric,
                                                                                      '%P'))
        self.TEntry_arrival.place(relx=0.12, rely=0.256, relheight=0.048, relwidth=0.213)
        self.TEntry_arrival.configure(takefocus="")
        self.TEntry_arrival.configure(cursor="ibeam")

        self.TEntry_departure = ttk.Entry(self.Frame1, validate="all", validatecommand=(self.validate_allow_numeric,
                                                                                        '%P'))
        self.TEntry_departure.place(relx=0.12, rely=0.331, relheight=0.048, relwidth=0.213)
        self.TEntry_departure.configure(takefocus="")
        self.TEntry_departure.configure(cursor="ibeam")

        self.TEntry_price_total = ttk.Entry(self.Frame1, validate="all", validatecommand=(self.validate_allow_numeric,
                                                                                          '%P'))
        self.TEntry_price_total.place(relx=0.12, rely=0.406, relheight=0.048, relwidth=0.213)
        self.TEntry_price_total.configure(takefocus="")
        self.TEntry_price_total.configure(cursor="ibeam")

        self.TEntry_price_ra = ttk.Entry(self.Frame1, validate="all", validatecommand=(self.validate_allow_numeric,
                                                                                       '%P'))
        self.TEntry_price_ra.place(relx=0.12, rely=0.481, relheight=0.048, relwidth=0.213)
        self.TEntry_price_ra.configure(takefocus="")
        self.TEntry_price_ra.configure(cursor="ibeam")

        self.TEntry_exp_booking = ttk.Entry(self.Frame1, validate="all", validatecommand=(self.validate_allow_numeric,
                                                                                          '%P'))
        self.TEntry_exp_booking.place(relx=0.12, rely=0.556, relheight=0.048, relwidth=0.213)
        self.TEntry_exp_booking.configure(takefocus="")
        self.TEntry_exp_booking.configure(cursor="ibeam")

        self.TEntry_exp_vat = ttk.Entry(self.Frame1, validate="all", validatecommand=(self.validate_allow_numeric,
                                                                                      '%P'))
        self.TEntry_exp_vat.place(relx=0.12, rely=0.632, relheight=0.048, relwidth=0.213)
        self.TEntry_exp_vat.configure(takefocus="")
        self.TEntry_exp_vat.configure(cursor="ibeam")

        self.Label1_8 = tk.Label(self.Frame1)
        self.Label1_8.place(relx=0.012, rely=0.331, height=32, width=64)
        self.Label1_8.configure(activebackground="#f9f9f9")
        self.Label1_8.configure(activeforeground="black")
        self.Label1_8.configure(background="#d9d9d9")
        self.Label1_8.configure(disabledforeground="#a3a3a3")
        self.Label1_8.configure(foreground="#000000")
        self.Label1_8.configure(highlightbackground="#d9d9d9")
        self.Label1_8.configure(highlightcolor="black")
        self.Label1_8.configure(text='''Wyjazd''')

        self.Label1_8 = tk.Label(self.Frame1)
        self.Label1_8.place(relx=0.012, rely=0.406, height=32, width=64)
        self.Label1_8.configure(activebackground="#f9f9f9")
        self.Label1_8.configure(activeforeground="black")
        self.Label1_8.configure(background="#d9d9d9")
        self.Label1_8.configure(disabledforeground="#a3a3a3")
        self.Label1_8.configure(foreground="#000000")
        self.Label1_8.configure(highlightbackground="#d9d9d9")
        self.Label1_8.configure(highlightcolor="black")
        self.Label1_8.configure(text='''Kwota całk''')

        self.Label1_8 = tk.Label(self.Frame1)
        self.Label1_8.place(relx=0.012, rely=0.481, height=32, width=64)
        self.Label1_8.configure(activebackground="#f9f9f9")
        self.Label1_8.configure(activeforeground="black")
        self.Label1_8.configure(background="#d9d9d9")
        self.Label1_8.configure(disabledforeground="#a3a3a3")
        self.Label1_8.configure(foreground="#000000")
        self.Label1_8.configure(highlightbackground="#d9d9d9")
        self.Label1_8.configure(highlightcolor="black")
        self.Label1_8.configure(text='''Kwota ra''')

        self.Label1_8 = tk.Label(self.Frame1)
        self.Label1_8.place(relx=0.012, rely=0.556, height=32, width=64)
        self.Label1_8.configure(activebackground="#f9f9f9")
        self.Label1_8.configure(activeforeground="black")
        self.Label1_8.configure(background="#d9d9d9")
        self.Label1_8.configure(disabledforeground="#a3a3a3")
        self.Label1_8.configure(foreground="#000000")
        self.Label1_8.configure(highlightbackground="#d9d9d9")
        self.Label1_8.configure(highlightcolor="black")
        self.Label1_8.configure(text='''Booking''')

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

        self.TEntry_city_tax = ttk.Entry(self.Frame1, validate="all", validatecommand=(self.validate_allow_numeric,
                                                                                       '%P'))
        self.TEntry_city_tax.place(relx=0.12, rely=0.707, relheight=0.048, relwidth=0.213)
        self.TEntry_city_tax.configure(takefocus="")
        self.TEntry_city_tax.configure(cursor="ibeam")

        self.TEntry_exp = ttk.Entry(self.Frame1, validate="all", validatecommand=(self.validate_allow_numeric,
                                                                                  '%P'))
        self.TEntry_exp.place(relx=0.12, rely=0.782, relheight=0.048, relwidth=0.213)
        self.TEntry_exp.configure(takefocus="")
        self.TEntry_exp.configure(cursor="ibeam")

        self.Label1_9 = tk.Label(self.Frame1)
        self.Label1_9.place(relx=0.012, rely=0.707, height=32, width=84)
        self.Label1_9.configure(activebackground="#f9f9f9")
        self.Label1_9.configure(activeforeground="black")
        self.Label1_9.configure(background="#d9d9d9")
        self.Label1_9.configure(disabledforeground="#a3a3a3")
        self.Label1_9.configure(foreground="#000000")
        self.Label1_9.configure(highlightbackground="#d9d9d9")
        self.Label1_9.configure(highlightcolor="black")
        self.Label1_9.configure(text='''Podatek miejski''')

        self.Label1_9 = tk.Label(self.Frame1)
        self.Label1_9.place(relx=0.012, rely=0.782, height=32, width=74)
        self.Label1_9.configure(activebackground="#f9f9f9")
        self.Label1_9.configure(activeforeground="black")
        self.Label1_9.configure(background="#d9d9d9")
        self.Label1_9.configure(disabledforeground="#a3a3a3")
        self.Label1_9.configure(foreground="#000000")
        self.Label1_9.configure(highlightbackground="#d9d9d9")
        self.Label1_9.configure(highlightcolor="black")
        self.Label1_9.configure(text='''Koszty''')

        self.TEntry_gift_price = ttk.Entry(self.Frame1, validate="all", validatecommand=(self.validate_allow_numeric,
                                                                                         '%P'))
        self.TEntry_gift_price.place(relx=0.12, rely=0.857, relheight=0.048, relwidth=0.213)
        self.TEntry_gift_price.configure(takefocus="")
        self.TEntry_gift_price.configure(cursor="ibeam")

        self.TEntry_clean_price = ttk.Entry(self.Frame1, validate="all", validatecommand=(self.validate_allow_numeric,
                                                                                          '%P'))
        self.TEntry_clean_price.place(relx=0.12, rely=0.932, relheight=0.048, relwidth=0.213)
        self.TEntry_clean_price.configure(takefocus="")
        self.TEntry_clean_price.configure(cursor="ibeam")

        self.Label1_9 = tk.Label(self.Frame1)
        self.Label1_9.place(relx=0.012, rely=0.857, height=32, width=74)
        self.Label1_9.configure(activebackground="#f9f9f9")
        self.Label1_9.configure(activeforeground="black")
        self.Label1_9.configure(background="#d9d9d9")
        self.Label1_9.configure(disabledforeground="#a3a3a3")
        self.Label1_9.configure(foreground="#000000")
        self.Label1_9.configure(highlightbackground="#d9d9d9")
        self.Label1_9.configure(highlightcolor="black")
        self.Label1_9.configure(text='''Prezent''')

        self.Label1_9 = tk.Label(self.Frame1)
        self.Label1_9.place(relx=0.012, rely=0.932, height=32, width=74)
        self.Label1_9.configure(activebackground="#f9f9f9")
        self.Label1_9.configure(activeforeground="black")
        self.Label1_9.configure(background="#d9d9d9")
        self.Label1_9.configure(disabledforeground="#a3a3a3")
        self.Label1_9.configure(foreground="#000000")
        self.Label1_9.configure(highlightbackground="#d9d9d9")
        self.Label1_9.configure(highlightcolor="black")
        self.Label1_9.configure(text='''Sprzątanie''')

        self.Label1_9 = tk.Label(self.Frame1)
        self.Label1_9.place(relx=0.347, rely=0.03, height=32, width=74)
        self.Label1_9.configure(activebackground="#f9f9f9")
        self.Label1_9.configure(activeforeground="black")
        self.Label1_9.configure(background="#d9d9d9")
        self.Label1_9.configure(disabledforeground="#a3a3a3")
        self.Label1_9.configure(foreground="#000000")
        self.Label1_9.configure(highlightbackground="#d9d9d9")
        self.Label1_9.configure(highlightcolor="black")
        self.Label1_9.configure(text='''Apartament''')

        self.Label1_9 = tk.Label(self.Frame1)
        self.Label1_9.place(relx=0.347, rely=0.105, height=32, width=74)
        self.Label1_9.configure(activebackground="#f9f9f9")
        self.Label1_9.configure(activeforeground="black")
        self.Label1_9.configure(background="#d9d9d9")
        self.Label1_9.configure(disabledforeground="#a3a3a3")
        self.Label1_9.configure(foreground="#000000")
        self.Label1_9.configure(highlightbackground="#d9d9d9")
        self.Label1_9.configure(highlightcolor="black")
        self.Label1_9.configure(text='''Depozyt''')

        self.Label1_9 = tk.Label(self.Frame1)
        self.Label1_9.place(relx=0.347, rely=0.18, height=32, width=74)
        self.Label1_9.configure(activebackground="#f9f9f9")
        self.Label1_9.configure(activeforeground="black")
        self.Label1_9.configure(background="#d9d9d9")
        self.Label1_9.configure(disabledforeground="#a3a3a3")
        self.Label1_9.configure(foreground="#000000")
        self.Label1_9.configure(highlightbackground="#d9d9d9")
        self.Label1_9.configure(highlightcolor="black")
        self.Label1_9.configure(text='''Dokument''')

        self.TEntry_place = ttk.Entry(self.Frame1, validate="all", validatecommand=(self.validate_allow_letters, '%P'))
        self.TEntry_place.place(relx=0.455, rely=0.03, relheight=0.047, relwidth=0.212)
        self.TEntry_place.configure(takefocus="")
        self.TEntry_place.configure(cursor="ibeam")

        self.TEntry_deposit = ttk.Entry(self.Frame1, validate="all", validatecommand=(self.validate_allow_numeric,
                                                                                      '%P'))
        self.TEntry_deposit.place(relx=0.455, rely=0.105, relheight=0.047, relwidth=0.212)
        self.TEntry_deposit.configure(takefocus="")
        self.TEntry_deposit.configure(cursor="ibeam")

        self.TEntry_invoice = ttk.Entry(self.Frame1, validate="all", validatecommand=(self.validate_allow_letters,
                                                                                      '%P'))
        self.TEntry_invoice.place(relx=0.455, rely=0.18, relheight=0.047, relwidth=0.212)
        self.TEntry_invoice.configure(takefocus="")
        self.TEntry_invoice.configure(cursor="ibeam")

        self.TEntry_paid = ttk.Entry(self.Frame1, validate="all", validatecommand=(self.validate_allow_letters,
                                                                                   '%P'))
        self.TEntry_paid.place(relx=0.455, rely=0.256, relheight=0.047, relwidth=0.212)
        self.TEntry_paid.configure(takefocus="")
        self.TEntry_paid.configure(cursor="ibeam")

        self.Label1_10 = tk.Label(self.Frame1)
        self.Label1_10.place(relx=0.347, rely=0.256, height=32, width=74)
        self.Label1_10.configure(activebackground="#f9f9f9")
        self.Label1_10.configure(activeforeground="black")
        self.Label1_10.configure(background="#d9d9d9")
        self.Label1_10.configure(disabledforeground="#a3a3a3")
        self.Label1_10.configure(foreground="#000000")
        self.Label1_10.configure(highlightbackground="#d9d9d9")
        self.Label1_10.configure(highlightcolor="black")
        self.Label1_10.configure(text='''Opłacone?''')

        self.TEntry_remaining_pay = ttk.Entry(self.Frame1, validate="all", validatecommand=(self.validate_allow_numeric,
                                                                                            '%P'))
        self.TEntry_remaining_pay.place(relx=0.455, rely=0.331, relheight=0.047, relwidth=0.213)
        self.TEntry_remaining_pay.configure(takefocus="")
        self.TEntry_remaining_pay.configure(cursor="ibeam")

        self.Label1_11 = tk.Label(self.Frame1)
        self.Label1_11.place(relx=0.347, rely=0.331, height=32, width=74)
        self.Label1_11.configure(activebackground="#f9f9f9")
        self.Label1_11.configure(activeforeground="black")
        self.Label1_11.configure(background="#d9d9d9")
        self.Label1_11.configure(disabledforeground="#a3a3a3")
        self.Label1_11.configure(foreground="#000000")
        self.Label1_11.configure(highlightbackground="#d9d9d9")
        self.Label1_11.configure(highlightcolor="black")
        self.Label1_11.configure(text='''Dopłata''')

        self.TEntry_commision = ttk.Entry(self.Frame1, validate="all", validatecommand=(self.validate_allow_numeric,
                                                                                        '%P'))
        self.TEntry_commision.place(relx=0.455, rely=0.406, relheight=0.047, relwidth=0.213)
        self.TEntry_commision.configure(takefocus="")
        self.TEntry_commision.configure(cursor="ibeam")

        self.Label1_12 = tk.Label(self.Frame1)
        self.Label1_12.place(relx=0.347, rely=0.406, height=32, width=74)
        self.Label1_12.configure(activebackground="#f9f9f9")
        self.Label1_12.configure(activeforeground="black")
        self.Label1_12.configure(background="#d9d9d9")
        self.Label1_12.configure(disabledforeground="#a3a3a3")
        self.Label1_12.configure(foreground="#000000")
        self.Label1_12.configure(highlightbackground="#d9d9d9")
        self.Label1_12.configure(highlightcolor="black")
        self.Label1_12.configure(text='''Prowizja''')

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

    def __init__(self, root2):

        self.authenticated = False
        self.count_login = 3
        self.root1 = root2
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
        self.username.focus()
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


class SimpleTableInput(tk.Frame):
    def __init__(self, parent, rows, columns):
        tk.Frame.__init__(self, parent)

        self.ilist = []
        self._entry = {}
        self.rows = rows
        self.columns = columns

        # register a command to use for validation
        vcmd = (self.register(self._validate), "%P")

        # create the table of widgets
        for row in range(self.rows):
            for column in range(self.columns):
                index = (row, column)
                e = tk.Entry(self, validate="key", validatecommand=vcmd)
                e.grid(row=row, column=column, stick="nsew")
                self._entry[index] = e
        # adjust column weights so they all expand equally
        for column in range(self.columns):
            self.grid_columnconfigure(column, weight=1)
        # designate a final, empty row to fill up any extra space
        self.grid_rowconfigure(rows, weight=1)

    def put(self):
        for i in range(10):
            self.ilist.append(i)
        print(self.ilist)
        for row in range(self.rows):
            if row == 0:
                for column in range(self.rows):
                    self._entry[row, column].insert(0, self.ilist[column])

    def get(self):

        """Return a list of lists, containing the data in the table"""
        result = []
        for row in range(self.rows):
            current_row = []
            for column in range(self.columns):
                index = (row, column)
                current_row.append(self._entry[index].get())
            result.append(current_row)
        return result

    def _validate(self, p):

        """Perform input validation.

        Allow only an empty value, or a value that can be converted to a float
        """
        if p.strip() == "":
            return True

        try:
            f = float(p)
        except ValueError:
            self.bell()
            return False
        return True


class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.table = SimpleTableInput(self, 50, 10)
        self.submit = tk.Button(self, text="Submit", command=self.on_submit)
        self.submit1 = tk.Button(self, text="Fill", command=self.on_submit1)
        self.table.pack(side="top", fill="both", expand=True)
        self.submit.pack(side="bottom")
        self.submit1.pack(side="bottom")

    def on_submit(self):
        print(self.table.get())

    def on_submit1(self):
        print(self.table.put())


if __name__ == "__main__":

    # root1 = Tk()
    # root1.geometry('425x185+700+300')  # uncomment to get AUTHENTICATION
    # application = Authentication(root1)
    # root1.mainloop()

    root = Tk()
    app = GUI(root)
    # if not application.authenticated:  # uncomment to get AUTHENTICATION
    #     sys.exit()

    root.mainloop()
