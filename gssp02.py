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
		headersForPostRequest = {'Content-type':'application/xml', 'Authorization' : 'Bearer uLRPWrjMDNWzSOeo4jMGbL3H2zcA8fyhkiElDBWefHiN5FaCCoqfF8OeoENci3nC1Y8TdNjiCIcXWKehwYhWbPH2eeDwKlmOJFXHb35G6CNMLyhSIMDWk3U5YTKv0ZXBUxCtnQ3FKjT5QtLJ0XzGeQLzzAMl3hATjDuzcbbIJCrIPc1bSjeCTxWpw3KHEWByEklEqTC0Zl8EgzHqWFUNA6LNeYRx2KMW1FszeEKuCmAnk1B2yzYmf6haKBMEGv5s'}

		urlForPostRequest = 'https://uat-store-api.priipcloud.com/product-store/api/product/' + files2[idx] + '/org/17'
		respPost = requests.post(url = urlForPostRequest, headers = headersForPostRequest, data = fileNameXMLToStr, verify=False)
