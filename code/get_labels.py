# based on sample type and primary site, give all cancer types with labels 0-54.
import pandas as pd 
import hashlib
import os 
import numpy as np
from utils import logger
def file_as_bytes(file):
    with file:
        return file.read()



def extractLabel(inputfile,outputfile1,outputfile2):
	df = pd.read_csv(inputfile, sep=",")
	
	primary_site = ['Breast', 'Bronchus and lung', 'Larynx', 'Retroperitoneum and peritoneum', 'Uterus, NOS', 'Connective, subcutaneous and other soft tissues', 'Kidney', 'Cervix uteri', 'Hematopoietic and reticuloendothelial systems', 'Other and unspecified parts of tongue', 'Bladder', 'Liver and intrahepatic bile ducts', 'Skin', 'Colon', 'Rectosigmoid junction', 'Corpus uteri', 'Stomach', 'Prostate gland', 'Ovary', 'Thymus', 'Heart, mediastinum, and pleura', 'Eye and adnexa', 'Lymph nodes', 'Adrenal gland', 'Other and unspecified parts of biliary tract', 'Gallbladder', 'Rectum', 'Esophagus', 'Pancreas', 'Blood', 'Brain', 'Other and ill-defined sites in lip, oral cavity and pharynx', 'Gum', 'Floor of mouth', 'Tonsil', 'Other and unspecified parts of mouth', 'Base of tongue', 'Oropharynx', 'Hypopharynx', 'Palate', 'Thyroid gland', 'Testis', 'Peripheral nerves and autonomic nervous system', 'Lip', 'Bones, joints and articular cartilage of other and unspecified sites', 'Other endocrine glands and related structures', 'Other and ill-defined sites', 'Bones, joints and articular cartilage of limbs', 'Other and unspecified major salivary glands', 'Unknown primary site', 'Small intestine', 'Meninges', 'Other and unspecified male genital organs', 'Spinal cord, cranial nerves, and other parts of central nervous system']

	sample_type = ['Primary Tumor', 'Solid Tissue Normal', 'Primary Blood Derived Cancer - Peripheral Blood', 'Metastatic', 'Recurrent Tumor', 'Primary Blood Derived Cancer - Bone Marrow', 'Recurrent Blood Derived Cancer - Bone Marrow', 'Recurrent Blood Derived Cancer - Peripheral Blood', 'Additional - New Primary', 'Cell Lines', 'Control Analyte', 'Additional Metastatic']
	
	#print (primary_site[0:10])
	print (df['sample'][0:10])
	print (df['primary'][0:10])
	labell = [];
	labelll = [];
	
	for x in range(11486):
		if 'Tumor' in df['sample'][x]:
			string = df['primary'][x]
			#print (string)
			for y in range(54):
				pstring = primary_site[y]
				if string == pstring:
					labell.append(y+1)
					break
				else:
					if y == 53:
						labell.append(55)
		else:
			labell.append(0)
	
	for x in range(11486):
		for z in range(12):
			if df['sample'][x] == sample_type[z]:
				labelll.append(z)
				break

	np_data1 = np.array(labell)
	pd_data1 = pd.DataFrame(np_data1,columns=['label_primary'])
	pd_data1.to_csv(outputfile1)
	
	np_data2 = np.array(labelll)
	pd_data2 = pd.DataFrame(np_data2,columns=['label_sample'])
	pd_data2.to_csv(outputfile2)
	
	print (df['file_id'][0:10],pd_data1['label_primary'][0:10],pd_data2['label_sample'][0:10])
	
	#dl = pd.read_csv(outputfile)
	#result = pd.merge(df['file_id'],pd_data['label'],how="left")
	#print (result[0:10])
	
	return 1

	

if __name__ == '__main__':


	data_dir ="/home/amber/Documents/ee542-lab10-group9/data/"
	# Input directory and label file. The directory that holds the data. Modify this when use.
	#dirname = data_dir + "miRNA"
	label_file = data_dir + "label_matrix.csv"
	
	#output file
	outputfile1 = data_dir + "label_primary.csv"
	outputfile2 = data_dir + "label_sample.csv"

	# extract data
	#matrix_df = extractMatrix(dirname)
	label_df = extractLabel(label_file,outputfile1,outputfile2)

	# label summary
	#outputlabel(label_file,outputfile1,outputfile2,outputfile)

	#merge the two based on the file_id
	#result = pd.merge(matrix_df, label_df, on='file_id', how="left")
	#print(result)

	#save data
	#result.to_csv(outputfile, index=False)
	#print (labeldf)

 




