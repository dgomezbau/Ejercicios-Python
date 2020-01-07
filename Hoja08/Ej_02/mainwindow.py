import wx

class MyFrame(wx.Frame): #herencia    
    def __init__(self): 
        super().__init__(parent=None, title='Hello World') #constructor padre
        panel = wx.Panel(self) #creamos panel con parent component este mismo frame
        my_sizer = wx.BoxSizer(wx.VERTICAL)

        my_btn = wx.Button(panel, label='Pulsa\nme', pos=(5, 55))
        my_sizer.Add(my_btn, 0, wx.ALL | wx.EXPAND, 5)
        panel.SetSizer(my_sizer)

        self.Show()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()