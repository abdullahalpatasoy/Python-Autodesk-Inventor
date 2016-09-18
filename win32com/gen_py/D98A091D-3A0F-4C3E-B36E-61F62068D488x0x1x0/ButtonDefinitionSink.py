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

class ButtonDefinitionSink:
	"""Event sink for ButtonDefinition"""
	CLSID = CLSID_Sink = IID('{9B5D2EC6-A4BD-4B3A-8A34-069EE52B009D}')
	coclass_clsid = IID('{CD3A37C9-E647-41AA-B0D9-4EED2A875789}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		 50371714 : "OnHelp",
		 50371713 : "OnExecute",
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
#	def OnHelp(self, Context=defaultNamedNotOptArg, HandlingCode=pythoncom.Missing):
#		"""Fires signaling the client to present help for the associated command"""
#	def OnExecute(self, Context=defaultNamedNotOptArg):
#		"""Fires when ButtonDefinition is Executed"""


win32com.client.CLSIDToClass.RegisterCLSID( "{9B5D2EC6-A4BD-4B3A-8A34-069EE52B009D}", ButtonDefinitionSink )
