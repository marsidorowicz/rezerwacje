import  tkinter

mainWindow = tkinter.Tk()
LARGE_FONT = ("Verdana", 12)


def create_window():
    window = tkinter.Toplevel(mainWindow)
    window.title("Dodaj rezerwację")
    window.geometry("640x480+200+200")


def reload_frame(content):
    test1.set(content)
    main_frame.grid(row=1, column=1, sticky="nsew", rowspan=5)


class MainWindow(tkinter.Tk):

    def __init__(self, *args, **kwargs):

        tkinter.Tk.__init__(self, *args, **kwargs)
        container = tkinter.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        frame = StartPage(container, self)
        self.frames[StartPage] = frame


class ReservationFrame(tkinter.Frame):

    def __init__(self, parent, controller):

        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Witaj")
        label.pack(pady=100, padx=100)


class StartPage(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="StartPage", font=LARGE_FONT)
        label.pack(pady=200, padx=200)

        button1 = tkinter.Button(self, text="Dodaj rezerwację",)
        button1.pack()


class PageOne(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Rezerwacje", font=LARGE_FONT)
        label.pack(pady=200, padx=200)

        button2 = tkinter.Button(self, text="Strona główna")
        button2.pack()


# screen setup
mainWindow.title("Rezerwacje")
mainWindow.geometry("1024x768+200+200")
mainWindow.configure(background="black")

# window configuration
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=10)
mainWindow.columnconfigure(2, weight=2)
mainWindow.rowconfigure(1, weight=5)
mainWindow.rowconfigure(2, weight=5)
mainWindow.rowconfigure(3, weight=1)

# labels
tkinter.Label(mainWindow, text="Rezerwacje MSCApartments", fg="black").grid(row=0, column=1)

# main Frame
main_frame = tkinter.Frame(mainWindow)
main_frame.grid(row=1, column=1, sticky="nsew", rowspan=5)

# buttons
button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=0, column=0, sticky="ns", rowspan=5)
button_new_reservation = tkinter.Button(button_frame, text="Dodaj rezerwację", fg="black", command=lambda: reload_frame(StartPage))
button_new_reservation.grid(row=0, column=0)

# tkinter.Label(main_frame, text="ABC", relief="raised").pack(side="left")
test1 = tkinter.StringVar()
test1.set("ABC")
result = tkinter.Label(main_frame, textvariable=test1)
result.grid(row=1, column=1, sticky="nsew", rowspan=5)

mainWindow.mainloop()


app = MainWindow()
app.mainloop()