import wx

class MyFrame(wx.Frame): #herencia    
    def __init__(self): 
        super().__init__(parent=None, title='Hello World') #constructor padre
        panel = wx.Panel(self) #creamos panel con parent component este mismo frame

        self.Show()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()