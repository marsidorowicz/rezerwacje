import tkinter as tk

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

                    # index = (self.rows, column)
                    # self._entry[index].insert(0, i)
                    # i += 1
            # for row in range(self.rows):
            #     current_row = []
            #     for column in range(self.columns):
            #         index = (row, column)
            #         for i in range(10):
            #             stri = str(i)
            #             self._entry[index].insert(0, stri)
            #             column += 1
            #         row += 1


    def get(self):
        '''Return a list of lists, containing the data in the table'''
        result = []
        for row in range(self.rows):
            current_row = []
            for column in range(self.columns):
                index = (row, column)
                current_row.append(self._entry[index].get())
            result.append(current_row)
        return result

    def _validate(self, P):
        '''Perform input validation.

        Allow only an empty value, or a value that can be converted to a float
        '''
        if P.strip() == "":
            return True

        try:
            f = float(P)
        except ValueError:
            self.bell()
            return False
        return True

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.table = SimpleTableInput(self, 10, 10)
        self.submit = tk.Button(self, text="Submit", command=self.on_submit)
        self.submit1 = tk.Button(self, text="Fill", command=self.on_submit1)
        self.table.pack(side="top", fill="both", expand=True)
        self.submit.pack(side="bottom")
        self.submit1.pack(side="bottom")

    def on_submit(self):
        print(self.table.get())

    def on_submit1(self):
        print(self.table.put())


root = tk.Tk()
Example(root).pack(side="top", fill="both", expand=True)
root.mainloop()