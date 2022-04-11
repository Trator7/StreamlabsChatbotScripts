#!/usr/bin/python
# -*- coding: utf-8 -*-

""" Support After Raid
    1.0.0 Initial public release
"""

#---------------------------------------
# Import Libraries
#---------------------------------------
import clr
clr.AddReference("IronPython.Modules.dll")

import os
import json
import re
import io
from collections import deque

#---------------------------------------
# [Required] Script Information
#---------------------------------------
ScriptName = "Support After Raid"
Website = "http://www.twitch.tv/trator7"
Description = "Write a support message for another streamer after a raid"
Creator = "Trator"
Version = "1.0.0"

#---------------------------------------
# Classes
#---------------------------------------
class Settings(object):
    """ Load in saved settings file if available else set default values. """
    def __init__(self):
        self.path = os.path.join(os.path.dirname(__file__), "greetings.txt")
        self.Load_Greetings()

    def Reload(self):
        self.Load_Greetings()
    
    def Load_Greetings(self):
        self.greetings = {}
        with io.open(self.path, "r", encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                user, message = line.split("|$")
                self.greetings[str.lower(user)] = message

    def Save(self, settingsfile):
        return

#---------------------------------------
# Global Variables
#---------------------------------------
# Settings file path
ScriptSettings = None
# Raider RawData
reUserNotice = re.compile(r"(?:^(?:@(?P<irctags>[^\ ]*)\ )?:tmi\.twitch\.tv\ USERNOTICE)")

#---------------------------------------
# Functions
#---------------------------------------
def EnqueueAudioFile(audiofile):
    return

#---------------------------------------
# [Required] Intialize Data (Only called on Load)
#---------------------------------------
def Init():
    # Globals
    global ScriptSettings
    # Load in saved settings
    ScriptSettings = Settings()
    # End of Init
    return

#---------------------------------------
# [Optional] Reload Settings
#---------------------------------------
def ReloadSettings(jsondata):
    # Reload newly saved settings
    ScriptSettings.Reload()
    # End of ReloadSettings
    return

#---------------------------------------
# [Required] Execute Data / Process Messages
#---------------------------------------
def Execute(data):
    # Raw IRC message from Twitch
    if data.IsRawData() and data.IsFromTwitch():
        # Apply regex on raw data to detect raid usernotice
        usernotice = reUserNotice.search(data.RawData)
        if usernotice:
            tags = dict(re.findall(r"([^=]+)=([^;]*)(?:;|$)", usernotice.group("irctags")))
            id = tags['msg-id']
            if (id == 'raid'):
                displayName = tags['msg-param-displayName']
                viewerCount = tags['msg-param-viewerCount']
                
                if(displayName.lower() in ScriptSettings.greetings.keys()):
                    Parent.SendTwitchMessage(ScriptSettings.greetings[displayName.lower()].format(displayName))
                else:
                    Parent.SendTwitchMessage(ScriptSettings.greetings["default"].format(displayName))
    return

#---------------------------------------
# [Required] Tick Function
#---------------------------------------
def Tick():
    return