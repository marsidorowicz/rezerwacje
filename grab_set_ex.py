import tkinter as tk


class Main(tk.Tk):

    def __init__(self,*args, **kwargs):
        tk.Tk.__init__(self,*args, *kwargs)

        button = tk.Button(self,text="second window", command=lambda: Settings())
        button.pack()


class Settings(tk.Tk):

    def __init__(self,*args, **kwargs):
        tk.Tk.__init__(self,*args, *kwargs)
        button = tk.Button(self,text="quit", command=lambda: quit())
        button.pack()
        self.grab_set()


if __name__ == "__main__":
    app = Main()
    app.mainloop()