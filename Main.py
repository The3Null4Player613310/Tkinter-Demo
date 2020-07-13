import tkinter as tk


class Test(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.setup_window()
        self.create_widgets()

    def setup_window(self):
        self.master.title("Tkinter Test")
        self.master.geometry("900x650+0+0")

    def create_widgets(self):
        print("making widgets")

        # label code below

        text = tk.Label(self, text="FooBar")
        text.pack()

        # button code below

        button = tk.Button(self, text='Foo', command=None)
        button.pack()

        # checkbox code below

        foobar = tk.StringVar()

        label = tk.Label(self, textvariable=foobar)
        label.pack()

        checkfoo = tk.Checkbutton(self, variable=foobar, onvalue='foo', offvalue='')
        checkfoo.pack()
        checkbar = tk.Checkbutton(self, variable=foobar, onvalue='bar', offvalue='')
        checkbar.pack()


root = tk.Tk()
test = Test(root)
test.mainloop()
