# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.00
# By python version 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Wed Nov 18 11:54:05 2015
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
class PropertySets(DispatchBaseClass):
	"""Object that manages the collection of Property Set objects"""
	CLSID = IID('{73F35CC8-ED6E-11D2-B785-0060B0F159EF}')
	coclass_clsid = None

	# Result is of type PropertySet
	def Add(self, Name=defaultNamedNotOptArg, InternalName=defaultNamedOptArg):
		"""Adds a new Property Set. The new set's FMTID can be optionally provided (as a string)"""
		ret = self._oleobj_.InvokeTypes(50338305, LCID, 1, (9, 0), ((8, 1), (12, 17)),Name
			, InternalName)
		if ret is not None:
			ret = Dispatch(ret, u'Add', '{73F35CC7-ED6E-11D2-B785-0060B0F159EF}')
		return ret

	def FlushToFile(self):
		"""Flush all of the Properties in each of the Property Sets onto the File. The 'dirty' flags are reset"""
		return self._oleobj_.InvokeTypes(50338308, LCID, 1, (24, 0), (),)

	# Result is of type PropertySet
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		"""Gets the Setin this collection in a sequences fashion; by index, or by its name -- Display or Internal"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, u'Item', '{73F35CC7-ED6E-11D2-B785-0060B0F159EF}')
		return ret

	def PropertySetExists(self, PropertySetName=defaultNamedNotOptArg, PropertySet=pythoncom.Missing):
		"""Method that returns Boolean to indicate whether a PropertySet with the specified name already exists in the PropertySets collection."""
		return self._ApplyTypes_(50338310, 1, (11, 0), ((8, 1), (16396, 18)), u'PropertySetExists', None,PropertySetName
			, PropertySet)

	def RefreshFromFile(self):
		"""Refresh all of the Properties in each of the Property Sets from the File. The 'dirty' flags are reset and any edits are lost"""
		return self._oleobj_.InvokeTypes(50338307, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Count": (2130706438, 2, (3, 0), (), "Count", None),
		"Dirty": (50338309, 2, (11, 0), (), "Dirty", None),
		"Parent": (2130706434, 2, (9, 0), (), "Parent", None),
		"Type": (2130706435, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		"""Gets the Setin this collection in a sequences fashion; by index, or by its name -- Display or Internal"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{73F35CC7-ED6E-11D2-B785-0060B0F159EF}')
		return ret

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
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob, '{73F35CC7-ED6E-11D2-B785-0060B0F159EF}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{73F35CC7-ED6E-11D2-B785-0060B0F159EF}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if '_enum_' not in self.__dict__:
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2130706438, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

win32com.client.CLSIDToClass.RegisterCLSID( "{73F35CC8-ED6E-11D2-B785-0060B0F159EF}", PropertySets )
