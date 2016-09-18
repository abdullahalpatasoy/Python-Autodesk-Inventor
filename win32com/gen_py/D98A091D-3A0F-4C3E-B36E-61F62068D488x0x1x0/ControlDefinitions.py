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
class ControlDefinitions(DispatchBaseClass):
	"""Represents a ControlDefinitions object"""
	CLSID = IID('{B9D982C4-3FFF-4796-AD6D-C6D1F16D7BA9}')
	coclass_clsid = None

	# Result is of type ButtonDefinition
	def AddButtonDefinition(self, DisplayName=defaultNamedNotOptArg, InternalName=defaultNamedNotOptArg, Classification=defaultNamedNotOptArg, ClientId=defaultNamedNotOptArg
			, DescriptionText=u'', ToolTipText=u'', StandardIcon=defaultNamedNotOptArg, LargeIcon=defaultNamedNotOptArg, ButtonDisplay=43011):
		"""Method that adds a ButtonDefinition object"""
		return self._ApplyTypes_(50371330, 1, (13, 32), ((8, 1), (8, 1), (3, 1), (12, 17), (8, 49), (8, 49), (12, 17), (12, 17), (3, 49)), u'AddButtonDefinition', '{CD3A37C9-E647-41AA-B0D9-4EED2A875789}',DisplayName
			, InternalName, Classification, ClientId, DescriptionText, ToolTipText
			, StandardIcon, LargeIcon, ButtonDisplay)

	# Result is of type ComboBoxDefinition
	def AddComboBoxDefinition(self, DisplayName=defaultNamedNotOptArg, InternalName=defaultNamedNotOptArg, Classification=defaultNamedNotOptArg, DropDownWidth=defaultNamedNotOptArg
			, ClientId=defaultNamedNotOptArg, DescriptionText=u'', ToolTipText=u'', StandardIcon=defaultNamedNotOptArg, LargeIcon=defaultNamedNotOptArg
			, ButtonDisplay=43011):
		"""Method that adds a ComboBoxDefinition object"""
		return self._ApplyTypes_(50371331, 1, (13, 32), ((8, 1), (8, 1), (3, 1), (3, 1), (12, 17), (8, 49), (8, 49), (12, 17), (12, 17), (3, 49)), u'AddComboBoxDefinition', '{60F87ABB-0D3B-47D0-A6A9-E9AAC919EF31}',DisplayName
			, InternalName, Classification, DropDownWidth, ClientId, DescriptionText
			, ToolTipText, StandardIcon, LargeIcon, ButtonDisplay)

	# Result is of type MacroControlDefinition
	def AddMacroControlDefinition(self, MacroOrProgram=defaultNamedNotOptArg):
		"""Method that adds a Macro UIDefinition object"""
		ret = self._oleobj_.InvokeTypes(50371329, LCID, 1, (9, 0), ((8, 1),),MacroOrProgram
			)
		if ret is not None:
			ret = Dispatch(ret, u'AddMacroControlDefinition', '{2F800161-0E4D-4953-A0B7-E55EE05E039B}')
		return ret

	# Result is of type ControlDefinition
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		"""Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well."""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, u'Item', '{1ABBBF4A-8946-4A44-BFAE-F3200B41AA40}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'Application'
		"Application": (2130706433, 2, (9, 0), (), "Application", '{70109AA0-63C1-11D2-B78B-0060B0EC020B}'),
		"Count": (2130706438, 2, (3, 0), (), "Count", None),
		"Type": (2130706435, 2, (3, 0), (), "Type", None),
		"UseDefaultMultiCharAliases": (50371332, 2, (11, 0), (), "UseDefaultMultiCharAliases", None),
	}
	_prop_map_put_ = {
		"UseDefaultMultiCharAliases": ((50371332, LCID, 4, 0),()),
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		"""Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well."""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{1ABBBF4A-8946-4A44-BFAE-F3200B41AA40}')
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
		return win32com.client.util.Iterator(ob, '{1ABBBF4A-8946-4A44-BFAE-F3200B41AA40}')
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{1ABBBF4A-8946-4A44-BFAE-F3200B41AA40}')
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

win32com.client.CLSIDToClass.RegisterCLSID( "{B9D982C4-3FFF-4796-AD6D-C6D1F16D7BA9}", ControlDefinitions )
