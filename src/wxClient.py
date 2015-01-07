'''
Created on 7 janv. 2015

@author: humble_jok
'''
from wx._core import App, BoxSizer, VERTICAL, EXPAND, FlexGridSizer,\
    ALIGN_CENTER_VERTICAL, ALL, StdDialogButtonSizer, ID_OK, ALIGN_CENTER,\
    ID_ANY, DefaultPosition, DefaultSize
from wx._windows import Dialog, Panel, Frame, DEFAULT_FRAME_STYLE
from wx._controls import TextCtrl, StaticText, Button

class WxLogin(Dialog):
    def __init__(self, *args, **kwargs):
        super(WxLogin, self).__init__(*args, **kwargs)
        self.panel = WxLoginPanel(self)
        sizer = BoxSizer(VERTICAL)
        sizer.Add(self.panel, 1, EXPAND)
        self.SetSizer(sizer)
        self.SetInitialSize()

class WxLoginPanel(Panel):
    def __init__(self, parent):
        super(WxLoginPanel, self).__init__(parent)
        
        self._username = TextCtrl(self)
        
        sizer = FlexGridSizer(2, 2, 8, 8)
        sizer.Add(StaticText(self, label='Your name:'), 0, ALIGN_CENTER_VERTICAL)
        sizer.Add(self._username, 0, EXPAND)
        
        msizer = BoxSizer(VERTICAL)
        msizer.Add(sizer, 1, EXPAND|ALL, 20)
        btnszr = StdDialogButtonSizer()
        button = Button(self, ID_OK)
        button.SetDefault()
        btnszr.AddButton(button)
        msizer.Add(btnszr, 0, ALIGN_CENTER|ALL, 12)
        btnszr.Realize()
        self.SetSizer(msizer)
        
    def get_username(self):
        return self._username.GetValue()

class WxLoginFrame(Frame):
    def __init__(self, parent, id=ID_ANY, title='Login',
                 pos=DefaultPosition, size=DefaultSize,
                 style=DEFAULT_FRAME_STYLE, name='LoginFrame'):
        super(WxLoginFrame, self).__init__(parent, id, title, pos, size, style, name)
        self.panel = WxLoginPanel(self)
        
class WxClient(App):
    def OnInit(self):
        self.frame = WxLoginFrame(None)
        self.SetTopWindow(self.frame)
        self.frame.Show()
        
        return True

if __name__ == "__main__":
    app = WxClient(False)
    app.MainLoop()
