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
class CommandManager(DispatchBaseClass):
	"""Command Manager Object that encapsulates all of the command-based functionality"""
	CLSID = IID('{9C88D3A9-C3EB-11D3-B79E-0060B0F159EF}')
	coclass_clsid = None

	def ClearPrivateEvents(self):
		"""Clears all data from Inventor's internal clipboard."""
		return self._oleobj_.InvokeTypes(50344738, LCID, 1, (24, 0), (),)

	# The method CommandEnabled is actually a property, but must be used as a method to correctly pass the arguments
	def CommandEnabled(self, BuiltInCommandId=defaultNamedNotOptArg):
		"""Gets a Boolean flag indicating if a given built-in command is enabled"""
		return self._oleobj_.InvokeTypes(50344712, LCID, 2, (11, 0), ((3, 1),),BuiltInCommandId
			)

	# Result is of type DragContext
	def CreateDragContext(self):
		"""Method that creates a new DragContext object"""
		ret = self._oleobj_.InvokeTypes(50344742, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, u'CreateDragContext', '{FA403DAE-32E0-4C17-BB7C-CD3626A9BFA9}')
		return ret

	# Result is of type InteractionEvents
	def CreateInteractionEvents(self):
		"""Creates a new Interaction Event object, providing exclusive input capability"""
		ret = self._oleobj_.InvokeTypes(50344715, LCID, 1, (13, 0), (),)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, u'CreateInteractionEvents', '{5C5381D9-CB23-4BD1-885F-744E8C90B9BB}')
		return ret

	# Result is of type MiniToolbar
	def CreateMiniToolbar(self):
		"""Method that creates a MiniToolbar object"""
		ret = self._oleobj_.InvokeTypes(50344743, LCID, 1, (13, 0), (),)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, u'CreateMiniToolbar', '{D5DA4F07-3728-4B95-9D14-5FF0ED96992E}')
		return ret

	def DoPreSelect(self, Entity=defaultNamedNotOptArg):
		"""Go through the pre-selection process with this given object"""
		return self._oleobj_.InvokeTypes(50344717, LCID, 1, (24, 0), ((9, 1),),Entity
			)

	def DoSelect(self, Entity=defaultNamedNotOptArg):
		"""Go through the process gone through when an object is selected, with this object"""
		return self._oleobj_.InvokeTypes(50344719, LCID, 1, (24, 0), ((9, 1),),Entity
			)

	def DoStopPreSelect(self, Entity=defaultNamedNotOptArg):
		"""End the pre-selection process with this given object"""
		return self._oleobj_.InvokeTypes(50344718, LCID, 1, (24, 0), ((9, 1),),Entity
			)

	def DoUnSelect(self, Entity=defaultNamedNotOptArg):
		"""Go through the process gone through when an object is un-selected, with this object"""
		return self._oleobj_.InvokeTypes(50344720, LCID, 1, (24, 0), ((9, 1),),Entity
			)

	def PeekPrivateEvent(self, DataType=pythoncom.Missing, Data=pythoncom.Missing):
		"""Peeks at the current data on Inventor's internal clipboard."""
		return self._ApplyTypes_(50344737, 1, (24, 0), ((16387, 2), (16396, 2)), u'PeekPrivateEvent', None,DataType
			, Data)

	def Pick(self, Filter=defaultNamedNotOptArg, PromptText=defaultNamedNotOptArg):
		"""Prompts the user for a single selection"""
		ret = self._oleobj_.InvokeTypes(50344741, LCID, 1, (9, 0), ((3, 1), (8, 1)),Filter
			, PromptText)
		if ret is not None:
			ret = Dispatch(ret, u'Pick', None)
		return ret

	def PostPrivateEvent(self, DataType=defaultNamedNotOptArg, Data=defaultNamedNotOptArg):
		"""Pastes data into Inventor's internal clipboard. The intended recipient of this data within Inventor (typically, a built-in command) will consume it and empty the clipboard"""
		return self._oleobj_.InvokeTypes(50344711, LCID, 1, (24, 0), ((3, 1), (12, 1)),DataType
			, Data)

	def PromptMessage(self, Prompt=defaultNamedNotOptArg, Buttons=defaultNamedNotOptArg, Title=defaultNamedOptArg, DefaultAnswer=defaultNamedOptArg
			, Restrictions=defaultNamedOptArg, PromptStrings=defaultNamedOptArg):
		"""Prompt user (unless user has suppressed this prompt)"""
		return self._oleobj_.InvokeTypes(50344740, LCID, 1, (3, 0), ((8, 1), (3, 1), (12, 17), (12, 17), (12, 17), (12, 17)),Prompt
			, Buttons, Title, DefaultAnswer, Restrictions, PromptStrings
			)

	def StartCommand(self, BuiltInCommandId=defaultNamedNotOptArg):
		"""Starts up the command specified. If not applicable in the current environment, returns failure"""
		return self._oleobj_.InvokeTypes(50344705, LCID, 1, (24, 0), ((3, 1),),BuiltInCommandId
			)

	def StartExecutable(self, ExecutableName=defaultNamedNotOptArg, Parameters=defaultNamedNotOptArg):
		"""Starts up the executable specified. The initiated process can be made a child of this Inventor process"""
		return self._oleobj_.InvokeTypes(50344708, LCID, 1, (24, 0), ((8, 1), (8, 1)),ExecutableName
			, Parameters)

	def StopActiveCommand(self):
		"""Terminates the current command. The default command cannot be terminated"""
		return self._oleobj_.InvokeTypes(50344707, LCID, 1, (24, 0), (),)

	def _PostPrivateEvent(self, Tag=defaultNamedNotOptArg, Data=defaultNamedNotOptArg):
		"""Hidden Property. Future signature of the PostPrivateEvent method. Includes the new 'Tag' as required to be specified"""
		return self._oleobj_.InvokeTypes(50344736, LCID, 1, (24, 0), ((8, 1), (12, 1)),Tag
			, Data)

	_prop_map_get_ = {
		"ActiveCommand": (50344739, 2, (8, 0), (), "ActiveCommand", None),
		# Method 'CommandCategories' returns object of type 'CommandCategories'
		"CommandCategories": (50344732, 2, (9, 0), (), "CommandCategories", '{AE2CB260-129A-494C-9F8C-AD8140271E8A}'),
		# Method 'ControlDefinitions' returns object of type 'ControlDefinitions'
		"ControlDefinitions": (50344733, 2, (9, 0), (), "ControlDefinitions", '{B9D982C4-3FFF-4796-AD6D-C6D1F16D7BA9}'),
		# Method 'Parent' returns object of type 'Application'
		"Parent": (2130706434, 2, (9, 0), (), "Parent", '{70109AA0-63C1-11D2-B78B-0060B0EC020B}'),
		"SelectionActive": (50344716, 2, (11, 0), (), "SelectionActive", None),
		"Type": (0, 2, (3, 0), (), "Type", None),
		# Method 'UserInputEvents' returns object of type 'UserInputEvents'
		"UserInputEvents": (50344710, 2, (13, 0), (), "UserInputEvents", '{9235396D-0350-11D3-B787-0060B0F159EF}'),
		"_ActiveCommand": (50344706, 2, (3, 0), (), "_ActiveCommand", None),
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

win32com.client.CLSIDToClass.RegisterCLSID( "{9C88D3A9-C3EB-11D3-B79E-0060B0F159EF}", CommandManager )
