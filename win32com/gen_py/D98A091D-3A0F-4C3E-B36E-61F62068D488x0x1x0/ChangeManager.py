# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.00
# By python version 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Tue Nov 17 17:35:13 2015
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
class ChangeManager(DispatchBaseClass):
	"""ChangeManager Object"""
	CLSID = IID('{D70C53E3-58A6-48CA-95D2-AF6F4AAD04EA}')
	coclass_clsid = None

	# Result is of type ChangeDefinitions
	def Add(self, ClientId=defaultNamedNotOptArg):
		"""Creates a new ChangeDefinitions collection object based on a unique string that identifies the client"""
		ret = self._oleobj_.InvokeTypes(50388737, LCID, 1, (9, 0), ((8, 1),),ClientId
			)
		if ret is not None:
			ret = Dispatch(ret, u'Add', '{9ACB775D-8E1E-4A38-9121-7E1467526860}')
		return ret

	def GetObjectFromScriptKey(self, ScriptKey=defaultNamedNotOptArg):
		"""Gets the object with the specified string.  The script key should have been generated using the GetScriptKeyFromObject method and the document should be in the same or similar state as when the script key was generated."""
		ret = self._oleobj_.InvokeTypes(50388738, LCID, 1, (9, 0), ((8, 1),),ScriptKey
			)
		if ret is not None:
			ret = Dispatch(ret, u'GetObjectFromScriptKey', None)
		return ret

	def GetScriptKeyFromObject(self, Object=defaultNamedNotOptArg):
		"""Generates a key (identifier) for the input object.  This key is suitable to use in constructing the Inputs argument of the OnWriteToScript event on the ChangeProcessor object."""
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(50388739, LCID, 1, (8, 0), ((9, 1),),Object
			)

	# Result is of type ChangeDefinitions
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		"""Allows integer-indexed access to items in the collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, u'Item', '{9ACB775D-8E1E-4A38-9121-7E1467526860}')
		return ret

	_prop_map_get_ = {
		"Application": (2130706433, 2, (9, 0), (), "Application", None),
		"Count": (2130706438, 2, (3, 0), (), "Count", None),
		"Parent": (2130706434, 2, (9, 0), (), "Parent", None),
		"Type": (2130706435, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		"""Allows integer-indexed access to items in the collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{9ACB775D-8E1E-4A38-9121-7E1467526860}')
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
		return win32com.client.util.Iterator(ob, '{9ACB775D-8E1E-4A38-9121-7E1467526860}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{9ACB775D-8E1E-4A38-9121-7E1467526860}')
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

win32com.client.CLSIDToClass.RegisterCLSID( "{D70C53E3-58A6-48CA-95D2-AF6F4AAD04EA}", ChangeManager )
