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
        print("widgets go here")


root = tk.Tk()
test = Test(root)
test.mainloop()