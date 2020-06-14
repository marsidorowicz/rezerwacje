import tkinter as tk
from tkinter import ttk


LARGE_FONT = ("Verdana", 12)


class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default=None)  # icon setup put in default *.ico
        tk.Tk.wm_title(self, "System rezerwacji MSCApartments")
        tk.Tk.geometry(self, "1000x1000")

        container = tk.Frame(self)
        container.grid(row=0, column=0, sticky="nsew")

        self.frames = {}

        frame_home = StartPage(container, self)
        frame_reservations = PageOne(container, self)

        self.frames[StartPage] = frame_home
        self.frames[PageOne] = frame_reservations

        frame_home.grid(row=1, column=2, sticky="nsew")
        frame_reservations.grid(row=1, column=2, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=200, padx=200)

        # command within button cant throw args to funcs. Use lambda to throw those args to the func instead
        button1 = ttk.Button(self, text="Strona główna", command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text="Rezerwacje", command=lambda: controller.show_frame(PageOne))
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Rezerwacje", font=LARGE_FONT)
        label.pack(pady=200, padx=200)

        # command within button cant throw args to funcs. Use lambda to throw those args to the func instead
        button1 = ttk.Button(self, text="Strona główna", command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text="Rezerwacje", command=lambda: controller.show_frame(PageOne))
        button2.pack()


app = MainWindow()
app.columnconfigure(1, weight=1)
app.columnconfigure(2, weight=10)
app.columnconfigure(3, weight=2)
app.rowconfigure(1, weight=5)
app.rowconfigure(2, weight=5)
app.rowconfigure(3, weight=1)
app.mainloop()