# TUGAS 03 PEMODELAN DAN PEMBELAJARAN MESIN
# NAMA   : RENDY CHRISTIAN
# NPM    : 2006529695
# IMPLEMENTASI CLUSTERING DENGAN METODE DECISION TREE PADA DATASET "dataDiabetesTugas.csv"

# import library 
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split 
from sklearn import preprocessing, metrics, tree

# import dataset
df = pd.read_csv ('C:/Users/OSMOND/Documents/Python/dataDiabetesTugas.csv', sep = ';') # read dataset (separate ; (csv))
df.drop(['No. Sample'], axis = 1, inplace = True)       # menghapus/drop kolom "no.sample"

# melakukan label encoder pada kolom class untuk mengubah nilai dari text menjadi numerical (binary)
label_encoder = preprocessing.LabelEncoder()
df['class'] = label_encoder.fit_transform(df['class'])
df['class'].unique()

# men-display dataset
print(tabulate(df, headers = 'keys', tablefmt = 'psql'))

#Mengatur features dan target variabel
independentVar = ['preg', 'plas', 'pres', 'skin','insu','mass','pedi']
X = df[independentVar].values   # Variabel independent
y = df['class'].values          # Variable dependent (target)

# Membagi data ke dalam data training dan test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) 
# >>>>>>>> 70% training and 30% test <<<<<<<<<<<

# Implementasi decision tree classification
print("Metode yang digunakan : Decision-Tree Classification\n")
clf = DecisionTreeClassifier(criterion="entropy", splitter = "best", max_depth=None)  # membuat objek classifier decision tree
clf = clf.fit(X_train,y_train)                                  # melakukan train pada classifier decision tree
y_pred = clf.predict(X_test)                                    # prediksi response untuk melakukan test dataset
print("Akurasi :",metrics.accuracy_score(y_test, y_pred))       # Persentase akurasi model decision tree
print("\n")

# visualisasi decision tree dengan meggunakan plot_tree
fig = plt.figure(figsize=(25,25))                               # menentukan ukuran gambar/figure
_ = tree.plot_tree(clf,  filled=True,
                feature_names = independentVar,
                class_names=['0','1'])                          # plotting decision tree
fig.savefig("diabetes_decisionTree.png")                        # figure akan disimpan di local memory 
