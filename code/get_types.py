# to get info for sample types, primary sites, and disease types.
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

	#print (df['label'][0:4])
	#print (dc['disease'][0:4])

	sample_type = 1
	disease_type = 1
	primary_site = 1
	
	sample_list = ['Primary Tumor']
	disease_list = ['Ductal and Lobular Neoplasms']
	primary_list = ['Breast']
	
	for y in range(11486):
		if df['label'][y] not in sample_list:
			# print ('add one more type')
			sample_list.append(df['label'][y])
			sample_type = sample_type + 1

	for z in range(10601):
		if dc['disease'][z] not in disease_list:
			disease_list.append(dc['disease'][z])
			disease_type = disease_type + 1
		if dc['primary'][z] not in primary_list:
			primary_list.append(dc['primary'][z])
			primary_site = primary_site + 1
	
	print ("sample_type_number=",sample_type, "\ndisease_type_number=", disease_type, "\nprimary_site_number=", primary_site)
	
	print ("\nsample_type: ",sample_list)
	print ("\ndisease_type: ",disease_list)
	print ("\nprimary_site: ",primary_list)
	


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
	extractLabel(label_file,label_case)

