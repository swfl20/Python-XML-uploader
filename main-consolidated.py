import xml.etree.ElementTree as ET
import requests
import shutil, os
import array

# obtain via WSD
endpoint = '[endpoint scrubbed]'
token = '[token scrubbed]'
params = '[params scrubbed]'

#---
# Function which handles all the logic in relation to how the client sends us information
# 
def operation(toUpload, operation):
    
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
                #---
                # slightly complicated logic is needed for gssp to get the naming convention right:
                #   -Indicatives XML generates indicative term-sheets
                #   -Final XMLs generates all pricing supplements AND final term-sheets
                
                scString = filename.split('_')[0]
                scenarioNo = scString.split('Sc')[1]
                
                TSprefix = "GSSP_OC_" + docType + "_TS_EN_Sc_"
                PSprefix = "GSSP_OC_PS_EN_Sc_"
                
                if int(scenarioNo) < 10:
                    TSprefix = TSprefix + "0"
                    PSprefix = PSprefix + "0"
                
                if operation == 'Full':                
                    #This is for the indicative and final term-sheets
                    files2.append(filename.replace("_" + docType, "").replace("GSSP_OC_", "").replace("Sc", TSprefix).replace("_", " ").split('.')[0])
                    
                    #extra operation for the pricing supplements
                    if docType == 'final':
                        files2.append(filename.replace("_" + docType, "").replace("GSSP_OC_", "").replace("Sc", PSprefix).replace("_", " ").split('.')[0])
                else:
                    #This will only rename the files
                    currDir = os.getcwd() 
                    parDir = os.path.dirname(currDir)
                        
                    #This is for the indicative and final term-sheets
                    newTSname = filename.replace("_" + docType, "").replace("GSSP_OC_", "").replace("Sc", TSprefix).replace("_", " ")
                    os.rename(parDir + '\\' + region + '\\' + docType + '\\' + filename, parDir + '\\' + region + '\\' + docType + '\\' + newTSname)
                    
                    if docType == 'final':
                        newPSname = filename.replace("_" + docType, "").replace("GSSP_OC_", "").replace("Sc", PSprefix).replace("_", " ")
                        shutil.copytree(parDir + '\\' + region + '\\' + docType + '\\', parDir + '\\PS') # create a copy of these XML into a new directory for the PS
                        os.rename(parDir + '\\PS\\' + filename, parDir + '\\PS\\' + newPSname)
                
                #---
                # Your files are now ready to Batch-Upload in tradeforms/webapp
                # TODO: utf-8 encoding
                #---
                        
        # run this next section if it's the full operation
        if operation == 'Full':
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
# Use this line to run the script, and state what your intended operation is
#   -Param 1: region that you would like to run the script on, permitted values are:
#       - 'US', 'GSSP', 'Both'
#   -Param 2: State the operation, whether you want to simply rename the files, or execute full upload operation, accepted values are:
#       - 'Rename', 'Full'

operation('Both', 'Full') 
