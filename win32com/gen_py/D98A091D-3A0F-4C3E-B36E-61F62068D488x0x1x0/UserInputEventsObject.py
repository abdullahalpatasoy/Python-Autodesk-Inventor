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

from win32com.client import DispatchBaseClass
class UserInputEventsObject(DispatchBaseClass):
	"""User Input Events Object"""
	CLSID = IID('{2772058F-17D8-4969-8D46-51860F09AC9B}')
	coclass_clsid = IID('{9235396D-0350-11D3-B787-0060B0F159EF}')

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2130706433, 2, (9, 0), (), "Application", '{70109AA0-63C1-11D2-B78B-0060B0EC020B}'),
		# Method 'Parent' returns object of type 'CommandManager'
		"Parent": (2130706434, 2, (9, 0), (), "Parent", '{9C88D3A9-C3EB-11D3-B79E-0060B0F159EF}'),
		"Type": (0, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Type'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (3, 0), (), "Type", None))
	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

win32com.client.CLSIDToClass.RegisterCLSID( "{2772058F-17D8-4969-8D46-51860F09AC9B}", UserInputEventsObject )
