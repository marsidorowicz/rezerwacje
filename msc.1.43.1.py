import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from datetime import *
from tkinter import *
import platform
import datetime
import sched
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

Font = ("Verdana", 12)

try:
    from Tkinter import Frame, Label, Message, StringVar, Canvas
    from ttk import Scrollbar
    from Tkconstants import *
except ImportError:
    from tkinter import Frame, Label, Message, StringVar, Canvas
    from tkinter.ttk import Scrollbar
    from tkinter.constants import *

OS = platform.system()


class Mousewheel_Support(object):
    # implemetation of singleton pattern
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, root, horizontal_factor=2, vertical_factor=2):

        self._active_area = None




        if isinstance(horizontal_factor, int):
            self.horizontal_factor = horizontal_factor
        else:
            raise Exception("Vertical factor must be an integer.")

        if isinstance(vertical_factor, int):
            self.vertical_factor = vertical_factor
        else:
            raise Exception("Horizontal factor must be an integer.")

        if OS == "Linux":
            root.bind_all('<4>', self._on_mousewheel, add='+')
            root.bind_all('<5>', self._on_mousewheel, add='+')
        else:
            # Windows and MacOS
            root.bind_all("<MouseWheel>", self._on_mousewheel, add='+')

    def _on_mousewheel(self, event):
        if self._active_area:
            self._active_area.onMouseWheel(event)

    def _mousewheel_bind(self, widget):
        self._active_area = widget

    def _mousewheel_unbind(self):
        self._active_area = None

    def add_support_to(self, widget=None, xscrollbar=None, yscrollbar=None, what="units", horizontal_factor=None,
                       vertical_factor=None):
        if xscrollbar is None and yscrollbar is None:
            return

        if xscrollbar is not None:
            horizontal_factor = horizontal_factor or self.horizontal_factor

            xscrollbar.onMouseWheel = self._make_mouse_wheel_handler(widget, 'x', self.horizontal_factor, what)
            xscrollbar.bind('<Enter>', lambda event, scrollbar=xscrollbar: self._mousewheel_bind(scrollbar))
            xscrollbar.bind('<Leave>', lambda event: self._mousewheel_unbind())

        if yscrollbar is not None:
            vertical_factor = vertical_factor or self.vertical_factor

            yscrollbar.onMouseWheel = self._make_mouse_wheel_handler(widget, 'y', self.vertical_factor, what)
            yscrollbar.bind('<Enter>', lambda event, scrollbar=yscrollbar: self._mousewheel_bind(scrollbar))
            yscrollbar.bind('<Leave>', lambda event: self._mousewheel_unbind())

        main_scrollbar = yscrollbar if yscrollbar is not None else xscrollbar

        if widget is not None:
            if isinstance(widget, list) or isinstance(widget, tuple):
                list_of_widgets = widget
                for widget in list_of_widgets:
                    widget.bind('<Enter>', lambda event: self._mousewheel_bind(widget))
                    widget.bind('<Leave>', lambda event: self._mousewheel_unbind())

                    widget.onMouseWheel = main_scrollbar.onMouseWheel
            else:
                widget.bind('<Enter>', lambda event: self._mousewheel_bind(widget))
                widget.bind('<Leave>', lambda event: self._mousewheel_unbind())

                widget.onMouseWheel = main_scrollbar.onMouseWheel

    @staticmethod
    def _make_mouse_wheel_handler(widget, orient, factor=1, what="units"):
        view_command = getattr(widget, orient + 'view')

        if OS == 'Linux':
            def onMouseWheel(event):
                if event.num == 4:
                    view_command("scroll", (-1) * factor, what)
                elif event.num == 5:
                    view_command("scroll", factor, what)

        elif OS == 'Windows':
            def onMouseWheel(event):
                view_command("scroll", (-1) * int((event.delta / 120) * factor), what)

        elif OS == 'Darwin':
            def onMouseWheel(event):
                view_command("scroll", event.delta, what)

        return onMouseWheel


