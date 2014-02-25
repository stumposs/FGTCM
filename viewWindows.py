'''
This class contains objects and methods relevant to the child windows 
of the main frame. 
'''
import wx

class FGObserver(object):
    def __init__(self, fgObjects):
        super(FGObserver,self,fgObjects).__init__()
        self.fgObjects = fgObjects

    def Observe(self):
        return

class FGViewEnvironment(wx.ScrolledWindow, FGObserver):
    def __init__(self, parent, fgObjects):
        self.parent = parent
        wx.ScrolledWindow.__init__(self,parent,-1,style=wx.TAB_TRAVERSAL)
        self.inc = 0

    def Observe(self):
        self.inc = self.inc + 1
        t = wx.StaticText(self,label=str(self.inc))

class FGViewStatistics(wx.ScrolledWindow, FGObserver):
    def __init__(self, parent, fgObjects):
        self.parent = parent
        wx.ScrolledWindow.__init__(self,parent,-1, style=wx.TAB_TRAVERSAL)
        self.inc = 0
        
    def Observe(self):
        self.inc = self.inc + 1
        t = wx.StaticText(self,label=str(self.inc))

class FGViewMonitorMap(wx.Window,FGObserver):
    def __init__(self, parent):
        self.parent = parent
        wx.ScrolledWindow.__init__(self,parent,-1, style=wx.TAB_TRAVERSAL)
        
        
    def Observe(self):
        self.inc = self.inc + 1
        t = wx.StaticText(self,label=str(self.inc))
        '''
        For example, loop through fgObjects and draw markers at each location using 
        coordinates = self.fgObject
        '''