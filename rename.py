import array
import time
from os import path

docTypes = ['indicative','final']

for docType in docTypes:
	files = []
	files2 = []

	filePath = 'C:\\Users\\Stephen\\Desktop\\changed-' + docType + '\\'

	for filename in os.listdir(filePath):
		# files.append(filename.split('.')[0])
		# if docType == 'indicative':
			src = path.realpath(filename);
			newname = filename.replace("_" + docType, "").replace("GSSP_OC_", "").replace("Sc", "GSSP_OC_" + docType + "_TS_EN_Sc_0").replace("_", " ")
			os.rename('C:\\Users\\Stephen\\Desktop\\changed-' + docType + '\\' + filename,'C:\\Users\\Stephen\\Desktop\\changed-' + docType + '\\' + newname)
		# else:
			# files2.append(filename.replace("_" + docType, "").replace("GSSP_OC_", "").replace("Sc", "GSSP_OC_" + docType + "_TS_EN_Sc_").replace("_", " ").split('.')[0])
			# files2.append(filename.replace("_" + docType, "").replace("GSSP_OC_", "").replace("Sc", "GSSP_OC_PS_EN_Sc_").replace("_", " ").split('.')[0])