class Scrolling_Area(Frame, object):


    def __init__(self, master, width=None, height=None, mousewheel_speed=2, scroll_horizontally=True, xscrollbar=None,
                 scroll_vertically=True, yscrollbar=None, outer_background=None, inner_frame=Frame, **kw):
        super(Scrolling_Area, self).__init__(master, **kw)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self._clipper = Frame(self, background=outer_background, width=width, height=height)
        self._clipper.grid(row=0, column=0, sticky=N + E + W + S)

        self._width = width
        self._height = height

        self.innerframe = inner_frame(self._clipper, padx=0, pady=0, highlightthickness=0)
        self.innerframe.place(in_=self._clipper, x=0, y=0)

        #  add connection to google sheet
        rows = GUI.refresh_google_sheet()

        self.lenrows = len(rows)

        self.lb = {}
        for i in range(len(rows[0])):
            listbox = Listbox(self.innerframe, width=25, relief="sunken", height=self.lenrows)
            listbox.pack(side="left", fill="y", expand=True)
            self.lb[i] = listbox

        # set width for specific listbox
        for row in rows:
            for i in range(len(rows[0])):
                try:
                    self.lb[i].insert(END, row[i])
                    if i < 10:
                        self.lb[i].configure(width=12)
                    if i == 12:
                        self.lb[i].configure(width=12)
                    if i == 14:
                        self.lb[i].configure(width=15)
                    if i == 15:
                        self.lb[i].configure(width=18)
                    if i == 16:
                        self.lb[i].configure(width=13)
                    if i > 17:
                        self.lb[i].configure(width=12)
                except Exception as e:
                    pass
        # set color and bg for specific listbox
        for i in range(len(rows[0])):
            for b in range(1, len(rows)):
                try:
                    self.lb[i].itemconfig(b, {'bg': 'black'})
                    self.lb[i].itemconfig(b, {'foreground': 'white'})
                    self.lb[i].itemconfig(0, {'bg': 'black'})
                    self.lb[i].itemconfig(0, {'foreground': 'wheat'})
                    self.lb[i].configure(justify=CENTER)
                except Exception as e:
                    pass

        if scroll_vertically:
            if yscrollbar is not None:
                self.yscrollbar = yscrollbar
            else:
                self.yscrollbar = Scrollbar(self, orient=VERTICAL)
                self.yscrollbar.grid(row=0, column=1, sticky=N + S)

            self.yscrollbar.set(0.0, 1.0)
            self.yscrollbar.config(command=self.yview)
        else:
            self.yscrollbar = None

        self._scroll_vertically = scroll_vertically

        if scroll_horizontally:
            if xscrollbar is not None:
                self.xscrollbar = xscrollbar
            else:
                self.xscrollbar = Scrollbar(self, orient=HORIZONTAL)
                self.xscrollbar.grid(row=1, column=0, sticky=E + W)

            self.xscrollbar.set(0.0, 1.0)
            self.xscrollbar.config(command=self.xview)
        else:
            self.xscrollbar = None

        self._scroll_horizontally = scroll_horizontally

        self._jfraction = 0.05
        self._startX = 0
        self._startY = 0

        # Whenever the clipping window or scrolled frame change size,
        # update the scrollbars.
        self.innerframe.bind('<Configure>', self._on_configure)
        self._clipper.bind('<Configure>', self._on_configure)

        self.innerframe.xview = self.xview
        self.innerframe.yview = self.yview

        Mousewheel_Support(self).add_support_to(self.innerframe, xscrollbar=self.xscrollbar, yscrollbar=self.yscrollbar)

    def update_viewport(self):
        # compute new height and width
        self.update()
        frameHeight = float(self.innerframe.winfo_reqheight())
        frameWidth = float(self.innerframe.winfo_reqwidth())

        if self._width is not None:
            width = min(self._width, frameWidth)
        else:
            width = self._frameWidth

        if self._height is not None:
            height = min(self._height, frameHeight)
        else:
            height = self._frameHeight

        self._clipper.configure(width=width, height=height)

    def _on_configure(self, event):
        self._frameHeight = float(self.innerframe.winfo_reqheight())
        self._frameWidth = float(self.innerframe.winfo_reqwidth())

        # resize the visible part
        if self._scroll_horizontally:
            self.xview("scroll", 0, "unit")

        if self._scroll_vertically:
            self.yview("scroll", 0, "unit")

    def xview(self, mode=None, value=None, units=None):
        value = float(value)

        clipperWidth = self._clipper.winfo_width()
        frameWidth = self._frameWidth

        _startX = self._startX

        if mode is None:
            return self.xscrollbar.get()
        elif mode == 'moveto':
            # absolute movement
            self._startX = int(value * frameWidth)
        else:
            # mode == 'scroll'
            # relative movement
            if units == 'units':
                jump = int(clipperWidth * self._jfraction)
            else:
                jump = clipperWidth
            self._startX = self._startX + value * jump

        if frameWidth <= clipperWidth:
            # The scrolled frame is smaller than the clipping window.

            self._startX = 0
            hi = 1.0
            # use expand by default
            relwidth = 1
        else:
            # The scrolled frame is larger than the clipping window.
            # use expand by default
            if self._startX + clipperWidth > frameWidth:
                self._startX = frameWidth - clipperWidth
                hi = 1.0
            else:
                if self._startX < 0:
                    self._startX = 0
                hi = (self._startX + clipperWidth) / frameWidth
            relwidth = ''

        if self._startX != _startX:
            # Position frame relative to clipper.
            self.innerframe.place(x=-self._startX, relwidth=relwidth)

        lo = self._startX / frameWidth
        self.xscrollbar.set(lo, hi)

    def yview(self, mode=None, value=None, units=None):
        value = float(value)
        clipperHeight = self._clipper.winfo_height()
        frameHeight = self._frameHeight

        _startY = self._startY

        if mode is None:
            return self.yscrollbar.get()
        elif mode == 'moveto':
            self._startY = value * frameHeight
        else:  # mode == 'scroll'
            if units == 'units':
                jump = int(clipperHeight * self._jfraction)
            else:
                jump = clipperHeight
            self._startY = self._startY + value * jump

        if frameHeight <= clipperHeight:
            # The scrolled frame is smaller than the clipping window.

            self._startY = 0
            hi = 1.0
            # use expand by default
            relheight = 1
        else:
            # The scrolled frame is larger than the clipping window.
            # use expand by default
            if self._startY + clipperHeight > frameHeight:
                self._startY = frameHeight - clipperHeight
                hi = 1.0
            else:
                if self._startY < 0:
                    self._startY = 0
                hi = (self._startY + clipperHeight) / frameHeight
            relheight = ''

        if self._startY != _startY:
            # Position frame relative to clipper.
            self.innerframe.place(y=-self._startY, relheight=relheight)

        lo = self._startY / frameHeight
        # self.yscrollbar.set(lo, hi)


