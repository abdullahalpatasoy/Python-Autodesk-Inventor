# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.00
# By python version 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Tue Nov 17 17:32:51 2015
"""Autodesk Inventor Object Library"""
makepy_version = '0.5.00'
python_version = 0x2070af0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{D98A091D-3A0F-4C3E-B36E-61F62068D488}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

from win32com.client import CoClassBaseClass
import sys
__import__('win32com.gen_py.D98A091D-3A0F-4C3E-B36E-61F62068D488x0x1x0.UserInputEventsSink')
UserInputEventsSink = sys.modules['win32com.gen_py.D98A091D-3A0F-4C3E-B36E-61F62068D488x0x1x0.UserInputEventsSink'].UserInputEventsSink
__import__('win32com.gen_py.D98A091D-3A0F-4C3E-B36E-61F62068D488x0x1x0.UserInputEventsObject')
UserInputEventsObject = sys.modules['win32com.gen_py.D98A091D-3A0F-4C3E-B36E-61F62068D488x0x1x0.UserInputEventsObject'].UserInputEventsObject
class UserInputEvents(CoClassBaseClass): # A CoClass
	# User Input Events Object
	CLSID = IID('{9235396D-0350-11D3-B787-0060B0F159EF}')
	coclass_sources = [
		UserInputEventsSink,
	]
	default_source = UserInputEventsSink
	coclass_interfaces = [
		UserInputEventsObject,
	]
	default_interface = UserInputEventsObject

win32com.client.CLSIDToClass.RegisterCLSID( "{9235396D-0350-11D3-B787-0060B0F159EF}", UserInputEvents )
