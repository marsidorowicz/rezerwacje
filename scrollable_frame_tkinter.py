# import tkinter as tk
# from tkinter import ttk
#
# root = tk.Tk()
# container = ttk.Frame(root)
# canvas = tk.Canvas(container)
# scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
# scrollable_frame = ttk.Frame(canvas)
#
# scrollable_frame.bind(
#     "<Configure>",
#     lambda e: canvas.configure(
#         scrollregion=canvas.bbox("all")
#     )
# )
#
# canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
#
# canvas.configure(yscrollcommand=scrollbar.set)
#
# for i in range(50):
#     ttk.Label(scrollable_frame, text="Sample scrolling label").pack()
#
# container.pack()
# canvas.pack(side="left", fill="both", expand=True)
# scrollbar.pack(side="right", fill="y")
#
# root.mainloop()

import tkinter as tk
import tkinter
from tkinter import ttk
import gspread
from oauth2client.service_account import ServiceAccountCredentials
try:
    from Tkinter import Frame, Label, Message, StringVar, Canvas
    from ttk import Scrollbar
    from Tkconstants import *
except ImportError:
    from tkinter import Frame, Label, Message, StringVar, Canvas
    from tkinter.ttk import Scrollbar
    from tkinter.constants import *


import platform


class ScrollableFrame(ttk.Frame):

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(-1 * (event.delta // 120), "units")

    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.canvas = tk.Canvas(self)
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

        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        scope = 'https://spreadsheets.google.com/feeds https://googleapis.com/auth/drive'
        cred = ServiceAccountCredentials.from_json_keyfile_name(
            'E:\\Programowanie\plucky-avatar-282313-93e0d7031067.json')

        gs = gspread.authorize(cred)

        kontr = gs.open('Kontrahenci2020').sheet1

        rows = kontr.get()

        self.data = []
        for index, dat in enumerate(self.data):
            self.x = len(dat)
        self.lb = {}
        for i in range(20):
            listbox = tk.Listbox(self.scrollbar, width=14, relief="sunken", height=500)
            listbox.pack(side="left", fill="y", expand=True)
            self.lb[i] = listbox

        for i, dat in enumerate(rows[0]):

            try:
                self.lb[i].insert(i, dat)
                self.lb[i].itemconfig(0, {'bg': 'black'})
                self.lb[i].itemconfig(0, {'foreground': 'wheat'})
                self.lb[i].configure(justify=CENTER)
            except Exception as e:
                pass


root = tk.Tk()

frame = ScrollableFrame(root)




frame.pack()
root.mainloop()