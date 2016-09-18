# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.00
# By python version 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Wed Nov 18 08:47:11 2015
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
__import__('win32com.gen_py.D98A091D-3A0F-4C3E-B36E-61F62068D488x0x1x0._VbaImplementationEvents')
_VbaImplementationEvents = sys.modules['win32com.gen_py.D98A091D-3A0F-4C3E-B36E-61F62068D488x0x1x0._VbaImplementationEvents']._VbaImplementationEvents
__import__('win32com.gen_py.D98A091D-3A0F-4C3E-B36E-61F62068D488x0x1x0.Document')
Document = sys.modules['win32com.gen_py.D98A091D-3A0F-4C3E-B36E-61F62068D488x0x1x0.Document'].Document
class _Document(CoClassBaseClass): # A CoClass
	CLSID = IID('{0249C8A3-806D-4A1D-8BC0-4699BE1203AF}')
	coclass_sources = [
		_VbaImplementationEvents,
	]
	default_source = _VbaImplementationEvents
	coclass_interfaces = [
		Document,
	]
	default_interface = Document

win32com.client.CLSIDToClass.RegisterCLSID( "{0249C8A3-806D-4A1D-8BC0-4699BE1203AF}", _Document )
