import requests,bs4,webbrowser
from tkinter import *
class SampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.entry=Entry(self)
        self.entry.pack()
        self.entry.focus_set()
        self.button = Button(self,text="Chordify",width=10,command=self.on_button)
        self.button.pack()
        self.button =Button(self,text="Download",width=10,command=self.on_download)
        self.button.pack()

    def on_button(self):
        res = requests.get('http://google.com/search?q=' + self.entry.get()+'chords')
        try:
            res.raise_for_status()
        except Exception as exec:
            print("Check your Internet Connection!%s"%(exec))
        soup = bs4.BeautifulSoup(res.text)
        links = soup.select('.r a')
        webbrowser.open('http://google.com'+links[0].get('href'))

    def on_download(self):
        res = requests.get('http://google.com/search?q=' + self.entry.get() + 'chords')
        try:
            res.raise_for_status()
        except Exception as exec:
            print("Check your Internet Connection!%s" % (exec))
        soup = bs4.BeautifulSoup(res.text)
        links = soup.select('.r a')
        name = self.entry.get()+'.htm'
        res2 = requests.get(('http://google.com'+links[0].get('href')))
        down = open(name, 'wb')
        down.write(res2.content)
        down.close()







app = SampleApp()
app.mainloop()