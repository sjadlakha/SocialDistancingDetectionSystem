import tkinter as tk
from tkinter import ttk
from human_detection_cascade import humanDetection

class tkinterApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        container  = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, DistancePage):
            frame = F(container, self)

            self.frames[F] =  frame
            frame.grid(row=0, column=0, sticky = "nsew")

        self.show_frame(StartPage)
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Label(self,
                 text="SOCIAL DISTANCING DETECTION AND ALARM SYSTEM",
                 fg="green",
                 pady=100,
                 font="Helvetica 50 bold ").pack()
        tk.Label(self,
                 text="""This system connects with your surveillance system and detects human beings captured in the video.
                    On processing the video stream, it displays whether the humans are maintaining safe distance between them or not.""",
                 fg="blue",
                 font="Helvetica 20",
                 justify=tk.CENTER).pack()

        tk.Button(self,
                  text="Click To Initialise",
                  relief='raised',
                  fg='green',
                  font="Helvetica 30 bold ",
                  height=3,
                  highlightcolor='light green',
                  pady='4',
                  padx='10',
                  command= lambda : controller.show_frame(DistancePage)
                  ).pack()


class DistancePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.val = 1
        tk.Label(self,
                 text="SOCIAL DISTANCING DETECTION AND ALARM SYSTEM",
                 fg="green",
                 pady=100,
                 font="Helvetica 50 bold ").pack()
        tk.Label(self,
                 text="""Enter The Minimum Distance""",
                 fg="blue",
                 font="Helvetica 20",
                 justify=tk.CENTER).pack()

        v = tk.Entry(
            self,
            bd=2,
            highlightcolor='light blue'
        )
        v.pack()

        def validateEntry():
            x = v.get()
            
            if x.isdigit() and len(x) <= 2:
                if int(x) > self.val and int(x) <= 15:
                    p_button["state"] = "normal"
                    INPUT_DISTANCE = int(x)
                else:
                    p_button["state"] = "disabled"
            else:
                p_button["state"] = "disabled"

        check_button = tk.Button(self,
                                 text='Check Validity',
                                 fg='green',
                                 pady=10,
                                 padx=10,
                                 font='Helvetica 20',
                                 command= validateEntry)
        check_button.pack(pady=10)

        p_button = tk.Button(self,
                             text='Proceed',
                             fg='green',
                             pady=10,
                             padx=10,
                             state="disabled",
                             font='Helvetica 30',
                             command= lambda : humanDetection(int(v.get())*100)
                             )
        p_button.pack(pady=20)


app = tkinterApp()
app.mainloop()