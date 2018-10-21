# To generate matrix which includes both file info and case info correspondingly.
import pandas as pd 
import hashlib
import os 
from utils import logger


def extractfile(inputfile):
	df = pd.read_csv(inputfile, sep="\t")
	df['sample'] = df['cases.0.samples.0.sample_type']
	df['case_id'] = df['cases.0.case_id']
	columns = ['case_id','sample','file_id']
	return df[columns]
	
	

def extractcase(inputfile):
	dc = pd.read_csv(inputfile, sep="\t")
	dc['case_id'] = dc['id']
	dc['disease'] = dc['disease_type']
	dc['primary'] = dc['primary_site']
	columns = ['case_id','disease','primary']
	return dc[columns]



if __name__ == '__main__':


	data_dir ="/home/amber/Documents/ee542-lab10-group9/data/"
	# Input directory and label file. The directory that holds the data. Modify this when use.
	#dirname = data_dir + "live_miRNA"
	label_file = data_dir + "files_meta.tsv"
	label_case = data_dir + "cases_meta.tsv"
	
	#output file
	outputfile = data_dir + "label_matrix.csv"

	# extract data
	case_df = extractfile(label_file)
	file_df = extractcase(label_case)

	#merge the two based on the file_id
	result = pd.merge(file_df, case_df, on='case_id', how="left")
	#print(result)

	#save data
	result.to_csv(outputfile, index=False)
	#print (labeldf)
