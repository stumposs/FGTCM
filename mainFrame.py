import wx
import viewWindows
from viewWindows import *
from fg import FGObject
'''
This is the main frame class
'''
class FGFrame(wx.Frame):
	def __init__(self,*args,**kwargs):
		super(FGFrame,self).__init__(*args,**kwargs)
		self.fgObjects = {}
		vertSizer = wx.BoxSizer(wx.VERTICAL)
		horiSizer = wx.BoxSizer(wx.HORIZONTAL)
		self.viewEnvironment = FGViewEnvironment(self,self.fgObjects)
		vertSizer.Add(self.viewEnvironment,2,wx.EXPAND)
		self.SetSizer(vertSizer)

		self.viewStats = FGViewStatistics(self,self.fgObjects)
		horiSizer.Add(self.viewStats,3,wx.EXPAND)
		self.SetSizer(horiSizer)

		self.fglisteners = [self.viewStats, self.viewEnvironment]

	def updateFGObjs(self, string):
		if string is not None:
			fgPlayerDictsList = fg.parse(string)
			if len(fgPlayerDictsList) == 0:
				return
			for playerDict in fgPlayerDictsList:
				if "playername" not in playerDict:
					continue
				else:
					playerid = playerDict["playername"]
					if playerid in self.fgObjects:
						self.fgObjects[playerid].updateFromMessage(playerDict)
						for view in self.fglisteners:
						    view.Observe()
					else:
						newPlayer = FGObject(playerid, playerDict)
						self.fgObjects[playerid] = newPlayer