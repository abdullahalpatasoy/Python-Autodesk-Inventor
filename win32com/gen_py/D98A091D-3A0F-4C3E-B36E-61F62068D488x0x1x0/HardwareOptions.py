# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.00
# By python version 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Tue Nov 17 17:41:12 2015
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

from win32com.client import DispatchBaseClass
class HardwareOptions(DispatchBaseClass):
	"""HardwareOptions Object"""
	CLSID = IID('{9A19AF07-A6BF-43AA-ABF3-870CA1CF329F}')
	coclass_clsid = None

	_prop_map_get_ = {
		"Application": (2130706433, 2, (9, 0), (), "Application", None),
		"Diagnostics": (50406661, 2, (8, 0), (), "Diagnostics", None),
		"GraphicsDriverType": (50406660, 2, (3, 0), (), "GraphicsDriverType", None),
		"GraphicsOptimization": (50406659, 2, (3, 0), (), "GraphicsOptimization", None),
		"GraphicsSettingType": (50406662, 2, (3, 0), (), "GraphicsSettingType", None),
		"Type": (2130706435, 2, (3, 0), (), "Type", None),
		"UseSoftwareGraphics": (50406663, 2, (11, 0), (), "UseSoftwareGraphics", None),
		"WarnForDriverErrors": (50406658, 2, (11, 0), (), "WarnForDriverErrors", None),
		"WarnForUnrecommendedDriver": (50406657, 2, (11, 0), (), "WarnForUnrecommendedDriver", None),
	}
	_prop_map_put_ = {
		"GraphicsDriverType": ((50406660, LCID, 4, 0),()),
		"GraphicsOptimization": ((50406659, LCID, 4, 0),()),
		"GraphicsSettingType": ((50406662, LCID, 4, 0),()),
		"UseSoftwareGraphics": ((50406663, LCID, 4, 0),()),
		"WarnForDriverErrors": ((50406658, LCID, 4, 0),()),
		"WarnForUnrecommendedDriver": ((50406657, LCID, 4, 0),()),
	}

win32com.client.CLSIDToClass.RegisterCLSID( "{9A19AF07-A6BF-43AA-ABF3-870CA1CF329F}", HardwareOptions )
