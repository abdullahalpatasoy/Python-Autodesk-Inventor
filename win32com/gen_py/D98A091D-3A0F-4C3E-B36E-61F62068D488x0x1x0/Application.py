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
class Application(DispatchBaseClass):
	"""Inventor Application Object"""
	CLSID = IID('{70109AA0-63C1-11D2-B78B-0060B0EC020B}')
	coclass_clsid = None

	def ConstructInternalNameAndRevisionId(self, InternalNameToken=defaultNamedNotOptArg, RevisionIdToken=defaultNamedNotOptArg, InternalName=pythoncom.Missing, RevisionId=pythoncom.Missing):
		"""Constructs and returns the Internal Name and Revision Identifier"""
		return self._ApplyTypes_(50332020, 1, (24, 0), ((8, 1), (8, 1), (16392, 2), (16392, 2)), u'ConstructInternalNameAndRevisionId', None,InternalNameToken
			, RevisionIdToken, InternalName, RevisionId)

	def CreateFileDialog(self, Dialog=pythoncom.Missing):
		"""Creates a file dialog"""
		return self._ApplyTypes_(50331981, 1, (24, 0), ((16393, 2),), u'CreateFileDialog', None,Dialog
			)

	def CreateInternalName(self, Name=defaultNamedNotOptArg, Number=defaultNamedNotOptArg, Custom=defaultNamedNotOptArg, InternalName=pythoncom.Missing):
		"""Constructs the unique, deterministic name out of the sub-strings supplied (Name + Number + Custom = InternalName). The internal name is a stringified GUID"""
		return self._ApplyTypes_(50331967, 1, (24, 0), ((8, 1), (8, 1), (8, 1), (16392, 2)), u'CreateInternalName', None,Name
			, Number, Custom, InternalName)

	# Result is of type ProgressBar
	def CreateProgressBar(self, DisplayInStatusBar=defaultNamedNotOptArg, NumberOfSteps=defaultNamedNotOptArg, Title=defaultNamedNotOptArg, AllowCancel=False
			, HWND=0):
		"""Creates a new ProgressBar object."""
		ret = self._oleobj_.InvokeTypes(50332034, LCID, 1, (13, 0), ((11, 1), (3, 1), (8, 1), (11, 49), (3, 49)),DisplayInStatusBar
			, NumberOfSteps, Title, AllowCancel, HWND)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, u'CreateProgressBar', '{8574FEAB-B050-439E-AC97-9704A217E5A1}')
		return ret

	def GetAppFrameExtents(self, Top=pythoncom.Missing, Left=pythoncom.Missing, Height=pythoncom.Missing, Width=pythoncom.Missing):
		"""Obtains the position and size of the Application's main frame window"""
		return self._ApplyTypes_(50331915, 1, (24, 0), ((16387, 2), (16387, 2), (16387, 2), (16387, 2)), u'GetAppFrameExtents', None,Top
			, Left, Height, Width)

	def GetInterfaceObject(self, ProgIDorCLSID=defaultNamedNotOptArg):
		"""Constructs and returns the specified object"""
		ret = self._oleobj_.InvokeTypes(50331987, LCID, 1, (13, 0), ((8, 1),),ProgIDorCLSID
			)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, u'GetInterfaceObject', None)
		return ret

	def GetInterfaceObject32(self, ProgIDorCLSID=defaultNamedNotOptArg):
		"""same as GetInterfaceObject, except that on 64-bit Inventor, the COM server is loaded in the Inventor 32-bit host process"""
		ret = self._oleobj_.InvokeTypes(50332022, LCID, 1, (13, 0), ((8, 1),),ProgIDorCLSID
			)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, u'GetInterfaceObject32', None)
		return ret

	def GetTemplateFile(self, DocumentType=defaultNamedNotOptArg, SystemOfMeasure=8961, DraftingStandard=9729, DocumentSubType=defaultNamedOptArg):
		"""Obtains the Inventor template file that corresponds to the criteria specified in the input arguments"""
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(50331960, LCID, 1, (8, 0), ((3, 1), (3, 49), (3, 49), (12, 17)),DocumentType
			, SystemOfMeasure, DraftingStandard, DocumentSubType)

	def LicenseChallenge(self):
		"""Request a license challenge string"""
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(50431489, LCID, 1, (8, 0), (),)

	def LicenseResponse(self, Response=defaultNamedNotOptArg):
		"""Provides a license challenge response string"""
		return self._oleobj_.InvokeTypes(50431490, LCID, 1, (24, 0), ((8, 1),),Response
			)

	def Login(self):
		"""Prompts the user to login to online services if not already logged in"""
		return self._oleobj_.InvokeTypes(50332042, LCID, 1, (11, 0), (),)

	def Move(self, Top=defaultNamedNotOptArg, Left=defaultNamedNotOptArg, Height=defaultNamedNotOptArg, Width=defaultNamedNotOptArg):
		"""Moves the frame window"""
		return self._oleobj_.InvokeTypes(50331977, LCID, 1, (24, 0), ((16387, 1), (16387, 1), (16387, 1), (16387, 1)),Top
			, Left, Height, Width)

	def Quit(self):
		"""Shuts down the application"""
		return self._oleobj_.InvokeTypes(50331913, LCID, 1, (24, 0), (),)

	def ReserveLicense(self, ClientId=defaultNamedNotOptArg):
		"""Informs Inventor/Apprentice that a license should be retained for this instace of the application. Used to prevent idle detection from returning the seat license to the license pool. Requires a call to UnreserveLicense with teh same ClientID to allow the licen???l??????"""
		return self._oleobj_.InvokeTypes(50332031, LCID, 1, (24, 0), ((8, 1),),ClientId
			)

	def ShowMyHomeWindow(self, ContentTypeOrURL=defaultNamedOptArg):
		"""Method that displays the MyHome base window with the specified content in it"""
		return self._oleobj_.InvokeTypes(50332045, LCID, 1, (24, 0), ((12, 17),),ContentTypeOrURL
			)

	def UnreserveLicense(self, ClientId=defaultNamedNotOptArg):
		"""Informs Inventor/Apprentice that normal seat license reclamation can resume. Use this method when extended processing for which a license was reserved completes. Do not use without a previous call to ReserveLicense using the same ClientID."""
		return self._oleobj_.InvokeTypes(50332032, LCID, 1, (24, 0), ((8, 1),),ClientId
			)

	def WriteCIPWaypoint(self, WaypointData=defaultNamedNotOptArg):
		"""Hidden method. Not for public use. Method that writes information describing the action of the current command as a CIP waypoint."""
		return self._oleobj_.InvokeTypes(50331927, LCID, 1, (24, 0), ((8, 1),),WaypointData
			)

	def _ConstructInternalNameAndFileVersion(self, Name=defaultNamedNotOptArg, Number=defaultNamedNotOptArg, Custom=defaultNamedNotOptArg, Revision=defaultNamedNotOptArg
			, InternalName=pythoncom.Missing, FileVersion=pythoncom.Missing):
		"""*** DEFUNCT SINCE R5.3"""
		return self._ApplyTypes_(50331951, 1, (24, 0), ((8, 1), (8, 1), (8, 1), (8, 1), (16392, 2), (16392, 2)), u'_ConstructInternalNameAndFileVersion', None,Name
			, Number, Custom, Revision, InternalName, FileVersion
			)

	def _DeleteRegistryEntry(self, SubKey=defaultNamedNotOptArg, ValueName=defaultNamedNotOptArg, RegistryHive=defaultNamedNotOptArg):
		"""Hidden method. Not for public use. Deletes an entry from the system registry, including the current Inventor hive"""
		return self._oleobj_.InvokeTypes(50331936, LCID, 1, (24, 0), ((8, 1), (8, 1), (3, 1)),SubKey
			, ValueName, RegistryHive)

	def _GetShapeManagerVersion(self, MajorVersion=pythoncom.Missing, MinorVersion=pythoncom.Missing, PointVersion=pythoncom.Missing):
		"""Hidden property. Not for public use"""
		return self._ApplyTypes_(50331971, 1, (24, 0), ((16387, 2), (16387, 2), (16387, 2)), u'_GetShapeManagerVersion', None,MajorVersion
			, MinorVersion, PointVersion)

	# The method _IsRegistryEntry is actually a property, but must be used as a method to correctly pass the arguments
	def _IsRegistryEntry(self, SubKey=defaultNamedNotOptArg, ValueName=defaultNamedNotOptArg, RegistryHive=defaultNamedNotOptArg):
		"""Hidden property. Not for public use. Gets a Boolean indicating whether the specified entry exists in the system registry, including the current Inventor hive"""
		return self._oleobj_.InvokeTypes(50331933, LCID, 2, (11, 0), ((8, 1), (8, 1), (3, 1)),SubKey
			, ValueName, RegistryHive)

	def _LogExceptionDump(self, Value=defaultNamedNotOptArg):
		"""Logs an exception dump file"""
		return self._oleobj_.InvokeTypes(50332005, LCID, 1, (24, 0), ((16387, 1),),Value
			)

	def _MigrateStylesLibrary(self, LibraryPath=defaultNamedNotOptArg, Result=pythoncom.Missing, NumLibraries=pythoncom.Missing):
		"""Migrates a styles library"""
		return self._ApplyTypes_(50332004, 1, (24, 0), ((8, 1), (16392, 2), (16387, 2)), u'_MigrateStylesLibrary', None,LibraryPath
			, Result, NumLibraries)

	def _PutXMLData(self, DocumentName=defaultNamedNotOptArg, ControlData=defaultNamedNotOptArg, InputData=defaultNamedNotOptArg):
		"""Put XML Data to control Inventor"""
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(50332000, LCID, 1, (8, 0), ((12, 1), (8, 1), (8, 1)),DocumentName
			, ControlData, InputData)

	# The method _RegistryEntry is actually a property, but must be used as a method to correctly pass the arguments
	def _RegistryEntry(self, SubKey=defaultNamedNotOptArg, ValueName=defaultNamedNotOptArg, RegistryHive=defaultNamedNotOptArg):
		"""Hidden property. Not for public use. Gets an entry from the system registry, including the current Inventor hive"""
		return self._ApplyTypes_(50331934, 2, (12, 0), ((8, 1), (8, 1), (3, 1)), u'_RegistryEntry', None,SubKey
			, ValueName, RegistryHive)

	def _ReplayTranscript(self, TranscriptFileName=defaultNamedNotOptArg):
		"""Hidden method. Not for public use. Replays a session transcript"""
		return self._oleobj_.InvokeTypes(50331948, LCID, 1, (24, 0), ((8, 1),),TranscriptFileName
			)

	def _SetRegistryEntry(self, SubKey=defaultNamedNotOptArg, ValueName=defaultNamedNotOptArg, Value=defaultNamedNotOptArg, RegistryHive=defaultNamedNotOptArg
			, RefreshWithEntry=defaultNamedNotOptArg):
		"""Hidden method. Not for public use. Creates an entry in the system registry, including the current Inventor hive"""
		return self._oleobj_.InvokeTypes(50331935, LCID, 1, (24, 0), ((8, 1), (8, 1), (12, 1), (3, 1), (11, 1)),SubKey
			, ValueName, Value, RegistryHive, RefreshWithEntry)

	_prop_map_get_ = {
		# Method 'ActiveAppearanceLibrary' returns object of type 'AssetLibrary'
		"ActiveAppearanceLibrary": (50332051, 2, (9, 0), (), "ActiveAppearanceLibrary", '{BE5F1900-C9E6-49B4-BA3A-1BC7FF49DCD0}'),
		# Method 'ActiveColorScheme' returns object of type 'ColorScheme'
		"ActiveColorScheme": (50331995, 2, (9, 0), (), "ActiveColorScheme", '{917CE8E7-741A-48A3-8E15-89A6DA053C40}'),
		# Method 'ActiveDocument' returns object of type 'Document'
		"ActiveDocument": (50331905, 2, (9, 0), (), "ActiveDocument", '{70109AA1-63C1-11D2-B78B-0060B0EC020B}'),
		"ActiveDocumentType": (50331906, 2, (3, 0), (), "ActiveDocumentType", None),
		# Method 'ActiveEditDocument' returns object of type 'Document'
		"ActiveEditDocument": (50332027, 2, (9, 0), (), "ActiveEditDocument", '{70109AA1-63C1-11D2-B78B-0060B0EC020B}'),
		"ActiveEditObject": (50331958, 2, (9, 0), (), "ActiveEditObject", None),
		# Method 'ActiveEnvironment' returns object of type 'Environment'
		"ActiveEnvironment": (50331964, 2, (9, 0), (), "ActiveEnvironment", '{4E27C06E-4D6A-4E53-9F84-32A0643623CF}'),
		# Method 'ActiveMaterialLibrary' returns object of type 'AssetLibrary'
		"ActiveMaterialLibrary": (50332052, 2, (9, 0), (), "ActiveMaterialLibrary", '{BE5F1900-C9E6-49B4-BA3A-1BC7FF49DCD0}'),
		# Method 'ActiveView' returns object of type 'View'
		"ActiveView": (50331910, 2, (9, 0), (), "ActiveView", '{70109AA3-63C1-11D2-B78B-0060B0EC020B}'),
		# Method 'ActiveWebView' returns object of type 'WebView'
		"ActiveWebView": (50332050, 2, (9, 0), (), "ActiveWebView", '{CCEBC8A5-7171-47B6-B9DC-067DAC0C79E7}'),
		"AllUsersAppDataPath": (50332025, 2, (8, 0), (), "AllUsersAppDataPath", None),
		# Method 'ApplicationAddIns' returns object of type 'ApplicationAddIns'
		"ApplicationAddIns": (50331941, 2, (9, 0), (), "ApplicationAddIns", '{A0481EEA-2031-11D3-B78D-0060B0F159EF}'),
		# Method 'ApplicationEvents' returns object of type 'ApplicationEvents'
		"ApplicationEvents": (50331922, 2, (13, 0), (), "ApplicationEvents", '{70109AAD-63C1-11D2-B78B-0060B0EC020B}'),
		# Method 'AssemblyEvents' returns object of type 'AssemblyEvents'
		"AssemblyEvents": (50332012, 2, (13, 0), (), "AssemblyEvents", '{BABF5BC3-9878-11D4-8DE2-0010B541CAA8}'),
		# Method 'AssemblyOptions' returns object of type 'AssemblyOptions'
		"AssemblyOptions": (50331988, 2, (9, 0), (), "AssemblyOptions", '{C6345819-0FAA-45A0-BF96-3C946F130076}'),
		# Method 'AssetLibraries' returns object of type 'AssetLibraries'
		"AssetLibraries": (50332053, 2, (9, 0), (), "AssetLibraries", '{DF8C6267-186F-4A45-8BD4-2545484B102E}'),
		# Method 'CameraEvents' returns object of type 'CameraEvents'
		"CameraEvents": (50332040, 2, (13, 0), (), "CameraEvents", '{DB89B455-6C7F-4008-986F-05D5218DA204}'),
		"CameraRollMode3Dx": (50332038, 2, (11, 0), (), "CameraRollMode3Dx", None),
		"Caption": (50331914, 2, (8, 0), (), "Caption", None),
		# Method 'ChangeManager' returns object of type 'ChangeManager'
		"ChangeManager": (50331991, 2, (9, 0), (), "ChangeManager", '{D70C53E3-58A6-48CA-95D2-AF6F4AAD04EA}'),
		# Method 'ColorSchemes' returns object of type 'ColorSchemes'
		"ColorSchemes": (50331996, 2, (9, 0), (), "ColorSchemes", '{817C825E-2D55-4E09-A69E-789E9753959D}'),
		# Method 'CommandManager' returns object of type 'CommandManager'
		"CommandManager": (50331949, 2, (9, 0), (), "CommandManager", '{9C88D3A9-C3EB-11D3-B79E-0060B0F159EF}'),
		# Method 'ContentCenter' returns object of type 'ContentCenter'
		"ContentCenter": (50331992, 2, (9, 0), (), "ContentCenter", '{8AC1686D-0646-41D5-A28F-05353181AEBA}'),
		# Method 'ContentCenterOptions' returns object of type 'ContentCenterOptions'
		"ContentCenterOptions": (50332036, 2, (9, 0), (), "ContentCenterOptions", '{650A171B-40E1-4C3B-B55E-DFB3D31C2CB8}'),
		"CurrentUserAppDataPath": (50332024, 2, (8, 0), (), "CurrentUserAppDataPath", None),
		# Method 'DesignProjectManager' returns object of type 'DesignProjectManager'
		"DesignProjectManager": (50332002, 2, (9, 0), (), "DesignProjectManager", '{4A60CB5E-1EE8-4180-A801-194704F3021E}'),
		# Method 'DisplayOptions' returns object of type 'DisplayOptions'
		"DisplayOptions": (50332017, 2, (9, 0), (), "DisplayOptions", '{48694BB1-0E75-4A39-94E0-C7C133C23305}'),
		# Method 'Documents' returns object of type 'Documents'
		"Documents": (50331907, 2, (9, 0), (), "Documents", '{70109AA2-63C1-11D2-B78B-0060B0EC020B}'),
		# Method 'DrawingOptions' returns object of type 'DrawingOptions'
		"DrawingOptions": (50332021, 2, (9, 0), (), "DrawingOptions", '{221277C1-7963-4539-B2E5-E7E16D3C75AA}'),
		# Method 'EnvironmentBaseCollection' returns object of type 'EnvironmentBaseCollection'
		"EnvironmentBaseCollection": (50331979, 2, (9, 0), (), "EnvironmentBaseCollection", '{BC985A7D-4B44-4089-870D-0AEE95D5E86A}'),
		# Method 'Environments' returns object of type 'Environments'
		"Environments": (50331963, 2, (9, 0), (), "Environments", '{D23D422B-C248-4EA4-98AF-9E6390C99964}'),
		# Method 'ErrorManager' returns object of type 'ErrorManager'
		"ErrorManager": (50332035, 2, (9, 0), (), "ErrorManager", '{7B550B22-4519-43D2-9A9E-5EC0D9FFCCD6}'),
		# Method 'FavoriteAssets' returns object of type 'AssetsEnumerator'
		"FavoriteAssets": (50332054, 2, (9, 0), (), "FavoriteAssets", '{505BB0CA-670E-4D54-AB26-F66A64DBB72C}'),
		# Method 'FileAccessEvents' returns object of type 'FileAccessEvents'
		"FileAccessEvents": (50331924, 2, (13, 0), (), "FileAccessEvents", '{32E4A319-C5E8-11D2-B77F-0060B0F159EF}'),
		# Method 'FileLocations' returns object of type 'FileLocations'
		"FileLocations": (50331943, 2, (9, 0), (), "FileLocations", '{0BF73FD9-1253-11D3-B789-0060B0F159EF}'),
		# Method 'FileManager' returns object of type 'FileManager'
		"FileManager": (50331982, 2, (9, 0), (), "FileManager", '{B00506C6-BEB7-47F6-8B1B-A5CB5DCD09B3}'),
		# Method 'FileOptions' returns object of type 'FileOptions'
		"FileOptions": (50331997, 2, (9, 0), (), "FileOptions", '{EB213A42-0727-48F0-9BCF-C55F6CB4CD78}'),
		# Method 'FileUIEvents' returns object of type 'FileUIEvents'
		"FileUIEvents": (50331923, 2, (13, 0), (), "FileUIEvents", '{70109AAA-63C1-11D2-B78B-0060B0EC020B}'),
		"FlythroughMode3Dx": (50332037, 2, (11, 0), (), "FlythroughMode3Dx", None),
		# Method 'GeneralOptions' returns object of type 'GeneralOptions'
		"GeneralOptions": (50331989, 2, (9, 0), (), "GeneralOptions", '{DBB345F5-06CB-4B20-96B8-C47EF589ECBE}'),
		# Method 'HardwareOptions' returns object of type 'HardwareOptions'
		"HardwareOptions": (50332010, 2, (9, 0), (), "HardwareOptions", '{9A19AF07-A6BF-43AA-ABF3-870CA1CF329F}'),
		"Height": (50331975, 2, (3, 0), (), "Height", None),
		# Method 'HelpManager' returns object of type 'HelpManager'
		"HelpManager": (50331950, 2, (9, 0), (), "HelpManager", '{9C88D3AA-C3EB-11D3-B79E-0060B0F159EF}'),
		"InstallPath": (50332023, 2, (8, 0), (), "InstallPath", None),
		"IsCIPEnabled": (50331926, 2, (11, 0), (), "IsCIPEnabled", None),
		"LanguageCode": (50332044, 2, (8, 0), (), "LanguageCode", None),
		"LanguageName": (50331953, 2, (8, 0), (), "LanguageName", None),
		# Method 'LanguageTools' returns object of type 'LanguageTools'
		"LanguageTools": (50332026, 2, (9, 0), (), "LanguageTools", '{0420658E-CCD1-4100-BFA1-AD78AA655551}'),
		"Left": (50331974, 2, (3, 0), (), "Left", None),
		"Locale": (50331952, 2, (3, 0), (), "Locale", None),
		"MRUDisplay": (50332030, 2, (11, 0), (), "MRUDisplay", None),
		"MRUEnabled": (50331925, 2, (11, 0), (), "MRUEnabled", None),
		"MainFrameHWND": (50331946, 2, (3, 0), (), "MainFrameHWND", None),
		"MaterialDisplayUnits": (50332055, 2, (3, 0), (), "MaterialDisplayUnits", None),
		# Method 'MeasureTools' returns object of type 'MeasureTools'
		"MeasureTools": (50332018, 2, (9, 0), (), "MeasureTools", '{78B3596A-176A-43F5-A65C-4BDFFC042236}'),
		# Method 'ModelingEvents' returns object of type 'ModelingEvents'
		"ModelingEvents": (50332011, 2, (13, 0), (), "ModelingEvents", '{B0128AFD-14AE-4FD6-AED0-314D1F79F3EB}'),
		# Method 'NotebookOptions' returns object of type 'NotebookOptions'
		"NotebookOptions": (50332009, 2, (9, 0), (), "NotebookOptions", '{CEF827E8-5A0A-452D-83BB-1A88815C1601}'),
		"OpenDocumentsDisplay": (50332041, 2, (11, 0), (), "OpenDocumentsDisplay", None),
		# Method 'PartOptions' returns object of type 'PartOptions'
		"PartOptions": (50332006, 2, (9, 0), (), "PartOptions", '{986FCF92-8A47-4DEC-9007-DD852292DE71}'),
		# Method 'Preferences' returns object of type 'ObjectsEnumeratorByVariant'
		"Preferences": (50331939, 2, (9, 0), (), "Preferences", '{9235396B-0350-11D3-B787-0060B0F159EF}'),
		# Method 'PresentationOptions' returns object of type 'PresentationOptions'
		"PresentationOptions": (50332048, 2, (9, 0), (), "PresentationOptions", '{6E68C1F1-A6AF-4235-8E86-AB031F7813E3}'),
		"Ready": (50331998, 2, (11, 0), (), "Ready", None),
		# Method 'ReferenceKeyEvents' returns object of type 'ReferenceKeyEvents'
		"ReferenceKeyEvents": (50431491, 2, (13, 0), (), "ReferenceKeyEvents", '{D893A325-547B-4DE2-8F8B-BD9594025979}'),
		# Method 'RepresentationEvents' returns object of type 'RepresentationEvents'
		"RepresentationEvents": (50332016, 2, (13, 0), (), "RepresentationEvents", '{955CB4BF-782F-4A58-8538-4E1028EA5D20}'),
		# Method 'SaveOptions' returns object of type 'SaveOptions'
		"SaveOptions": (50332014, 2, (9, 0), (), "SaveOptions", '{A6EC8B79-931A-409E-90CE-3EE28CB9F9F4}'),
		"ScreenUpdating": (50332028, 2, (11, 0), (), "ScreenUpdating", None),
		"SilentOperation": (50331954, 2, (11, 0), (), "SilentOperation", None),
		# Method 'Sketch3DOptions' returns object of type 'Sketch3DOptions'
		"Sketch3DOptions": (50332007, 2, (9, 0), (), "Sketch3DOptions", '{D39AB98F-45E0-4CAE-A0F2-4490804F2AD3}'),
		# Method 'SketchEvents' returns object of type 'SketchEvents'
		"SketchEvents": (50332015, 2, (13, 0), (), "SketchEvents", '{579B848D-41FD-4A4E-87F8-58A213360623}'),
		# Method 'SketchOptions' returns object of type 'SketchOptions'
		"SketchOptions": (50331999, 2, (9, 0), (), "SketchOptions", '{8B657FE9-BF0A-4AED-B1FB-166229D406B3}'),
		# Method 'SoftwareVersion' returns object of type 'SoftwareVersion'
		"SoftwareVersion": (50331956, 2, (9, 0), (), "SoftwareVersion", '{076C16D1-4994-11D4-9E0F-0010A4C72F07}'),
		"StatusBarText": (50331962, 2, (8, 0), (), "StatusBarText", None),
		# Method 'StyleEvents' returns object of type 'StyleEvents'
		"StyleEvents": (50332019, 2, (13, 0), (), "StyleEvents", '{4732A4F0-D435-4F10-8548-4DBE68276D58}'),
		# Method 'StylesManager' returns object of type 'StylesManager'
		"StylesManager": (50332039, 2, (9, 0), (), "StylesManager", '{D93EE206-0CA6-401E-B74E-0D9E4F924751}'),
		"SubscriptionStatus": (50332043, 2, (3, 0), (), "SubscriptionStatus", None),
		"SupportsFileManagement": (50332033, 2, (11, 0), (), "SupportsFileManagement", None),
		# Method 'TestManager' returns object of type 'TestManager'
		"TestManager": (50331986, 2, (9, 0), (), "TestManager", '{369933DF-0F63-46AA-919B-17C91F385C9E}'),
		"Top": (50331973, 2, (3, 0), (), "Top", None),
		# Method 'TransactionManager' returns object of type 'TransactionManager'
		"TransactionManager": (50331944, 2, (9, 0), (), "TransactionManager", '{AE277672-2FDC-11D3-B78F-0060B0F159EF}'),
		# Method 'TransientBRep' returns object of type 'TransientBRep'
		"TransientBRep": (50331917, 2, (9, 0), (), "TransientBRep", '{2BFE4397-C369-4CEF-90C9-D5C8AE90BC9F}'),
		# Method 'TransientGeometry' returns object of type 'TransientGeometry'
		"TransientGeometry": (50331959, 2, (9, 0), (), "TransientGeometry", '{97ECB3AE-6C6E-4D8A-A91E-564314494EB8}'),
		# Method 'TransientObjects' returns object of type 'TransientObjects'
		"TransientObjects": (50331961, 2, (9, 0), (), "TransientObjects", '{6BA435D7-BBD6-11D4-8DE6-0010B541CAA8}'),
		# Method 'TutorialsManager' returns object of type 'TutorialsManager'
		"TutorialsManager": (50332047, 2, (9, 0), (), "TutorialsManager", '{0169EC1F-0694-4353-B28D-3D74B59402D0}'),
		"Type": (0, 2, (3, 0), (), "Type", None),
		# Method 'UnitsOfMeasure' returns object of type 'UnitsOfMeasure'
		"UnitsOfMeasure": (50332029, 2, (9, 0), (), "UnitsOfMeasure", '{D007B6F9-71BB-48FF-B14C-EE5D633CB0C3}'),
		# Method 'UserInterfaceManager' returns object of type 'UserInterfaceManager'
		"UserInterfaceManager": (50331990, 2, (9, 0), (), "UserInterfaceManager", '{3AF77BAF-EECD-4301-823D-9B604FE5C176}'),
		"UserName": (50331965, 2, (8, 0), (), "UserName", None),
		# Method 'VBAProjects' returns object of type 'InventorVBAProjects'
		"VBAProjects": (50331972, 2, (9, 0), (), "VBAProjects", '{EEB0116A-7B74-4A9C-B2FF-96BC31812249}'),
		"VBE": (50331968, 2, (9, 0), (), "VBE", None),
		# Method 'Views' returns object of type 'ViewsEnumerator'
		"Views": (50331911, 2, (9, 0), (), "Views", '{2C16787B-83FF-11D4-8DDB-0010B541CAA8}'),
		"Visible": (50331916, 2, (11, 0), (), "Visible", None),
		# Method 'WebViews' returns object of type 'WebViews'
		"WebViews": (50332049, 2, (9, 0), (), "WebViews", '{B894B815-AEF1-4FAA-938A-2131E2E5190F}'),
		"Width": (50331976, 2, (3, 0), (), "Width", None),
		"WindowState": (50331978, 2, (3, 0), (), "WindowState", None),
		# Method '_AppPerformanceMonitor' returns object of type '_AppPerformanceMonitor'
		"_AppPerformanceMonitor": (50331980, 2, (9, 0), (), "_AppPerformanceMonitor", '{DDC2F383-3824-49E3-837C-7387D4775893}'),
		"_CanReplayTranscript": (50331947, 2, (11, 0), (), "_CanReplayTranscript", None),
		# Method '_DebugInstrumentation' returns object of type 'DebugInstrumentation'
		"_DebugInstrumentation": (50331966, 2, (13, 0), (), "_DebugInstrumentation", '{F6F33559-6984-11D5-8DF3-0010B541CAA8}'),
		"_DefaultPrinter3DName": (50332056, 2, (8, 0), (), "_DefaultPrinter3DName", None),
		"_ForceMigrationOnOpen": (50331984, 2, (11, 0), (), "_ForceMigrationOnOpen", None),
		"_HarvestStylesOnOpen": (50331993, 2, (11, 0), (), "_HarvestStylesOnOpen", None),
		"_PurgeStylesOnOpen": (50331994, 2, (11, 0), (), "_PurgeStylesOnOpen", None),
		"_SuppressFileDirtyEvents": (50332001, 2, (11, 0), (), "_SuppressFileDirtyEvents", None),
		"_TestIO": (50331969, 2, (9, 0), (), "_TestIO", None),
		"_TranscriptAPIChanges": (50332003, 2, (11, 0), (), "_TranscriptAPIChanges", None),
		"_TranscriptFileName": (50331945, 2, (8, 0), (), "_TranscriptFileName", None),
		# Method 'iFeatureOptions' returns object of type 'iFeatureOptions'
		"iFeatureOptions": (50332008, 2, (9, 0), (), "iFeatureOptions", '{2B03891E-1B59-4576-8160-C61EA6E6D0DC}'),
	}
	_prop_map_put_ = {
		"ActiveAppearanceLibrary": ((50332051, LCID, 4, 0),()),
		"ActiveMaterialLibrary": ((50332052, LCID, 4, 0),()),
		"CameraRollMode3Dx": ((50332038, LCID, 4, 0),()),
		"Caption": ((50331914, LCID, 4, 0),()),
		"FlythroughMode3Dx": ((50332037, LCID, 4, 0),()),
		"Height": ((50331975, LCID, 4, 0),()),
		"Left": ((50331974, LCID, 4, 0),()),
		"MRUDisplay": ((50332030, LCID, 4, 0),()),
		"MRUEnabled": ((50331925, LCID, 4, 0),()),
		"MaterialDisplayUnits": ((50332055, LCID, 4, 0),()),
		"OpenDocumentsDisplay": ((50332041, LCID, 4, 0),()),
		"ScreenUpdating": ((50332028, LCID, 4, 0),()),
		"SilentOperation": ((50331954, LCID, 4, 0),()),
		"StatusBarText": ((50331962, LCID, 4, 0),()),
		"SupportsFileManagement": ((50332033, LCID, 4, 0),()),
		"Top": ((50331973, LCID, 4, 0),()),
		"UserName": ((50331965, LCID, 4, 0),()),
		"Visible": ((50331916, LCID, 4, 0),()),
		"Width": ((50331976, LCID, 4, 0),()),
		"WindowState": ((50331978, LCID, 4, 0),()),
		"_DefaultPrinter3DName": ((50332056, LCID, 4, 0),()),
		"_ForceMigrationOnOpen": ((50331984, LCID, 4, 0),()),
		"_HarvestStylesOnOpen": ((50331993, LCID, 4, 0),()),
		"_PurgeStylesOnOpen": ((50331994, LCID, 4, 0),()),
		"_SuppressFileDirtyEvents": ((50332001, LCID, 4, 0),()),
		"_TestIO": ((50331969, LCID, 4, 0),()),
		"_TranscriptAPIChanges": ((50332003, LCID, 4, 0),()),
		"_UpdateAnnotationsOnSheetActivate": ((50331985, LCID, 4, 0),()),
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

win32com.client.CLSIDToClass.RegisterCLSID( "{70109AA0-63C1-11D2-B78B-0060B0EC020B}", Application )
