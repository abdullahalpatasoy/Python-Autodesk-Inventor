# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.00
# By python version 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Wed Nov 18 08:47:11 2015
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
class Document(DispatchBaseClass):
	"""Document Object"""
	CLSID = IID('{70109AA1-63C1-11D2-B78B-0060B0EC020B}')
	coclass_clsid = IID('{0249C8A3-806D-4A1D-8BC0-4699BE1203AF}')

	def Activate(self):
		"""Makes this Document the active one (receives user-focus)"""
		return self._oleobj_.InvokeTypes(50332166, LCID, 1, (24, 0), (),)

	def Close(self, SkipSave=False):
		"""Closes this document"""
		return self._oleobj_.InvokeTypes(50332167, LCID, 1, (24, 0), ((11, 49),),SkipSave
			)

	# Result is of type HighlightSet
	def CreateHighlightSet(self):
		"""Methods that create a new highlight set"""
		ret = self._oleobj_.InvokeTypes(50332247, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, u'CreateHighlightSet', '{545F2567-592E-45DA-A262-77BD7E546F7A}')
		return ret

	# Result is of type DocumentsEnumerator
	def FindWhereUsed(self, FullFileName=defaultNamedNotOptArg):
		"""Obtains the set of documents that reference the given file within this document"""
		ret = self._oleobj_.InvokeTypes(50332220, LCID, 1, (9, 0), ((8, 1),),FullFileName
			)
		if ret is not None:
			ret = Dispatch(ret, u'FindWhereUsed', '{ACE59077-7778-11D4-8DD8-0010B541CAA8}')
		return ret

	def GetLocationFoundIn(self, LocationName=pythoncom.Missing, LocationType=pythoncom.Missing):
		"""Obtains the name of the Location this file was found in"""
		return self._ApplyTypes_(50332163, 1, (24, 0), ((16392, 2), (16387, 2)), u'GetLocationFoundIn', None,LocationName
			, LocationType)

	def GetMissingAddInBehavior(self, ClientId=pythoncom.Missing, DisabledCommandTypesEnum=pythoncom.Missing, DisabledCommands=pythoncom.Missing):
		"""Gets the commands to be disabled when a particular AddIn is absent"""
		return self._ApplyTypes_(50332244, 1, (24, 0), ((16392, 2), (16387, 2), (16393, 2)), u'GetMissingAddInBehavior', None,ClientId
			, DisabledCommandTypesEnum, DisabledCommands)

	def GetPrivateStorage(self, StorageName=defaultNamedNotOptArg, CreateIfNecessary=defaultNamedNotOptArg):
		"""Obtains a private sub-storage within this Document with the given name. Can create one, if one does not exist"""
		ret = self._oleobj_.InvokeTypes(50332175, LCID, 1, (13, 0), ((8, 1), (11, 1)),StorageName
			, CreateIfNecessary)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, u'GetPrivateStorage', None)
		return ret

	def GetPrivateStream(self, StreamName=defaultNamedNotOptArg, CreateIfNecessary=defaultNamedNotOptArg):
		"""Obtains a private stream within this Document with the given name. Can create one, if one does not exist"""
		ret = self._oleobj_.InvokeTypes(50332176, LCID, 1, (13, 0), ((8, 1), (11, 1)),StreamName
			, CreateIfNecessary)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, u'GetPrivateStream', None)
		return ret

	# Result is of type ObjectsEnumerator
	# The method GetReferencedOLEFileDescriptors2 is actually a property, but must be used as a method to correctly pass the arguments
	def GetReferencedOLEFileDescriptors2(self, ReferenceType=3329):
		"""Gets the collection of OLE attachments made in this Document that match the input type. Returns all OLE attachments if type is kOLEDocumentUnknownObject"""
		ret = self._oleobj_.InvokeTypes(50332264, LCID, 2, (9, 0), ((3, 49),),ReferenceType
			)
		if ret is not None:
			ret = Dispatch(ret, u'GetReferencedOLEFileDescriptors2', '{A94DCF5E-90E9-4F60-BB55-F65B4618ECD5}')
		return ret

	def HasPrivateStorage(self, StorageName=defaultNamedNotOptArg):
		"""Obtains a Boolean flag indicating if the specified sub-storage exists within this Document"""
		return self._oleobj_.InvokeTypes(50332173, LCID, 1, (11, 0), ((8, 1),),StorageName
			)

	def HasPrivateStream(self, StreamName=defaultNamedNotOptArg):
		"""Obtains a Boolean flag indicating if the specified stream exists within this Document"""
		return self._oleobj_.InvokeTypes(50332174, LCID, 1, (11, 0), ((8, 1),),StreamName
			)

	def LockSaveSet(self):
		"""Use F1 key to display help topic"""
		return self._oleobj_.InvokeTypes(50332256, LCID, 1, (24, 0), (),)

	def Migrate(self):
		"""Method that forces the document to migrate if it needs migration.  If the document doesnt need to be migrated, this method does nothing and returns a success."""
		return self._oleobj_.InvokeTypes(50332251, LCID, 1, (24, 0), (),)

	def PutInternalName(self, Name=defaultNamedNotOptArg, Number=defaultNamedNotOptArg, Custom=defaultNamedNotOptArg, InternalName=pythoncom.Missing):
		"""Constructs and sets the Internal Name for this Document from strings supplied. This can only be done on a previously un-saved document (New or SaveCopyAs)"""
		return self._ApplyTypes_(50332221, 1, (24, 0), ((8, 1), (8, 1), (8, 1), (16392, 2)), u'PutInternalName', None,Name
			, Number, Custom, InternalName)

	def PutInternalNameAndRevisionId(self, InternalNameToken=defaultNamedNotOptArg, RevisionIdToken=defaultNamedNotOptArg, InternalName=pythoncom.Missing, RevisionId=pythoncom.Missing):
		"""Constructs and sets the Internal Name and Revision Identifier for this Document from strings supplied. This can only be done on a previously un-saved document (New or SaveCopyAs)"""
		return self._ApplyTypes_(50332246, 1, (24, 0), ((8, 1), (8, 1), (16392, 2), (16392, 2)), u'PutInternalNameAndRevisionId', None,InternalNameToken
			, RevisionIdToken, InternalName, RevisionId)

	def Rebuild(self):
		"""Performs compute operations on all of the entities within this Document's scope as if all of the driving entities had been 'dirtied'"""
		return self._oleobj_.InvokeTypes(50332207, LCID, 1, (24, 0), (),)

	def Rebuild2(self, AcceptErrorsAndContinue=True):
		"""Method that performs compute operations on all of the entities within this Document's scope as if all of the driving entities had been 'dirtied', returns False if any errors are encountered during the rebuild"""
		return self._oleobj_.InvokeTypes(50332249, LCID, 1, (11, 0), ((11, 49),),AcceptErrorsAndContinue
			)

	def ReleaseReference(self):
		"""Releases the reference that gets added if a document is opened invisibly thru the API. Releasing the reference on a hidden document makes it a candidate for closure the next time Inventor closes all unreferenced documents. This is not a COM reference release"""
		return self._oleobj_.InvokeTypes(50332253, LCID, 1, (24, 0), (),)

	def RevertReservedForWriteByMe(self):
		"""Reverts the file checked out by the caller"""
		return self._oleobj_.InvokeTypes(50332227, LCID, 1, (24, 0), (),)

	def Save(self):
		"""Saves this document to disk"""
		return self._oleobj_.InvokeTypes(50332169, LCID, 1, (24, 0), (),)

	def Save2(self, SaveDependents=True, DocumentsToSave=defaultNamedOptArg):
		"""Saves the specified documents"""
		return self._oleobj_.InvokeTypes(50332262, LCID, 1, (24, 0), ((11, 49), (12, 17)),SaveDependents
			, DocumentsToSave)

	def SaveAs(self, FileName=defaultNamedNotOptArg, SaveCopyAs=defaultNamedNotOptArg):
		"""Saves this document into a file of the specified name. None of the dependent documents get saved"""
		return self._oleobj_.InvokeTypes(50332170, LCID, 1, (24, 0), ((8, 1), (11, 1)),FileName
			, SaveCopyAs)

	def SetMissingAddInBehavior(self, ClientId=defaultNamedNotOptArg, DisabledCommandTypesEnum=defaultNamedNotOptArg, DisabledCommands=defaultNamedOptArg):
		"""Sets the commands to be disabled when a particular AddIn is absent"""
		return self._oleobj_.InvokeTypes(50332243, LCID, 1, (24, 0), ((8, 1), (3, 1), (12, 17)),ClientId
			, DisabledCommandTypesEnum, DisabledCommands)

	def SetThumbnailSaveOption(self, SaveOption=defaultNamedNotOptArg, ImageFullFileName=u''):
		"""Method that sets the thumbnail (preview picture) save option"""
		return self._ApplyTypes_(50332260, 1, (24, 32), ((3, 1), (8, 49)), u'SetThumbnailSaveOption', None,SaveOption
			, ImageFullFileName)

	def Update(self):
		"""Performs compute operations on all of the entities within this Document's scope that may be out of date with respect to their driving entities"""
		return self._oleobj_.InvokeTypes(50332206, LCID, 1, (24, 0), (),)

	def Update2(self, AcceptErrorsAndContinue=True):
		"""This is a variation of Document_Update. This method indicates if error occurred during compute and allows users to ignore those errors"""
		return self._oleobj_.InvokeTypes(50332235, LCID, 1, (11, 0), ((11, 49),),AcceptErrorsAndContinue
			)

	def _DeleteUnusedEmbeddings(self, Preview=defaultNamedNotOptArg, NumEmbeddings=pythoncom.Missing, Embeddings=defaultNamedNotOptArg):
		"""Hidden method to delete all the OLE embeddings that are not referenced by this document"""
		return self._ApplyTypes_(50332257, 1, (24, 0), ((11, 1), (16387, 2), (24584, 3)), u'_DeleteUnusedEmbeddings', None,Preview
			, NumEmbeddings, Embeddings)

	# The method _IsTemplateUsed is actually a property, but must be used as a method to correctly pass the arguments
	def _IsTemplateUsed(self, TemplateGuid=defaultNamedNotOptArg, FileName=defaultNamedNotOptArg):
		"""Hidden property. Not for public use"""
		return self._oleobj_.InvokeTypes(50332214, LCID, 2, (11, 0), ((8, 1), (8, 1)),TemplateGuid
			, FileName)

	def _PutInternalNameAndFileVersion(self, Name=defaultNamedNotOptArg, Number=defaultNamedNotOptArg, Custom=defaultNamedNotOptArg, Revision=defaultNamedNotOptArg
			, InternalName=pythoncom.Missing, FileVersion=pythoncom.Missing):
		"""*** DEFUNCT SINCE R5.3"""
		return self._ApplyTypes_(50332192, 1, (24, 0), ((8, 1), (8, 1), (8, 1), (8, 1), (16392, 2), (16392, 2)), u'_PutInternalNameAndFileVersion', None,Name
			, Number, Custom, Revision, InternalName, FileVersion
			)

	def _VBAProjectChanged(self):
		"""Hidden method to force a document to require updating when a VBA project has  been modified."""
		return self._oleobj_.InvokeTypes(50332258, LCID, 1, (24, 0), (),)

	def _XmlOutToFile(self, schemaXmlString=defaultNamedNotOptArg, outXmlFile=defaultNamedNotOptArg):
		"""Hidden method. Not for public use, Output Validation XML"""
		return self._oleobj_.InvokeTypes(50332230, LCID, 1, (24, 0), ((8, 1), (8, 1)),schemaXmlString
			, outXmlFile)

	_prop_map_get_ = {
		"ActivatedObject": (50332208, 2, (9, 0), (), "ActivatedObject", None),
		# Method 'AllReferencedDocuments' returns object of type 'DocumentsEnumerator'
		"AllReferencedDocuments": (50332242, 2, (9, 0), (), "AllReferencedDocuments", '{ACE59077-7778-11D4-8DD8-0010B541CAA8}'),
		# Method 'AttributeManager' returns object of type 'AttributeManager'
		"AttributeManager": (50332210, 2, (9, 0), (), "AttributeManager", '{46D51BD4-B58D-4C94-BA7A-124B184AC687}'),
		# Method 'AttributeSets' returns object of type 'AttributeSets'
		"AttributeSets": (2130706452, 2, (9, 0), (), "AttributeSets", '{790B4EB3-7947-4D08-9510-372E93A24CF1}'),
		# Method 'BrowserPanes' returns object of type 'BrowserPanes'
		"BrowserPanes": (50332215, 2, (9, 0), (), "BrowserPanes", '{1EBEC999-3A4D-4A4C-A35A-3F2E773DD56D}'),
		"Compacted": (50332219, 2, (11, 0), (), "Compacted", None),
		"DatabaseRevisionId": (50332245, 2, (8, 0), (), "DatabaseRevisionId", None),
		"DefaultCommand": (50332234, 2, (8, 0), (), "DefaultCommand", None),
		"Dirty": (50332168, 2, (11, 0), (), "Dirty", None),
		"DisabledCommandTypes": (50332225, 2, (3, 0), (), "DisabledCommandTypes", None),
		"DisplayName": (50332161, 2, (8, 0), (), "DisplayName", None),
		"DisplayNameOverridden": (50332261, 2, (11, 0), (), "DisplayNameOverridden", None),
		# Method 'DocumentEvents' returns object of type 'DocumentEvents'
		"DocumentEvents": (50332171, 2, (13, 0), (), "DocumentEvents", '{70109AAC-63C1-11D2-B78B-0060B0EC020B}'),
		# Method 'DocumentInterests' returns object of type 'DocumentInterests'
		"DocumentInterests": (50332250, 2, (9, 0), (), "DocumentInterests", '{B1DA2E33-F616-41D4-917A-CEB1138058D0}'),
		# Method 'DocumentSubType' returns object of type 'DocumentSubType'
		"DocumentSubType": (50332226, 2, (9, 0), (), "DocumentSubType", '{D3EDB5BC-7B47-42B9-9D77-F3A2676EC15B}'),
		"DocumentType": (50332172, 2, (3, 0), (), "DocumentType", None),
		# Method 'File' returns object of type 'File'
		"File": (50332236, 2, (9, 0), (), "File", '{6E5CDAB2-6BA5-4EAD-B357-78646BE0A813}'),
		"FileSaveCounter": (50332182, 2, (3, 0), (), "FileSaveCounter", None),
		"FullDocumentName": (50332237, 2, (8, 0), (), "FullDocumentName", None),
		"FullFileName": (50332162, 2, (8, 0), (), "FullFileName", None),
		# Method 'GraphicsDataSetsCollection' returns object of type 'GraphicsDataSetsCollection'
		"GraphicsDataSetsCollection": (50332211, 2, (9, 0), (), "GraphicsDataSetsCollection", '{8C2CC3CF-A455-40D6-8505-56A702F6FB77}'),
		# Method 'HighlightSets' returns object of type 'HighlightSets'
		"HighlightSets": (50332217, 2, (9, 0), (), "HighlightSets", '{DD60CA37-AB7B-491F-AD9E-C9DF3B4B5BBB}'),
		"InternalName": (50332263, 2, (8, 0), (), "InternalName", None),
		# Method 'InventorDocument' returns object of type 'Document'
		"InventorDocument": (50332255, 2, (9, 0), (), "InventorDocument", '{70109AA1-63C1-11D2-B78B-0060B0EC020B}'),
		"IsModifiable": (50332228, 2, (11, 0), (), "IsModifiable", None),
		"NeedsMigrating": (50332252, 2, (11, 0), (), "NeedsMigrating", None),
		"Open": (50332238, 2, (11, 0), (), "Open", None),
		"OwnershipType": (50332254, 2, (3, 0), (), "OwnershipType", None),
		"Parent": (2130706434, 2, (9, 0), (), "Parent", None),
		# Method 'PrintManager' returns object of type 'PrintManager'
		"PrintManager": (50332209, 2, (9, 0), (), "PrintManager", '{69190E26-316F-47BD-AE75-8B64641C18C8}'),
		# Method 'PropertySets' returns object of type 'PropertySets'
		"PropertySets": (50332191, 2, (9, 0), (), "PropertySets", '{73F35CC8-ED6E-11D2-B785-0060B0F159EF}'),
		"RecentChanges": (50332231, 2, (3, 0), (), "RecentChanges", None),
		# Method 'ReferenceKeyManager' returns object of type 'ReferenceKeyManager'
		"ReferenceKeyManager": (50332216, 2, (9, 0), (), "ReferenceKeyManager", '{1405C19D-F8AC-41AD-AAB2-D0923BD45C15}'),
		# Method 'ReferencedDocumentDescriptors' returns object of type 'DocumentDescriptorsEnumerator'
		"ReferencedDocumentDescriptors": (50332239, 2, (9, 0), (), "ReferencedDocumentDescriptors", '{DBD3CBEE-DBBC-4A71-B122-33A8D1786D20}'),
		# Method 'ReferencedDocuments' returns object of type 'DocumentsEnumerator'
		"ReferencedDocuments": (50332240, 2, (9, 0), (), "ReferencedDocuments", '{ACE59077-7778-11D4-8DD8-0010B541CAA8}'),
		# Method 'ReferencedFileDescriptors' returns object of type 'ReferencedFileDescriptors'
		"ReferencedFileDescriptors": (50332179, 2, (9, 0), (), "ReferencedFileDescriptors", '{9E0BA9CB-E916-11D2-B785-0060B0F159EF}'),
		# Method 'ReferencedFiles' returns object of type 'DocumentsEnumerator'
		"ReferencedFiles": (50332178, 2, (9, 0), (), "ReferencedFiles", '{ACE59077-7778-11D4-8DD8-0010B541CAA8}'),
		# Method 'ReferencedOLEFileDescriptors' returns object of type 'ReferencedOLEFileDescriptors'
		"ReferencedOLEFileDescriptors": (50332180, 2, (9, 0), (), "ReferencedOLEFileDescriptors", '{9CAF98A0-33EA-11D3-B78F-0060B0F159EF}'),
		# Method 'ReferencedOLEFileDescriptors2' returns object of type 'ObjectsEnumerator'
		"ReferencedOLEFileDescriptors2": (50332264, 2, (9, 0), ((3, 49),), "ReferencedOLEFileDescriptors2", '{A94DCF5E-90E9-4F60-BB55-F65B4618ECD5}'),
		# Method 'ReferencingDocuments' returns object of type 'DocumentsEnumerator'
		"ReferencingDocuments": (50332241, 2, (9, 0), (), "ReferencingDocuments", '{ACE59077-7778-11D4-8DD8-0010B541CAA8}'),
		# Method 'RenderStyles' returns object of type 'RenderStyles'
		"RenderStyles": (50332212, 2, (9, 0), (), "RenderStyles", '{1F76C4FA-DB71-4D87-8390-1529297ED5A9}'),
		"RequiresUpdate": (50332205, 2, (11, 0), (), "RequiresUpdate", None),
		"ReservedForWrite": (50332185, 2, (11, 0), (), "ReservedForWrite", None),
		"ReservedForWriteByMe": (50332186, 2, (11, 0), (), "ReservedForWriteByMe", None),
		"ReservedForWriteLogin": (50332188, 2, (8, 0), (), "ReservedForWriteLogin", None),
		"ReservedForWriteName": (50332187, 2, (8, 0), (), "ReservedForWriteName", None),
		"ReservedForWriteTime": (50332190, 2, (7, 0), (), "ReservedForWriteTime", None),
		"ReservedForWriteVersion": (50332189, 2, (3, 0), (), "ReservedForWriteVersion", None),
		"RevisionId": (50332222, 2, (8, 0), (), "RevisionId", None),
		# Method 'SelectSet' returns object of type 'SelectSet'
		"SelectSet": (50332218, 2, (9, 0), (), "SelectSet", '{189559A8-0C9B-4F77-93E9-8330AAAD7943}'),
		# Method 'SelectionPreferences' returns object of type 'SelectionPreferences'
		"SelectionPreferences": (50332265, 2, (9, 0), (), "SelectionPreferences", '{1907E11C-C275-4008-95FA-9AC7539E1A7C}'),
		"SelectionPriority": (50332248, 2, (3, 0), (), "SelectionPriority", None),
		# Method 'SoftwareVersionCreated' returns object of type 'SoftwareVersion'
		"SoftwareVersionCreated": (50332201, 2, (9, 0), (), "SoftwareVersionCreated", '{076C16D1-4994-11D4-9E0F-0010A4C72F07}'),
		# Method 'SoftwareVersionSaved' returns object of type 'SoftwareVersion'
		"SoftwareVersionSaved": (50332202, 2, (9, 0), (), "SoftwareVersionSaved", '{076C16D1-4994-11D4-9E0F-0010A4C72F07}'),
		"SubType": (50332194, 2, (8, 0), (), "SubType", None),
		# Method 'Thumbnail' returns object of type 'Picture'
		"Thumbnail": (50332229, 2, (9, 0), (), "Thumbnail", '{7BF80981-BF32-101A-8BBB-00AA00300CAB}'),
		"ThumbnailSaveOption": (50332259, 2, (3, 0), (), "ThumbnailSaveOption", None),
		"Type": (0, 2, (3, 0), (), "Type", None),
		# Method 'UnitsOfMeasure' returns object of type 'UnitsOfMeasure'
		"UnitsOfMeasure": (50332203, 2, (9, 0), (), "UnitsOfMeasure", '{D007B6F9-71BB-48FF-B14C-EE5D633CB0C3}'),
		# Method 'VBAProject' returns object of type 'InventorVBAProject'
		"VBAProject": (50332223, 2, (9, 0), (), "VBAProject", '{95C6C576-FC7A-4B16-B565-BFABEF69B013}'),
		# Method 'Views' returns object of type 'Views'
		"Views": (50332164, 2, (9, 0), (), "Views", '{70109AA4-63C1-11D2-B78B-0060B0EC020B}'),
		"_ComatoseNodesCount": (50332200, 2, (3, 0), (), "_ComatoseNodesCount", None),
		"_DefaultCommand": (50332177, 2, (3, 0), (), "_DefaultCommand", None),
		# Method '_DocPerformanceMonitor' returns object of type '_DocPerformanceMonitor'
		"_DocPerformanceMonitor": (50332224, 2, (13, 0), (), "_DocPerformanceMonitor", '{89832854-67B3-4DBF-B8E6-715435D51FE2}'),
		"_InternalName": (50332193, 2, (8, 0), (), "_InternalName", None),
		"_PrimaryDeselGUID": (50332213, 2, (8, 0), (), "_PrimaryDeselGUID", None),
		"_SickNodesCount": (50332199, 2, (3, 0), (), "_SickNodesCount", None),
	}
	_prop_map_put_ = {
		"Dirty": ((50332168, LCID, 4, 0),()),
		"DisabledCommandTypes": ((50332225, LCID, 4, 0),()),
		"DisplayName": ((50332161, LCID, 4, 0),()),
		"DisplayNameOverridden": ((50332261, LCID, 4, 0),()),
		"FullFileName": ((50332162, LCID, 4, 0),()),
		"ReservedForWriteByMe": ((50332186, LCID, 4, 0),()),
		"SelectionPriority": ((50332248, LCID, 4, 0),()),
		"SubType": ((50332194, LCID, 4, 0),()),
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

win32com.client.CLSIDToClass.RegisterCLSID( "{70109AA1-63C1-11D2-B78B-0060B0EC020B}", Document )
