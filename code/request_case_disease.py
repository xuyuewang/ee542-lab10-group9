import requests
import json
import pandas as pd
import os

def retrieveCaseMeta(file_ids,outputfile):
    '''

    Get the tsv metadata for the list of case_ids
    Args:
        file_ids: numpy array of file_ids
        outputfile: the output filename

    '''

    fd = open(outputfile,'w')
    cases_endpt = 'https://api.gdc.cancer.gov/cases'


    filters = {
        "op":"in",
        "content":{
            "field":"cases.case_id",
            "value": file_ids.tolist()
        }
    }

    '''
    fields = [
        "case.case_id"
    ]

    '''
    # print (filters)
    #expand group is diagnosis and demoragphic
    params = {
        "filters" : filters,
        #"expand" : "diagnoses,demographic,exposures",
	"fields" : "primary_site",
        "format": "TSV",
        "pretty": "true",
        "size": 12000
    }
    # print (params)
    #print (filters)
    #print (fields)
    
    
    response = requests.post(cases_endpt, headers = {"Content-Type": "application/json"},json = params)
    # print (response.content.decode("utf-8"))
    fd.write(response.content.decode("utf-8"))
    fd.close()

if __name__ == '__main__':

    data_dir = "/home/amber/Documents/ee542-lab10-group9/data/"
    filename = data_dir+"file_case_id_DNA.csv"
    
    
    df = pd.read_csv(filename)
    case_ids = df.case_id.values
    # print(case_ids)
    
    caseids_meta_outfile = data_dir + "cases_meta_disease.tsv"
    # python request method
    retrieveCaseMeta(case_ids,caseids_meta_outfile)
    
    