class GUI(Frame):

    @staticmethod
    def quit1():
        msg = tk.messagebox.askquestion('Zamknięcie programu', 'Czy jesteś pewien, że chcesz zamknąć program?',
                                        icon='warning')
        if msg == 'yes':
            exit()

    def read_from_database(self):
        pass
        # self.cur.execute("SELECT * FROM reservations")
        # return self.cur.fetchall()

    def test1(self):
        self.Frame1.destroy()
        self.Frame1 = tk.Frame(root)
        self.Frame1.place(relx=0.159, rely=0.015, relheight=0.974, relwidth=0.833)
        # Example(self.Frame1).pack()
        self.connection = sqlite3.connect('r.sqlite')
        self.cur = self.connection.cursor()

    def on_vsb(self, *args):

        # # automate Listbox yview method creation
        for i in range(20):
            self.lb[i].yview(*args)

    def on_hsb(self, *args):

        # # automate Listbox yview method creation
        for i in range(20):
            self.lb[i].yview(*args)

    def on_mouse_wheel(self, event):

        # automate Listbox creation
        for i in range(self.x):
            self.lb[i].yview("scroll", event.delta // 50, "units")
        return "break"

    def refresh_main(self):

        self.automated_listbox_creation()

    @staticmethod
    def outlook_connection():

        CLIENT_ID = "1cceed32-ae0b-47e7-8742-ba715c1f0c5d"
        CLIENT_SECRET = "dSY4wy-5.Jfdn.FVh~TmVMnpVUK3yG656o"
        AUTHORITY = "https://login.microsoftonline.com/python-reservations"



    @staticmethod
    def settle(apartment=None, month=None):
        print("Connecting to google sheet apartamentymsc@gmail.com")
        cred = ServiceAccountCredentials.from_json_keyfile_name(
            'E:\\Programowanie\plucky-avatar-282313-93e0d7031067.json')

        gs = gspread.authorize(cred)
        print("Authentication successful, downloading content from sheet1")
        kontr = gs.open('Kontrahenci2020').sheet1
        rows = kontr.get()

        print("Connecting to google sheet Rozliczenia")
        cred = ServiceAccountCredentials.from_json_keyfile_name(
            'E:\\Programowanie\plucky-avatar-282313-93e0d7031067.json')

        gs1 = gspread.authorize(cred)
        accounting = gs1.open('Rozliczenia2020').sheet1
        rows_accounting = []
        today = datetime.datetime.today()
        months = ['STYCZEŃ', 'LUTY', 'MARZEC', 'KWIECIEŃ', 'MAJ', 'CZERWIEC', 'LIPIEC', 'SIERPIEŃ', 'WRZESIEŃ',
                  'PAŹDZIERNIK', 'LISTOPAD', 'GRUDZIEŃ']
        print("Poprzedni miesiąc do rozliczeń: ", months[today.month-2])
        print(datetime.datetime.now())
        try:
            rows_accounting = accounting.get()
        except Exception as e:
            pass
        for row in rows:
            if months[today.month-2] in row:
                try:
                    row_accounting = [row[0], row[1], row[2], row[3], row[4], row[6], row[7], row[8], row[9], row[10],
                                      row[13], row[14], row[19], row[20]]
                    if row_accounting not in rows_accounting:
                        accounting.insert_row(row_accounting)
                        print("New content from sheet1 is not yet uploaded to sheet2... uploading...")
                        print(row)
                    else:
                        print("Content up to date...")
                except Exception as e:
                    print("There was problem with new content data, some data required is missing...")
        return rows

    @staticmethod
    def refresh_google_sheet(text=None):

        print("Connecting to google sheet apartamentymsc@gmail.com")
        cred = ServiceAccountCredentials.from_json_keyfile_name(
            'E:\\Programowanie\plucky-avatar-282313-93e0d7031067.json')

        gs = gspread.authorize(cred)
        print("Authentication successful, downloading content from sheet1")
        kontr = gs.open('Kontrahenci2020').sheet1

        rows = kontr.get()
        print("Connecting to google sheet zapas")
        cred1 = ServiceAccountCredentials.from_json_keyfile_name(
            'E:\\Programowanie\\wayscript\\send-emails-282415-a9f0e1e1227d.json')

        gs1 = gspread.authorize(cred1)
        print("Authentication successful, downloading content from sheet2")
        zapas = gs1.open('Zapas').sheet1
        rows_zapas = []
        today = datetime.datetime.today()
        months = ['STYCZEŃ', 'LUTY', 'MARZEC', 'KWIECIEŃ', 'MAJ', 'CZERWIEC', 'LIPIEC', 'SIERPIEŃ', 'WRZESIEŃ',
                  'PAŹDZIERNIK', 'LISTOPAD', 'GRUDZIEŃ']
        print(months[today.month-1])
        print(datetime.datetime.now())
        try:
            rows_zapas = zapas.get()
        except Exception as e:
            pass
        for row in rows:
            if months[today.month-1] in row:
                if str(today.year) in row:
                    try:
                        row_reduced = [row[10], row[13], row[14], row[19], row[20], row[21]]
                        if row_reduced not in rows_zapas:
                            zapas.insert_row(row_reduced)
                            print("New content from sheet1 is not yet uploaded to sheet2... uploading...")
                            print(row)
                    except Exception as e:
                        print("There was problem with new content data, some data required is missing...")
        # check if there is end of month and download reservations from next month if so
        if today.day > 24:
            print("Niedługo nowy miesiąc, pobieram nowe dane z miesiąca {}...".format(months[today.month]))
            for row in rows:
                if months[today.month] in row:
                    if str(today.year) in row:
                        try:
                            row_reduced = [row[10], row[13], row[14], row[19], row[20], row[21]]
                            if row_reduced not in rows_zapas:
                                zapas.insert_row(row_reduced)
                                print("New content from sheet1 is not yet uploaded to sheet2... uploading...")
                                print(row)
                        except Exception as e:
                            print("There was problem with new content data, some data required is missing...")
        # check if year is ending, if so download new year reservations from January
        if today.month == 12:
            if today.day == 24:
                print("Niedługo nowy rok, pobieram nowe rezerwacje z roku {}".format(today.year+1)) #TODO new year
                for row in rows:
                    if months[0] in row:
                        if str(today.year+1) in row:
                            try:
                                row_reduced = [row[10], row[13], row[14], row[19], row[20], row[21]]
                                if row_reduced not in rows_zapas:
                                    zapas.insert_row(row_reduced)
                                    print("New content from sheet1 is not yet uploaded to sheet2... uploading...")
                                    print(row)
                            except Exception as e:
                                print("There was problem with new content data, some data required is missing...")
        print("Content seems up to date...")
        print(months[0])
        root.after(7200000, GUI.refresh_google_sheet)  # run itself again after 1000 ms
        return rows

    def clock(self, text=None):
        self.time = datetime.datetime.now().strftime("Czas: %H:%M:%S"), datetime.datetime.today().year,\
                    datetime.datetime.today().month, datetime.datetime.today().day
        self.lab.config(text=self.time)
        # lab['text'] = time
        root.after(1000, self.clock)  # run itself again after 1000 ms

    def automated_listbox_creation(self):

        self.Frame1.destroy()
        if self.vsb:
            self.vsb.destroy()
        if self.hsb:
            self.hsb.destroy()
        self.Frame1 = tk.Frame(root, background="black")
        self.Frame1.place(x=200, y=30, relheight=0.930, relwidth=0.800)
        # open scrollable frame window
        self.scrolling_area = Scrolling_Area(self.Frame1)
        self.scrolling_area.pack(expand=True, fill="both")
        self.lab = Label(root)
        self.lab.place(x=200, y=0)

        # run first time automatic tasks
        self.clock()

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.geometry("1500x600+50+50")
        self.master.title("System obsługi apartamentów")
        self.master.minsize(1500, 600)
        self.master.maxsize(1924, 1061)
        self.master.resizable(1, 1)
        self.authenticated = False
        self.connection = sqlite3.connect('r.sqlite')
        self.cur = self.connection.cursor()
        self.frame = None
        self.vsb = None
        self.hsb = None
        self.listbox = None
        self.lb = {}

        self.Frame1 = tk.Frame(root, background="black")
        self.Frame1.place(relx=0.159, rely=0.015, relheight=0.974, relwidth=0.833)

        # menu
        self.Home = ttk.Button(root, text='''Strona główna''', command=self.refresh_main)
        self.Home.place(relx=0.01, rely=0.015, height=34, width=137)
        self.Reservation_button = ttk.Button(root, text='''Dodaj rezerwację''', command=lambda: ReservationWindow())
        self.Reservation_button.place(relx=0.01, rely=0.088, height=34, width=137)
        self.Button1_2 = ttk.Button(root, text='''Rozliczenie''', command=GUI.outlook_connection)
        self.Button1_2.place(relx=0.01, rely=0.161, height=34, width=137)
        self.Quit = ttk.Button(root, text='''Zamknij''', command=self.quit1)
        self.Quit.place(relx=0.01, rely=0.234, height=34, width=137)
        self.automated_listbox_creation()


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
