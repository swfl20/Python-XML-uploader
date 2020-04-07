import xml.etree.ElementTree as ET
import requests
import os
import array
import time

docTypes = ['indicative','traded','final']

for docType in docTypes:
	files = []
	files2 = []

	filePath = 'C:\\Users\\Stephen\\Desktop\\changed-' + docType + '\\'

	for filename in os.listdir(filePath):
		files.append(filename)
		if docType == 'final' or docType == 'indicative':
			files2.append(filename.replace("_" + docType + "_TS_EN", "").replace("GSSP_OC_", "").replace("Sc", "GSSP_OC_" + docType + "_TS_EN_Sc_").replace("_", " ").split('.')[0])
		else:
			files2.append(filename.replace("_PS_EN", "").replace("GSSP_OC_", "").replace("Sc", "GSSP_OC_PS_EN_Sc_").replace("_", " ").split('.')[0])
		
	files2.sort(reverse = False)
    
	for file in files:
		idx = files.index(file)
		tree = ET.parse('C:\\Users\\Stephen\\Desktop\\changed-' + docType + '\\' + file)
		root = tree.getroot()
		fileNameXMLToStr = ET.tostring(root, encoding='utf8', method='xml')
		headersForPostRequest = {'Content-type':'application/xml', 'Authorization' : 'Bearer kA80QouKDIrkvoUWGhZGGlaEYer0imgCUBlCfGQ3Rx5ZNe8e6P1AHmzAoTRZUz6QlYEUMeEQzHhVIuycPJqDCRwaznu5SpdWgGTRpqWoDouJbpoQYnlW165JFt2fEzXU2wsxi4DTnOdEYV5jyKIkeuIdNp6YCzBDCP2qnnFyBZRir6Rg2TLqE5jcGfjJRPzfq6edGXRdYUPFIMJR1sYBlwjSXlZHN7G6GJJwAbc3nW5Xk7CtF3IkbAm7J7sPs0h7'}

		urlForPostRequest = 'https://uat-store-api.priipcloud.com/product-store/api/product/' + files2[idx] + '/org/17'
		respPost = requests.post(url = urlForPostRequest, headers = headersForPostRequest, data = fileNameXMLToStr, verify=False)
