import win32com.client

app=win32com.client.Dispatch("Inventor.Application") #Autodesk Inventor başlatılıyor. (Autodesk Inventor is running)
app.Visible = False #Autodesk Inventor arka planda çalışmasını istiyoruz. I want to running Autodesk Inventor in backend.

Part_FileName_Orig = raw_input('Dosya adresini girin:')  #You shall enter the file directory.

PartDoc=app.Documents.Open(Part_FileName_Orig)

print 'Erisilen dosya adeti:' + str(app.Documents.Count)


invDoc=app.ActiveDocument
docName=invDoc.DisplayName

print 'Erisilen dosya adi:' + docName


invDesignInfo=invDoc.PropertySets.Item("Design Tracking Properties")
invPartNumberProperty = invDesignInfo.Item("Mass")
invPartNumberVolume = invDesignInfo.Item("Volume")

print str(invPartNumberProperty) + ' gr'
print str(invPartNumberVolume) + ' dm3'

PartDoc.Close(True)

raw_input('Kapatmak icin enter a basin.')
