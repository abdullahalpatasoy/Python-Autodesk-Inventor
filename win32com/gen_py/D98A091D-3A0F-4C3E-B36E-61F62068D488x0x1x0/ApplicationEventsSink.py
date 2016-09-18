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

class ApplicationEventsSink:
	"""Outgoing IDispatch-based interface recognized by the Application Events Object"""
	CLSID = CLSID_Sink = IID('{CD4C47ED-C403-4F42-B3BF-0A90F3E89D81}')
	coclass_clsid = IID('{70109AAD-63C1-11D2-B78B-0060B0EC020B}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		 50333204 : "OnActivateDocument",
		 50333203 : "OnCloseDocument",
		 50333226 : "OnTerminateDocument",
		 50333215 : "OnNewView",
		 50333205 : "OnDeactivateDocument",
		 50333233 : "OnNewWebView",
		 50333216 : "OnDisplayModeChange",
		 50333234 : "OnWebViewAct",
		 50333214 : "OnDocumentChange",
		 50333232 : "OnCloseWebView",
		 50333228 : "OnRestart32BitHost",
		 50333213 : "OnActiveProjectChanged",
		 50333231 : "OnDeactivateWebView",
		 50333230 : "OnActivateWebView",
		 50333229 : "OnApplicationOptionChange",
		 50333217 : "OnReady",
		 50333227 : "OnMigrateDocument",
		 50333211 : "OnNewEditObject",
		 50333219 : "OnActivateView",
		 50333220 : "OnDeactivateView",
		 50333202 : "OnSaveDocument",
		 50333210 : "OnQuit",
		 50333200 : "OnNewDocument",
		 50333201 : "OnOpenDocument",
		 50333212 : "OnTranslateDocument",
		 50333225 : "OnInitializeDocument",
		 50333218 : "OnCloseView",
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
#	def OnActivateDocument(self, DocumentObject=defaultNamedNotOptArg, BeforeOrAfter=defaultNamedNotOptArg, Context=defaultNamedNotOptArg, HandlingCode=pythoncom.Missing):
#		"""Fires just before and soon after activation of a Document, supplying the context in which this action is being taken"""
#	def OnCloseDocument(self, DocumentObject=defaultNamedNotOptArg, FullDocumentName=defaultNamedNotOptArg, BeforeOrAfter=defaultNamedNotOptArg, Context=defaultNamedNotOptArg
#			, HandlingCode=pythoncom.Missing):
#		"""Fires just before and soon after close of a Document, supplying the context in which this action is being taken. When fired after close, the Document passed in can only be used for IUnknown comparisons"""
#	def OnTerminateDocument(self, DocumentObject=defaultNamedNotOptArg, FullDocumentName=defaultNamedNotOptArg, BeforeOrAfter=defaultNamedNotOptArg, Context=defaultNamedNotOptArg
#			, HandlingCode=pythoncom.Missing):
#		"""Fires just before and soon after termination of a Document, or its full closure, supplying the context in which this action is being taken. When fired after close, the Document passed in can only be used for IUnknown comparisons"""
#	def OnNewView(self, ViewObject=defaultNamedNotOptArg, BeforeOrAfter=defaultNamedNotOptArg, Context=defaultNamedNotOptArg, HandlingCode=pythoncom.Missing):
#		"""Fires just before and soon after a view is created"""
#	def OnDeactivateDocument(self, DocumentObject=defaultNamedNotOptArg, BeforeOrAfter=defaultNamedNotOptArg, Context=defaultNamedNotOptArg, HandlingCode=pythoncom.Missing):
#		"""Fires just before and soon after deactivation of a Document, supplying the context in which this action is being taken"""
#	def OnNewWebView(self, WebViewObject=defaultNamedNotOptArg, BeforeOrAfter=defaultNamedNotOptArg, Context=defaultNamedNotOptArg, HandlingCode=pythoncom.Missing):
#		"""Fires just after a web view is created"""
#	def OnDisplayModeChange(self, ViewObject=defaultNamedNotOptArg, BeforeOrAfter=defaultNamedNotOptArg, Context=defaultNamedNotOptArg, HandlingCode=pythoncom.Missing):
#		"""Fires just before and soon after the display mode changes"""
#	def OnWebViewAct(self, WebViewObject=defaultNamedNotOptArg, ActionID=defaultNamedNotOptArg, BeforeOrAfter=defaultNamedNotOptArg, Context=defaultNamedNotOptArg
#			, HandlingCode=pythoncom.Missing):
#		"""Event that fires just after a web view action occurs"""
#	def OnDocumentChange(self, DocumentObject=defaultNamedNotOptArg, BeforeOrAfter=defaultNamedNotOptArg, ReasonsForChange=defaultNamedNotOptArg, Context=defaultNamedNotOptArg
#			, HandlingCode=pythoncom.Missing):
#		"""Fires just before the document is changed, supplying the reasons for change and the context in which this action is being taken"""
#	def OnCloseWebView(self, WebViewObject=defaultNamedNotOptArg, BeforeOrAfter=defaultNamedNotOptArg, Context=defaultNamedNotOptArg, HandlingCode=pythoncom.Missing):
#		"""Event that fires just before a web view is closed."""
#	def OnRestart32BitHost(self, BeforeOrAfter=defaultNamedNotOptArg, Context=defaultNamedNotOptArg, HandlingCode=pythoncom.Missing):
#		"""Applies to 64-bit Inventor only. Fires after the Inventor 32-bit host process has been restarted"""
#	def OnActiveProjectChanged(self, ProjectObject=defaultNamedNotOptArg, BeforeOrAfter=defaultNamedNotOptArg, Context=defaultNamedNotOptArg, HandlingCode=pythoncom.Missing):
#		"""Fires just before and soon after the active project is changed, supplying the context in which this action is being taken"""
#	def OnDeactivateWebView(self, WebViewObject=defaultNamedNotOptArg, BeforeOrAfter=defaultNamedNotOptArg, Context=defaultNamedNotOptArg, HandlingCode=pythoncom.Missing):
#		"""Event that fires just before a web view is deactivated."""
#	def OnActivateWebView(self, WebViewObject=defaultNamedNotOptArg, BeforeOrAfter=defaultNamedNotOptArg, Context=defaultNamedNotOptArg, HandlingCode=pythoncom.Missing):
#		"""Event that fires just after a web view is activated."""
#	def OnApplicationOptionChange(self, BeforeOrAfter=defaultNamedNotOptArg, Context=defaultNamedNotOptArg, HandlingCode=pythoncom.Missing):
#		"""Fires just before and soon after application options are modified"""
#	def OnReady(self, BeforeOrAfter=defaultNamedNotOptArg, Context=defaultNamedNotOptArg, HandlingCode=pythoncom.Missing):
#		"""Fires only once soon after Inventor has completed its initialization. This includes initialization of all the Add-ins that are loaded at startup."""
#	def OnMigrateDocument(self, DocumentObject=defaultNamedNotOptArg, BeforeOrAfter=defaultNamedNotOptArg, Context=defaultNamedNotOptArg, HandlingCode=pythoncom.Missing):
#		"""Fires just before and soon after a Document is explicitly migrated, supplying the context in which this action is being taken"""
#	def OnNewEditObject(self, EditObject=defaultNamedNotOptArg, BeforeOrAfter=defaultNamedNotOptArg, Context=defaultNamedNotOptArg, HandlingCode=pythoncom.Missing):
#		"""Fires just before and soon after the current edit object changes, supplying the context in which this action is being taken"""
#	def OnActivateView(self, ViewObject=defaultNamedNotOptArg, BeforeOrAfter=defaultNamedNotOptArg, Context=defaultNamedNotOptArg, HandlingCode=pythoncom.Missing):
#		"""Fires just after a view is activated"""
#	def OnDeactivateView(self, ViewObject=defaultNamedNotOptArg, BeforeOrAfter=defaultNamedNotOptArg, Context=defaultNamedNotOptArg, HandlingCode=pythoncom.Missing):
#		"""Fires just after a view is deactivated"""
#	def OnSaveDocument(self, DocumentObject=defaultNamedNotOptArg, BeforeOrAfter=defaultNamedNotOptArg, Context=defaultNamedNotOptArg, HandlingCode=pythoncom.Missing):
#		"""Fires just before and soon after save of a Document, supplying the context in which this action is being taken"""
#	def OnQuit(self, BeforeOrAfter=defaultNamedNotOptArg, Context=defaultNamedNotOptArg, HandlingCode=pythoncom.Missing):
#		"""Fires just before the shut-down operation is about to begin, supplying the context in which this action is being taken"""
#	def OnNewDocument(self, DocumentObject=defaultNamedNotOptArg, BeforeOrAfter=defaultNamedNotOptArg, Context=defaultNamedNotOptArg, HandlingCode=pythoncom.Missing):
#		"""Fires just before and soon after initialization of a new Document, supplying the context in which this action is being taken"""
#	def OnOpenDocument(self, DocumentObject=defaultNamedNotOptArg, FullDocumentName=defaultNamedNotOptArg, BeforeOrAfter=defaultNamedNotOptArg, Context=defaultNamedNotOptArg
#			, HandlingCode=pythoncom.Missing):
#		"""Fires just before and soon after initialization of an opened Document, supplying the context in which this action is being taken"""
#	def OnTranslateDocument(self, TranslatingIn=defaultNamedNotOptArg, DocumentObject=defaultNamedNotOptArg, FullFileName=defaultNamedNotOptArg, BeforeOrAfter=defaultNamedNotOptArg
#			, Context=defaultNamedNotOptArg, HandlingCode=pythoncom.Missing):
#		"""Fires just before and soon after a Document is translated in or out, supplying the context in which this action is being taken"""
#	def OnInitializeDocument(self, DocumentObject=defaultNamedNotOptArg, FullDocumentName=defaultNamedNotOptArg, BeforeOrAfter=defaultNamedNotOptArg, Context=defaultNamedNotOptArg
#			, HandlingCode=pythoncom.Missing):
#		"""Fires just before and soon after initialization of a Document, which is not yet open, supplying the context in which this action is being taken"""
#	def OnCloseView(self, ViewObject=defaultNamedNotOptArg, BeforeOrAfter=defaultNamedNotOptArg, Context=defaultNamedNotOptArg, HandlingCode=pythoncom.Missing):
#		"""Fires just before a view is closed"""


win32com.client.CLSIDToClass.RegisterCLSID( "{CD4C47ED-C403-4F42-B3BF-0A90F3E89D81}", ApplicationEventsSink )
