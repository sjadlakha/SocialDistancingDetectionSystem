import tkinter
import cv2
import PIL.Image, PIL.ImageTk

class AreaVideoCapture:
    def __init__(self, video_source = 0):
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open connected video source: ", video_source)

        # Get dimensioons of the input footage to create a window accordingly
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    
    # Releasing the video source on closing the window
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
        cv2.destroyAllWindows()


    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
            else:
                return (ret, None)
        else:
            return (0, None)


class App:
    def __init__(self, window, window_title, video_source=0):
        self.window= window
        self.window.title(window_title)
        self.video_source = video_source

        self.vid = AreaVideoCapture(video_source)

        # Creating a canvas
        self.canvas = tkinter.Canvas(window, width=self.vid.width, height=self.vid.height)
        self.canvas.pack()

        # Stop Button
        # style = tkinter.ttk.Style()
        self.btn_stop = tkinter.Button(window, text="STOP DETECTION AND EXIT", width=50,
                                       command=self.end, pady=10, fg='white', highlightbackground='brown', font='Helvetica 20 bold')
        self.btn_stop.pack(pady=10, anchor=tkinter.CENTER, expand=True)

        # After calling once, it will be called automatically after given delay in ms
        self.delay = 15
        self.update()

        self.window.mainloop()

    def update(self):
        ret, frame = self.vid.get_frame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)

        self.window.after(self.delay, self.update)

    def end(self):
        self.vid.vid.release()
        self.window.destroy()
        cv2.destroyAllWindows()


App(tkinter.Tk(), "Video Stream")
