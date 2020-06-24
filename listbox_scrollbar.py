# import tkinter as tk
#
# root = tk.Tk()
#
# listbox = tk.Listbox(root)
# listbox.grid(row=0, column=0, sticky="news")
#
# scrollbar = tk.Scrollbar(root, orient='vertical', command=listbox.yview)
# scrollbar.grid(row=0, column=1, sticky='ns')
#
# listbox.config(yscrollcommand=scrollbar.set)
#
# # add some values to listbox for scrolling
# for i in range(50):
#     listbox.insert('end', str(i))
#
# root.mainloop()


# Its worth noting that when you bind the event is passed to the function that gets called anyway, so you could change your code to remove the lambdas something like this:

import tkinter as tk

class Menu(tk.Listbox):
    def __init__(self, master, items, *args, **kwargs):
        tk.Listbox.__init__(self, master, exportselection = False, *args, **kwargs)
        self.pack()

        for item in items:
            self.insert(tk.END, item)

        self.bind('<Enter>',  self.snapHighlightToMouse)
        self.bind('<Motion>', self.snapHighlightToMouse)
        self.bind('<Leave>',  self.unhighlight)

    def snapHighlightToMouse(self, event):
        self.selection_clear(0, tk.END)
        self.selection_set(self.nearest(event.y))

    def unhighlight(self, event=None):
        self.selection_clear(0, tk.END)

m = Menu(None, ['Alice', 'Bob', 'Caroline'])

tk.mainloop()