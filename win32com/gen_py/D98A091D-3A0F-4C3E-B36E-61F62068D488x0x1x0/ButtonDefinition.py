# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.00
# By python version 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Tue Nov 17 17:18:31 2015
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
__import__('win32com.gen_py.D98A091D-3A0F-4C3E-B36E-61F62068D488x0x1x0.ButtonDefinitionSink')
ButtonDefinitionSink = sys.modules['win32com.gen_py.D98A091D-3A0F-4C3E-B36E-61F62068D488x0x1x0.ButtonDefinitionSink'].ButtonDefinitionSink
__import__('win32com.gen_py.D98A091D-3A0F-4C3E-B36E-61F62068D488x0x1x0.ButtonDefinitionObject')
ButtonDefinitionObject = sys.modules['win32com.gen_py.D98A091D-3A0F-4C3E-B36E-61F62068D488x0x1x0.ButtonDefinitionObject'].ButtonDefinitionObject
class ButtonDefinition(CoClassBaseClass): # A CoClass
	# Represents a ButtonDefinition object
	CLSID = IID('{CD3A37C9-E647-41AA-B0D9-4EED2A875789}')
	coclass_sources = [
		ButtonDefinitionSink,
	]
	default_source = ButtonDefinitionSink
	coclass_interfaces = [
		ButtonDefinitionObject,
	]
	default_interface = ButtonDefinitionObject

win32com.client.CLSIDToClass.RegisterCLSID( "{CD3A37C9-E647-41AA-B0D9-4EED2A875789}", ButtonDefinition )
