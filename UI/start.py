import tkinter as tk

class main:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Social Distancing Alarm System')
        # setting the window to max size of the window
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (w, h))

    def start(self):

            tk.Label(self.root,
                    text="SOCIAL DISTANCING DETECTION AND ALARM SYSTEM",
                    fg="green",
                    pady=100,
                    font="Helvetica 50 bold ").pack()
            tk.Label(self.root,
                    text="""This system connects with your surveillance system and detects human beings captured in the video.
                    On processing the video stream, it displays whether the humans are maintaining safe distance between them or not.""",
                    fg="blue",
                    font="Helvetica 20",
                    justify=tk.CENTER).pack()

            tk.Button(self.root,
                    text="Click To Initialise",
                    relief='raised',
                    fg='green',
                    font="Helvetica 30 bold ",
                    height=3,
                    highlightcolor='light green',
                    pady='4',
                    padx='10'
                    ).pack()

            self.root.mainloop()

main().start()
