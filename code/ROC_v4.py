print(__doc__)

import pandas as pd 
import hashlib
import os 

import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle

from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from scipy import interp

data_dir ="/home/jon/Lab10/"

data_file = data_dir + "miRNA_matrix_multi_v2.csv"

df = pd.read_csv(data_file)
# print(df)
y_data = df.pop('label_primary').values
for i in range(len(y_data)):
	if y_data[i] != 0:
		y_data[i] = 1

print(y_data)
df.pop('file_id')

columns =df.columns
#print (columns)
X_data = df.values

# split the data to train and test set
X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.3, train_size=0.07, random_state=0)
print('1')

print(X_train)
print('1')
print(y_train)
print(len(X_train))
print(len(y_train))

print(X_test)
print(len(X_test))

# Learn to predict each class against the other
classifier = OneVsRestClassifier(svm.SVC(kernel='linear', probability=True,
                                 random_state=0))
y_score = classifier.fit(X_train, y_train).decision_function(X_test)

print('2')
# Compute ROC curve and ROC area for each class
fpr = dict()
tpr = dict()
roc_auc = dict()

fpr, tpr, _ = roc_curve(y_test, y_score)
roc_auc = auc(fpr, tpr)

plt.figure()
lw = 2
plt.plot(fpr, tpr, color='darkorange',
         lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic Figure')
plt.legend(loc="lower right")
plt.show()
