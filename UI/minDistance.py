from tkinter import *
import tkinter as tk


class minDist:
    def __init__(self):
        self.root = tk.Tk()
        # setting the window to max size of the window
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (w, h))
        self.val = 2

    def start(self):

        tk.Label(self.root,
                 text="SOCIAL DISTANCING DETECTION AND ALARM SYSTEM",
                 fg="green",
                 pady=100,
                 font="Helvetica 50 bold ").pack()
        tk.Label(self.root,
                 text="""Enter The Minimum Distance. Only 2 Digit Integer Values Are Allowed.""",
                 fg="blue",
                 font="Helvetica 20",
                 justify=tk.CENTER).pack()

        v = tk.Entry(
            self.root,
            bd=2,
            highlightcolor='light blue'
        )
        v.pack()

        def validateEntry():
            x = v.get()
            if x.isdigit() and len(x) <= 2:
                if int(x) > self.val:
                    p_button["state"] = "normal"
                else:
                    p_button["state"] = "disabled"
            else:
                p_button["state"] = "disabled"

        check_button = tk.Button(self.root,
                             text='Check Validity',
                             fg='green',
                             pady=10,
                             padx=10,
                             font='Helvetica 20',
                             command=validateEntry)
        check_button.pack(pady=10)

        p_button = tk.Button(self.root,
                             text='Proceed',
                             fg='green',
                             pady=10,
                             padx=10,
                             state="disabled",
                             font='Helvetica 30')
        p_button.pack(pady=20)

        self.root.mainloop()

# minDist().start()
