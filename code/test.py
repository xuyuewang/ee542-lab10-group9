import pandas as pd
import os


if __name__ == '__main__':

    data_dir = "/home/amber/Documents/ee542-lab10-group9/data/"
    filename = data_dir+"file_case_id_DNA.csv"
    
    
    df = pd.read_csv(filename)
    file_ids = df.file_id.values
    case_ids = df.case_id.values

    print(case_ids)
