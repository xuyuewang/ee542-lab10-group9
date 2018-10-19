import pandas as pd 
import hashlib
import os 
from utils import logger

def extractLabel(inputfile,inputcase):
	df = pd.read_csv(inputfile, sep="\t")
	dc = pd.read_csv(inputcase, sep="\t")
	#
	#print (df)
	
	df['label'] = df['cases.0.samples.0.sample_type']
	dc['disease'] = dc ['disease_type']
	dc['primary'] = dc['primary_site']

	print (df['label'][0:4])
	print (dc['disease'][0:4])

	sample_type = 1
	disease_type = 1
	primary_site = 1
	normal_count = 0
	tumor_count = 0
	
	sample_list = ['Primary Tumor']
	disease_list = ['Ductal and Lobular Neoplasms']
	primary_list = ['Breast']
	
	for y in range(11486):
		if df['label'][y] not in sample_list:
			print ('add one more type')
			sample_list.append(df['label'][y])
			sample_type = sample_type + 1

	for z in range(10601):
		if dc['disease'][z] not in disease_list:
			disease_list.append(dc['disease'][z])
			disease_type = disease_type + 1
		if dc['primary'][z] not in primary_list:
			primary_list.append(dc['primary'][z])
			primary_site = primary_site + 1
	
	
	print (sample_list)
	
	print (primary_list)
	print (disease_list)
	
print 
	
	'''
	for x in range(425):
		if 'Normal' in df['label'][x]:
			normal_count = normal_count + 1
		if 'Tumor' in df['label'][x]:
			tumor_count = tumor_count + 1
	
	print (normal_count)
	print (tumor_count)

	
	df.loc[df['cases.0.samples.0.sample_type'].str.contains("Normal"), 'label'] = 0
	df.loc[df['cases.0.samples.0.sample_type'].str.contains("Tumor"), 'label'] = 1
	tumor_count = df.loc[df.label == 1].shape[0]
	normal_count = df.loc[df.label == 0].shape[0]
	logger.info("{} Normal samples, {} Tumor samples ".format(normal_count,tumor_count))
	columns = ['file_id','label']
	'''
	return 1


if __name__ == '__main__':


	data_dir ="/home/amber/Documents/ee542-lab10-group9/data/"
	# Input directory and label file. The directory that holds the data. Modify this when use.
	#dirname = data_dir + "live_miRNA"
	label_file = data_dir + "files_meta.tsv"
	label_case = data_dir + "cases_meta.tsv"
	
	#output file
	#outputfile = data_dir + "miRNA_matrix.csv"

	# extract data
	#matrix_df = extractMatrix(dirname)
	label_df = extractLabel(label_file,label_case)

	#merge the two based on the file_id
	#result = pd.merge(matrix_df, label_df, on='file_id', how="left")
	#print(result)

	#save data
	#result.to_csv(outputfile, index=False)
	#print (labeldf)
