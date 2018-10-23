import numpy as np
import matplotlib.pyplot as plt
from itertools import product
from sklearn.decomposition import PCA
from sklearn.datasets import fetch_mldata
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import StandardScaler

#use all digits

mytargets = list(range(0,54))

data_dir ="/home/amber/Documents/lab10/"
data_file = data_dir + "miRNA_matrix_v1.csv"

df = pd.read_csv(data_file)
# print(df)
y_data = df.pop('label_primary').values

df.pop('file_id')
columns =df.columns
#print (columns)
X_data = df.values
# split the data to train and test set
X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.4, random_state=42)

#standardize the data.
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)

num_samples_to_plot = 10000
X_train, y_train = shuffle(X_train, y_train)
X_train, y_train = X_train[:num_samples_to_plot], y_train[:num_samples_to_plot]  # lets subsample a bit for a first impression


for digit in mytargets:
  instances=[i for i in y_train if i==digit]
  print "Digit",digit,"appears ",len(instances), "times"

pca = PCA(n_components=2)
fig, plot = plt.subplots()
fig.set_size_inches(50, 50)
plt.prism()

X_transformed = pca.fit_transform(X_train)

print (pca.explained_variance_ratio_)
print (y_train)
plot.scatter(X_transformed[:, 0], X_transformed[:, 1], c=y_train)
plot.set_xticks(())
plot.set_yticks(())

count=0;

plt.tight_layout()
plt.suptitle("PCA for GDC data ")

for label , x, y in zip(y_train, X_transformed[:, 0], X_transformed[:, 1]):
#Lets annotate every 1 out of 200 samples, otherwise graph will be cluttered with anotations
  if count % 200 == 0:
    plt.annotate(str(int(label)),xy=(x,y), color='black', weight='normal',size=10,bbox=dict(boxstyle="round4,pad=.5", fc="0.8"))
  count = count + 1

#plt.savefig("mnist_pca.png")
plt.show()
