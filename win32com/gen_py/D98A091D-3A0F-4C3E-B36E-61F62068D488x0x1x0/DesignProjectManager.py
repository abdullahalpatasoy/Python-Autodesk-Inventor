# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.00
# By python version 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Tue Nov 17 17:34:32 2015
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
class DesignProjectManager(DispatchBaseClass):
	"""Design Project Manager Object"""
	CLSID = IID('{4A60CB5E-1EE8-4180-A801-194704F3021E}')
	coclass_clsid = None

	# Result is of type ProjectOptionsButton
	def AddOptionsButton(self, ClientId=defaultNamedNotOptArg, DisplayName=defaultNamedNotOptArg, ToolTipText=defaultNamedNotOptArg, StandardIcon=defaultNamedOptArg):
		"""Method that adds an options button to the Projects dialog. The returned button object can be used to receive an OnClick event fired when the user clicks the option button."""
		ret = self._oleobj_.InvokeTypes(50401029, LCID, 1, (13, 0), ((8, 1), (8, 1), (8, 1), (12, 17)),ClientId
			, DisplayName, ToolTipText, StandardIcon)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, u'AddOptionsButton', '{A4791D9E-EEA1-4524-8543-174DA9CC42B3}')
		return ret

	def IsFileInActiveProject(self, FileName=defaultNamedNotOptArg, ProjectPathType=pythoncom.Missing, ProjectPathName=pythoncom.Missing):
		"""Returns whether the given file is located within the project using the resolution rules of the project, and additionally returns the path type (library, workspace, workgroup) and its name."""
		return self._ApplyTypes_(50401027, 1, (11, 0), ((8, 1), (16387, 2), (16392, 2)), u'IsFileInActiveProject', None,FileName
			, ProjectPathType, ProjectPathName)

	def ResolveFile(self, SourcePath=defaultNamedNotOptArg, DestinationFileName=defaultNamedNotOptArg, Options=defaultNamedOptArg):
		"""Run the file resolver from the source path and attempts to find the destination file name. The full file name of the resolved file is returned.  A null string is returned if no file was resolved to."""
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(50401028, LCID, 1, (8, 0), ((8, 1), (8, 1), (12, 16)),SourcePath
			, DestinationFileName, Options)

	_prop_map_get_ = {
		# Method 'ActiveDesignProject' returns object of type 'DesignProject'
		"ActiveDesignProject": (50401026, 2, (9, 0), (), "ActiveDesignProject", '{9A14B139-7101-40B1-BD92-B3F9870DC7F0}'),
		"Application": (2130706433, 2, (9, 0), (), "Application", None),
		# Method 'DesignProjects' returns object of type 'DesignProjects'
		"DesignProjects": (50401025, 2, (9, 0), (), "DesignProjects", '{131DB1C8-39A0-41F6-B881-9B49050D08DC}'),
		"Parent": (2130706434, 2, (9, 0), (), "Parent", None),
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

win32com.client.CLSIDToClass.RegisterCLSID( "{4A60CB5E-1EE8-4180-A801-194704F3021E}", DesignProjectManager )
