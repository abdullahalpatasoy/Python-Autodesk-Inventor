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

from win32com.client import DispatchBaseClass
class ButtonDefinitionObject(DispatchBaseClass):
	"""Represents a ButtonDefinition object"""
	CLSID = IID('{DBADC913-8652-4B4E-B13E-B356CC4E9BEE}')
	coclass_clsid = IID('{CD3A37C9-E647-41AA-B0D9-4EED2A875789}')

	def AutoAddToGUI(self):
		"""Adds it to AddIn Toolbar"""
		return self._oleobj_.InvokeTypes(50371086, LCID, 1, (24, 0), (),)

	def Delete(self):
		"""Method that deletes the UIDefinition Object"""
		return self._oleobj_.InvokeTypes(50371075, LCID, 1, (24, 0), (),)

	def Execute(self):
		"""Executes this ControlDefinition object"""
		return self._oleobj_.InvokeTypes(50371089, LCID, 1, (24, 0), (),)

	def Execute2(self, Synchronous=defaultNamedNotOptArg):
		"""Executes the ControlDefinition synchronously or asynchronously"""
		return self._oleobj_.InvokeTypes(50371097, LCID, 1, (24, 0), ((11, 1),),Synchronous
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2130706433, 2, (9, 0), (), "Application", '{70109AA0-63C1-11D2-B78B-0060B0EC020B}'),
		"BuiltIn": (50371073, 2, (11, 0), (), "BuiltIn", None),
		"Classification": (50371085, 2, (3, 0), (), "Classification", None),
		"ClientId": (50371094, 2, (8, 0), (), "ClientId", None),
		# Method 'ControlDefinitionEvents' returns object of type 'ControlDefinitionEvents'
		"ControlDefinitionEvents": (50371090, 2, (13, 0), (), "ControlDefinitionEvents", '{BEB3104E-2019-49E0-BC17-F5759998D9FE}'),
		"DefaultShortcut": (50371098, 2, (8, 0), (), "DefaultShortcut", None),
		"DefaultShortcutType": (50371099, 2, (3, 0), (), "DefaultShortcutType", None),
		"DefinitionType": (50371091, 2, (3, 0), (), "DefinitionType", None),
		"DescriptionText": (50371076, 2, (8, 0), (), "DescriptionText", None),
		"DisplayName": (50371088, 2, (8, 0), (), "DisplayName", None),
		"Enabled": (50371077, 2, (11, 0), (), "Enabled", None),
		"Id": (50371081, 2, (3, 0), (), "Id", None),
		"InternalName": (50371087, 2, (8, 0), (), "InternalName", None),
		"IsShortcutOverridden": (50371100, 2, (11, 0), (), "IsShortcutOverridden", None),
		# Method 'LargeIcon' returns object of type 'Picture'
		"LargeIcon": (50371093, 2, (9, 0), (), "LargeIcon", '{7BF80981-BF32-101A-8BBB-00AA00300CAB}'),
		"OverrideShortcut": (50371101, 2, (8, 0), (), "OverrideShortcut", None),
		"OverrideShortcutType": (50371102, 2, (3, 0), (), "OverrideShortcutType", None),
		# Method 'Parent' returns object of type 'CommandManager'
		"Parent": (2130706434, 2, (9, 0), (), "Parent", '{9C88D3A9-C3EB-11D3-B79E-0060B0F159EF}'),
		"Pressed": (50371590, 2, (11, 0), (), "Pressed", None),
		# Method 'ProgressiveToolTip' returns object of type 'ProgressiveToolTip'
		"ProgressiveToolTip": (50371103, 2, (9, 0), (), "ProgressiveToolTip", '{5189E676-CC1A-4901-98E7-EC85130FDB63}'),
		# Method 'StandardIcon' returns object of type 'Picture'
		"StandardIcon": (50371092, 2, (9, 0), (), "StandardIcon", '{7BF80981-BF32-101A-8BBB-00AA00300CAB}'),
		"ToolTipText": (50371082, 2, (8, 0), (), "ToolTipText", None),
		"Type": (2130706435, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
		"DefaultShortcut": ((50371098, LCID, 4, 0),()),
		"DescriptionText": ((50371076, LCID, 4, 0),()),
		"Enabled": ((50371077, LCID, 4, 0),()),
		"LargeIcon": ((50371093, LCID, 4, 0),()),
		"OverrideShortcut": ((50371101, LCID, 4, 0),()),
		"Pressed": ((50371590, LCID, 4, 0),()),
		"StandardIcon": ((50371092, LCID, 4, 0),()),
		"ToolTipText": ((50371082, LCID, 4, 0),()),
	}

win32com.client.CLSIDToClass.RegisterCLSID( "{DBADC913-8652-4B4E-B13E-B356CC4E9BEE}", ButtonDefinitionObject )
