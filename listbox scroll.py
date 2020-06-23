from tkinter import *

def onselect(event):
    w = event.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    info = find_info(value)
    listSelection.delete(0, END)
    listSelection.insert(END, "Node ID: " + info[0])
    listSelection.insert(END, "Owner/Description: " + info[1])
    listSelection.insert(END, "Last Latitude: " + info[2])
    listSelection.insert(END, "Last Longitude: " + info[3])



mapNodes = "http://ukhas.net/api/mapNodes"
nodeData = "http://ukhas.net/api/nodeData"
current_id = 0

window = Tk() # create window
window.configure(bg='lightgrey')
window.title("UKHASnet Node Manager")
window.geometry("680x400")

lbl1 = Label(window, text="Node List:", fg='black', font=("Helvetica", 16, "bold"))
lbl2 = Label(window, text="Node Information:", fg='black', font=("Helvetica", 16,"bold"))
lbl1.place(x=0, y=0)
lbl2.place(x=200, y=0)

scrollbar = Scrollbar(window, orient="vertical")
listNodes = Listbox(window, width=20, height=20, yscrollcommand=scrollbar.set, font=("Helvetica", 12))
scrollbar.config(command=listNodes.yview)
scrollbar.pack(side="right", fill="y")

listSelection = Listbox(window, width=50, height=4, font=("Helvetica", 12))

# pack objects onto window
listNodes.place(x=1, y=40)
listSelection.place(x=200, y=40)

window.mainloop()