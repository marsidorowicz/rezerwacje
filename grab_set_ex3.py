from tkinter import *


class GUI(Frame):

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.my_frame = Frame(self.master)
        self.my_frame.pack()
        self.master.geometry("1000x1000")
        self.button1 = Button(self.master, text="Open New Window",
                              command=OpenToplevelWindow)
        self.button1.pack()

        self.text = Text(self.master, width = 20, height = 3)
        self.text.pack()
        self.text.insert(END, "Before\ntop window\ninteraction")


class OpenToplevelWindow(Toplevel):

    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)
        self.grab_set()
        self.geometry("1000x1000")

        def replace_text():
            app.text.delete(1.0, END)
            app.text.insert(END, "Text From\nToplevel")

        top_button = Button(self, text = "Replace text in main window",
                            command = replace_text)
        top_button.pack()


if __name__ == "__main__":
    root = Tk()
    app = GUI(root)
    root.mainloop()