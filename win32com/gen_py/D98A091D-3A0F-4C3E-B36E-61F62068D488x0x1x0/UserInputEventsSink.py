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

class UserInputEventsSink:
	"""Outgoing interface recognized by the User Input Events Object"""
	CLSID = CLSID_Sink = IID('{711F30CD-A00B-4015-93A8-397EC8F5A284}')
	coclass_clsid = IID('{9235396D-0350-11D3-B787-0060B0F159EF}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		 50340358 : "OnContextMenu",
		 50340366 : "OnRadialMarkingMenu",
		 50340354 : "OnStartCommand",
		 50340367 : "OnLinearMarkingMenu",
		 50340356 : "OnContextMenuOld",
		 50340361 : "OnDoubleClick",
		 50340362 : "OnPreSelect",
		 50340360 : "OnTerminateCommand",
		 50340364 : "OnSelect",
		 50340368 : "OnContextualMiniToolbar",
		 50340365 : "OnUnSelect",
		 50340363 : "OnStopPreSelect",
		 50340357 : "OnDrag",
		 50340359 : "OnActivateCommand",
		 50340355 : "OnStopCommand",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnContextMenu(self, SelectionDevice=defaultNamedNotOptArg, AdditionalInfo=defaultNamedNotOptArg, CommandBar=defaultNamedNotOptArg):
#		"""Fires just before context menu is about to be displayed"""
#	def OnRadialMarkingMenu(self, SelectedEntities=defaultNamedNotOptArg, SelectionDevice=defaultNamedNotOptArg, RadialMenu=defaultNamedNotOptArg, AdditionalInfo=defaultNamedNotOptArg):
#		"""Fires before the marking menu is displayed to the user or before the user gestures using the right mouse button"""
#	def OnStartCommand(self, CommandID=defaultNamedNotOptArg):
#		"""Fires before starting up a command"""
#	def OnLinearMarkingMenu(self, SelectedEntities=defaultNamedNotOptArg, SelectionDevice=defaultNamedNotOptArg, LinearMenu=defaultNamedNotOptArg, AdditionalInfo=defaultNamedNotOptArg):
#		"""Fires before the overflow context menu is displayed to the user"""
#	def OnContextMenuOld(self, SelectionDevice=defaultNamedNotOptArg, AdditionalInfo=defaultNamedNotOptArg, CommandBar=defaultNamedNotOptArg):
#		"""Fires just before context menu is about to be displayed"""
#	def OnDoubleClick(self, SelectedEntities=defaultNamedNotOptArg, SelectionDevice=defaultNamedNotOptArg, Button=defaultNamedNotOptArg, ShiftKeys=defaultNamedNotOptArg
#			, ModelPosition=defaultNamedNotOptArg, ViewPosition=defaultNamedNotOptArg, View=defaultNamedNotOptArg, AdditionalInfo=defaultNamedNotOptArg, HandlingCode=pythoncom.Missing):
#		"""Fires when the user performs a double click operation when no command is active"""
#	def OnPreSelect(self, PreSelectEntity=defaultNamedNotOptArg, DoHighlight=pythoncom.Missing, MorePreSelectEntities=defaultNamedNotOptArg, SelectionDevice=defaultNamedNotOptArg
#			, ModelPosition=defaultNamedNotOptArg, ViewPosition=defaultNamedNotOptArg, View=defaultNamedNotOptArg):
#		"""Fires when the user hovers over an Inventor object, and it is a potential candidate for selection"""
#	def OnTerminateCommand(self, CommandName=defaultNamedNotOptArg, Context=defaultNamedNotOptArg):
#		"""Fires just before a command terminates"""
#	def OnSelect(self, JustSelectedEntities=defaultNamedNotOptArg, MoreSelectedEntities=defaultNamedNotOptArg, SelectionDevice=defaultNamedNotOptArg, ModelPosition=defaultNamedNotOptArg
#			, ViewPosition=defaultNamedNotOptArg, View=defaultNamedNotOptArg):
#		"""Fires when the user selects an object by clicking"""
#	def OnContextualMiniToolbar(self, SelectedEntities=defaultNamedNotOptArg, DisplayedCommands=defaultNamedNotOptArg, AdditionalInfo=defaultNamedNotOptArg):
#		"""Fires before contextual commands are displayed to the user in the graphics window when the user selects an object"""
#	def OnUnSelect(self, UnSelectedEntities=defaultNamedNotOptArg, SelectionDevice=defaultNamedNotOptArg, ModelPosition=defaultNamedNotOptArg, ViewPosition=defaultNamedNotOptArg
#			, View=defaultNamedNotOptArg):
#		"""Fires when an object is un-selected in any way (by selecting some other object. clicking in space, etc.)"""
#	def OnStopPreSelect(self, ModelPosition=defaultNamedNotOptArg, ViewPosition=defaultNamedNotOptArg, View=defaultNamedNotOptArg):
#		"""Fires when the user hovers away from an Inventor object and it is no longer highlighted"""
#	def OnDrag(self, DragState=defaultNamedNotOptArg, ShiftKeys=defaultNamedNotOptArg, ModelPosition=defaultNamedNotOptArg, ViewPosition=defaultNamedNotOptArg
#			, View=defaultNamedNotOptArg, AdditionalInfo=defaultNamedNotOptArg, HandlingCode=pythoncom.Missing):
#		"""Fires when the user performs a drag operation when no command is active"""
#	def OnActivateCommand(self, CommandName=defaultNamedNotOptArg, Context=defaultNamedNotOptArg):
#		"""Fires just before a command starts"""
#	def OnStopCommand(self, CommandID=defaultNamedNotOptArg):
#		"""Fires after a command terminates"""


win32com.client.CLSIDToClass.RegisterCLSID( "{711F30CD-A00B-4015-93A8-397EC8F5A284}", UserInputEventsSink )
