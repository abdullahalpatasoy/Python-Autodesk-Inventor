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
class PropertySet(DispatchBaseClass):
	"""Object that represents a Property Set. This is a collection of related Properties"""
	CLSID = IID('{73F35CC7-ED6E-11D2-B785-0060B0F159EF}')
	coclass_clsid = None

	# Result is of type Property
	def Add(self, PropValue=defaultNamedNotOptArg, Name=defaultNamedOptArg, PropId=defaultNamedOptArg):
		"""Adds a new Property to this Property Set"""
		ret = self._oleobj_.InvokeTypes(50338563, LCID, 1, (9, 0), ((12, 1), (12, 17), (12, 17)),PropValue
			, Name, PropId)
		if ret is not None:
			ret = Dispatch(ret, u'Add', '{73F35CC9-ED6E-11D2-B785-0060B0F159EF}')
		return ret

	def Delete(self):
		"""Deletes this Property Set"""
		return self._oleobj_.InvokeTypes(50338564, LCID, 1, (24, 0), (),)

	# Result is of type Property
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		"""Gets the Property given either its Name or its sequential index"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, u'Item', '{73F35CC9-ED6E-11D2-B785-0060B0F159EF}')
		return ret

	# Result is of type Property
	# The method ItemByPropId is actually a property, but must be used as a method to correctly pass the arguments
	def ItemByPropId(self, PropId=defaultNamedNotOptArg):
		"""Gets the Property in this Set by its PropId"""
		ret = self._oleobj_.InvokeTypes(50338566, LCID, 2, (9, 0), ((3, 1),),PropId
			)
		if ret is not None:
			ret = Dispatch(ret, u'ItemByPropId', '{73F35CC9-ED6E-11D2-B785-0060B0F159EF}')
		return ret

	_prop_map_get_ = {
		"Count": (2130706438, 2, (3, 0), (), "Count", None),
		"Dirty": (50338567, 2, (11, 0), (), "Dirty", None),
		"DisplayName": (50338561, 2, (8, 0), (), "DisplayName", None),
		"InternalName": (50338562, 2, (8, 0), (), "InternalName", None),
		"Name": (50338570, 2, (8, 0), (), "Name", None),
		# Method 'Parent' returns object of type 'PropertySets'
		"Parent": (2130706434, 2, (9, 0), (), "Parent", '{73F35CC8-ED6E-11D2-B785-0060B0F159EF}'),
		"Type": (2130706435, 2, (3, 0), (), "Type", None),
		"_CodePage": (50338568, 2, (3, 0), (), "_CodePage", None),
		"_Locale": (50338569, 2, (3, 0), (), "_Locale", None),
	}
	_prop_map_put_ = {
		"DisplayName": ((50338561, LCID, 4, 0),()),
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		"""Gets the Property given either its Name or its sequential index"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{73F35CC9-ED6E-11D2-B785-0060B0F159EF}')
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
		return win32com.client.util.Iterator(ob, '{73F35CC9-ED6E-11D2-B785-0060B0F159EF}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{73F35CC9-ED6E-11D2-B785-0060B0F159EF}')
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

win32com.client.CLSIDToClass.RegisterCLSID( "{73F35CC7-ED6E-11D2-B785-0060B0F159EF}", PropertySet )
