import xml.etree.ElementTree as ET
import requests
import os
import array
import time

docTypes = ['indicative','final']

for docType in docTypes:
	files = []
	files2 = []

	filePath = 'C:\\Users\\Stephen\\Desktop\\changed-' + docType + '\\'

	for filename in os.listdir(filePath):
		files.append(filename)
		if docType == 'indicative':
			files2.append(filename.replace("_" + docType, "").replace("GSSP_OC_", "").replace("Sc", "GSSP_OC_" + docType + "_TS_EN_Sc_").replace("_", " ").split('.')[0])
		else:
			files2.append(filename.replace("_" + docType, "").replace("GSSP_OC_", "").replace("Sc", "GSSP_OC_" + docType + "_TS_EN_Sc_").replace("_", " ").split('.')[0])
			files2.append(filename.replace("_" + docType, "").replace("GSSP_OC_", "").replace("Sc", "GSSP_OC_PS_EN_Sc_").replace("_", " ").split('.')[0])
		
	files2.sort(reverse = False)
    
	for file in files:
		idx = files.index(file)
		tree = ET.parse('C:\\Users\\Stephen\\Desktop\\changed-' + docType + '\\' + file)
		root = tree.getroot()
		fileNameXMLToStr = ET.tostring(root, encoding='utf8', method='xml')
		headersForPostRequest = {'Content-type':'application/xml', 'Authorization' : 'Bearer [token scrubbed]'}

		urlForPostRequest = '[endpoint scrubbed]' + files2[idx] + '[params scrubbed]'
		respPost = requests.post(url = urlForPostRequest, headers = headersForPostRequest, data = fileNameXMLToStr, verify=False)
