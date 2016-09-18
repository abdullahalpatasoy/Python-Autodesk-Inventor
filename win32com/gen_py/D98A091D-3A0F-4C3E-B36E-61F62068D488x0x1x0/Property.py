# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.00
# By python version 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Wed Nov 18 12:15:32 2015
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
class Property(DispatchBaseClass):
	"""Object that represents Property"""
	CLSID = IID('{73F35CC9-ED6E-11D2-B785-0060B0F159EF}')
	coclass_clsid = None

	def Delete(self):
		"""Deletes this Property from its Property Set"""
		return self._oleobj_.InvokeTypes(50339076, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Dirty": (50339077, 2, (11, 0), (), "Dirty", None),
		"DisplayName": (50339078, 2, (8, 0), (), "DisplayName", None),
		"Expression": (50339079, 2, (8, 0), (), "Expression", None),
		"Name": (50339074, 2, (8, 0), (), "Name", None),
		# Method 'Parent' returns object of type 'PropertySet'
		"Parent": (2130706434, 2, (9, 0), (), "Parent", '{73F35CC7-ED6E-11D2-B785-0060B0F159EF}'),
		"PropId": (50339073, 2, (3, 0), (), "PropId", None),
		"Type": (2130706435, 2, (3, 0), (), "Type", None),
		"Value": (50339075, 2, (12, 0), (), "Value", None),
	}
	_prop_map_put_ = {
		"DisplayName": ((50339078, LCID, 4, 0),()),
		"Expression": ((50339079, LCID, 4, 0),()),
		"Value": ((50339075, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(50339075, 2, (12, 0), (), "Value", None))
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

win32com.client.CLSIDToClass.RegisterCLSID( "{73F35CC9-ED6E-11D2-B785-0060B0F159EF}", Property )
