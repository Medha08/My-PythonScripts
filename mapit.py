import webbrowser
from tkinter import *
class SampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.entry = Entry(self,width=500)
        self.entry.pack()
        self.button = Button(self, text="Search", command=self.on_button)
        self.button.pack()


    def on_button(self):
        webbrowser.open('https://www.google.com/maps/place/' + self.entry.get())

app = SampleApp()
app.mainloop()