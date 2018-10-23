import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import hashlib
import os 


from sklearn.datasets import fetch_mldata
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from ggplot import *

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

df.pop('file_id')

columns =df.columns
#print (columns)
X_data = df.values

X = X_data
y = y_data

#print (X.shape, y.shape)


feat_cols = [ 'pixel'+str(i) for i in range(X.shape[1]) ]

df = pd.DataFrame(X,columns=feat_cols)
df['label'] = y
df['label'] = df['label'].apply(lambda i: str(i))

X, y = None, None

#print ('Size of the dataframe: {}'.format(df.shape))

rndperm = np.random.permutation(df.shape[0])

# pca = PCA(n_components=3)
# pca_result = pca.fit_transform(df[feat_cols].values)

# df['pca-one'] = pca_result[:,0]
# df['pca-two'] = pca_result[:,1] 
# df['pca-three'] = pca_result[:,2]

# #print ('Explained variation per principal component: {}'.format(pca.explained_variance_ratio_))



# chart = ggplot( df.loc[rndperm[:3000],:], aes(x='pca-one', y='pca-two', color='label') ) \
#         + geom_point(size=75,alpha=0.8) \
#         + ggtitle("First and Second Principal Components colored by digit")

# print(chart)
n_sne = 7000

time_start = time.time()
tsne = TSNE(n_components=2, verbose=1, perplexity=40, n_iter=300)
tsne_results = tsne.fit_transform(df.loc[rndperm[:n_sne],feat_cols].values)

print ('t-SNE done! Time elapsed: {} seconds'.format(time.time()-time_start))

df_tsne = df.loc[rndperm[:n_sne],:].copy()
df_tsne['x-tsne'] = tsne_results[:,0]
df_tsne['y-tsne'] = tsne_results[:,1]

chart = ggplot( df_tsne, aes(x='x-tsne', y='y-tsne', color='label') ) \
        + geom_point(size=70,alpha=0.1) \
        + ggtitle("tSNE dimensions colored by digit")
print(chart)