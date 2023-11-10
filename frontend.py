import wx

import yt_dlp

import moviepy.editor as mp

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Hello World')
        panel = wx.Panel(self)
        self.text_ctrl = wx.TextCtrl(panel, pos=(135, 35))
        my_btn = wx.Button(panel, label='Download Mp4', pos=(5, 55) )
        my_bt = wx.Button(panel, label='Download Mp3', pos=(5, 85) )
        my_bt.Bind(wx.EVT_BUTTON, self.on_presstwo)
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        self.Show()
    def on_press(self, event):
        value = self.text_ctrl.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            ydl_opts = {}

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([value])

            print("video downloaded succesfully")
    def on_presstwo(self, event):
        value = self.text_ctrl.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            clip = mp.VideoFileClip(value)

            clip.audio.write_audiofile("The reason")

app = wx.App()
frame = MyFrame()
app.MainLoop()