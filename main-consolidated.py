import xml.etree.ElementTree as ET
import requests
import os
import array

endpoint = 'https://uat-store-api.priipcloud.com/product-store/api/product/'
token = '[token scrubbed]'
params = '/org/17'

#---
# Function which handles all the logic in relation to how the client sends us information
#
def operation(toUpload):
    
    if toUpload == 'US'
        region = 'US'
    elif toUpload == 'GSSP':
        region = 'gssp'
    else:
        region = ['US','gssp']
    
    for reg in region:
            
        files = []
        files2 = []

        if reg == US:
            docTypes = ['traded','final'] #SEC does not include indicative products
        else:
            docTypes = ['indicative','final'] #GSSP does not include traded products
            
        for docType in docTypes:
            filePath = 'C:\\Users\\Stephen\\Desktop\\' + region + '\\' + docType + '\\'

        for filename in os.listdir(filePath):
            files.append(filename)
            #Rename these files so that they are compatible with the template editor regression store
            if region == 'US'
                files2.append(filename.replace("Sc9", "Sc09").replace("SEC_Shelf_", "").replace("Sc", "SEC_Shelf_Sc_").replace("_", " ").split('.')[0])
            else:
                if docType == 'indicative':
                    files2.append(filename.replace("_" + docType, "").replace("GSSP_OC_", "").replace("Sc", "GSSP_OC_" + docType + "_TS_EN_Sc_").replace("_", " ").split('.')[0])
                else:
                    files2.append(filename.replace("_" + docType, "").replace("GSSP_OC_", "").replace("Sc", "GSSP_OC_" + docType + "_TS_EN_Sc_").replace("_", " ").split('.')[0])
                    files2.append(filename.replace("_" + docType, "").replace("GSSP_OC_", "").replace("Sc", "GSSP_OC_PS_EN_Sc_").replace("_", " ").split('.')[0])
        
        files2.sort(reverse = False) # Sort these in ascending order

        #Execute api calls to upload these xmls to the product
        for file in files:
            idx = files.index(file)
            tree = ET.parse('C:\\Users\\Stephen\\Desktop\\changed-' + docType + '\\' + file)
            root = tree.getroot()
            fileNameXMLToStr = ET.tostring(root, encoding='utf8', method='xml')
            headersForPostRequest = {'Content-type':'application/xml', 'Authorization' : 'Bearer ' + token}

            urlForPostRequest = endpoint + files2[idx] + params
            respPost = requests.post(url = urlForPostRequest, headers = headersForPostRequest, data = fileNameXMLToStr, verify=False)

#---
# only use this line to run the script, and state what your intended operation is
#
operation('Both') #Use any of the 3 following strings 'US', 'GSSP', 'Both' depending on the folders sent yby client
