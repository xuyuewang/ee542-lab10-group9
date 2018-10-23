This is the git repo for ee542-lab10 by group 9.

Team members: 
Jinhyun: So jinhyuns@usc.edu;
Xuyue Wang: xuyuewan@usc.edu;
Yizhuo Wang: yizhuow@usc.edu.

Folder /data includes all data for this lab:
1. /miRNA includes 11486 samples of all cancer types from GDC.
2. Files generated when downloading the data: gdc_manifest.2018-10-18.txt, cases_meta.csv, file_meta.csv, files.2018-101-8.json, file_case_id_DNA.csv.
3. label_info.txt showns all categories in sample types, disease types, and primary sites.
4. Files generated when assigning the labels and get miRNA matrix: cases_meta_disease.tsv, file_label.csv, label_matrix.csv, label_primary.csv, label_sample.csv.

Folder /code includes all source code for this lab:
1. Check if all files are downloaded successfully by check.py.
2. Download the case IDs for the files by parse_file_case_id.py.
3. Get meta data for the files and corresponding cases by request_meta.py.
4. Get all categories of these data by get_types.py.
5. Generate the matrix when file_id, case_id, primary sites, sample types, and disease types by gen_label_matrix.py to have a better observation of these data before labelling.
6. Assign labels to the file based on sample types and primary sites by get_labels.py. It can be combined in the process when generating miRNA matrix.
7. Generate miRNA matrix by gen_miRNA_matrix.py.
8. Do a multiclassification and get the prediction result by predict_multiclass.py.
9. Visualize the features after feature selection by PCA and tSNE method. PCA.py and test_feature.py for PCA method. tSNE.py and test_feature2.py for tSNE method. (Note that here, PCA.py and tSNE.py use ggplot to plot the features while ggplot has compatibility issue with high version pandas. Code test_feature.py and test_feature2.py are substituted under such condition.)
10. Plot ROC curve for the model by ROC_v4.py.

To run these code, use command "python3 xxx.py" or "python xxx.py".
Install the modules which does not exist in your system use command "pip3 install xxx" or "pip install xxx".
