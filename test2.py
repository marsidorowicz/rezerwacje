import  tkinter

mainWindow = tkinter.Tk()

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
button_new_reservation = tkinter.Button(button_frame, text="Dodaj rezerwację", fg="black", command=lambda: replace_main_frame("BBB"))
button_new_reservation.grid(row=0, column=0)


def replace_main_frame(content):
    test1.set(content)


# tkinter.Label(main_frame, text="ABC", relief="raised").pack(side="left")
test1 = tkinter.StringVar()
test1.set("ABC")
result = tkinter.Label(main_frame, textvariable=test1)
result.grid(row=1, column=1, sticky="nsew", rowspan=5)

mainWindow.mainloop()