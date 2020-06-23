import tkinter as tk

root = tk.Tk()

listbox = tk.Listbox(root)
listbox.grid(row=0, column=0, sticky="news")

scrollbar = tk.Scrollbar(root, orient='vertical', command=listbox.yview)
scrollbar.grid(row=0, column=1, sticky='ns')

listbox.config(yscrollcommand=scrollbar.set)

# add some values to listbox for scrolling
for i in range(50):
    listbox.insert('end', str(i))

root.mainloop()