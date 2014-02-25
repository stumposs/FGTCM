"""
This file contains classes and methods responsible for the storage and 
manipulation of flight gear data
"""
import re

class FGObject(object):
	def __init__(self, id, props):
	    self.id = id
	    self.prop_list = props

	def updateFromMessage(self,list):
	    for item in list:
	        self.prop_list[item] = list[item]

def parse(string):
    
    playerRecordsList = re.split("&",string)
    print("length of list is: %s"% len(playerRecordsList))
    playerPropDictList = []
    
    
    for prop in playerRecordsList:
        props = re.split(",",prop)
        
        propDict = {}
        for pair in props:
            kv = re.split(" ",pair)
            if len(kv) == 2:
                propDict[kv[0]] = kv[1]
        playerPropDictList.append(propDict)
    return playerPropDictList