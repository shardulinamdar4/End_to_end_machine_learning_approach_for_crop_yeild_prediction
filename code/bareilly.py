import pandas as pd							#Importing the required liabraries
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt
import pprint
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import cross_val_score
from sklearn import metrics
import pickle

X_hr = pd.read_csv(r'C:\Users\user\Desktop\final\bareilly.csv')#Importing the dataset.(NOTE:You need to input your own file location here)
print(X_hr)							#Printing the dataset for you to have a look at it	
X_finite = X_hr[np.isfinite(X_hr["X1"])]			#In the following lines,the care of missing data is taken
X_finite = X_finite[np.isfinite(X_finite["X2"])]
X_finite = X_finite[np.isfinite(X_finite["X3"])]
X_finite = X_finite[np.isfinite(X_finite["X4"])]
Xn = X_finite
y = Xn["Y"]
X = Xn[["X1", "X2", "X3", "X4"]]
plt.figure(figsize=(9, 5))					#Plotting the graph of production values vs occurences
plt.hist(y, bins=30)
plt.xlabel('Production Value',fontsize=15)
plt.ylabel('Occurences',fontsize=15)
plt.title('Distribution of the Rice Production Values',fontsize=18)
plt.grid(True)
plt.show()
Xplot = Xn[["X1", "X2", "X3", "X4","Y"]]
var_name = "X1"
plt.figure(figsize=(10,6))					#Plotting the graph of production values vs rainfall
sns.regplot(x=var_name, y='Y', data=Xplot, scatter_kws={'alpha':0.6, 's':20})
plt.xlabel(var_name + " (Crop Produce of Last Year)", fontsize=15)
plt.ylabel('Y', fontsize=15)
plt.title("Distribution of y variable with feature "+var_name, fontsize=18)
plt.show()
# Z-Score Normalization
cols = list(X.columns)

for col in cols:
    col_zscore = col + '_zscore'
    X[col_zscore] = (X[col] - X[col].mean())/X[col].std(ddof=0)
X = X[["X1_zscore", "X2_zscore", "X3_zscore", "X4_zscore"]]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)   #Splitting the data into training and testing sets
alg = LinearRegression()
alg.fit(X_train, y_train)
filename = 'bareilly.pkl'  #name the file 
pickle.dump(alg, open(filename, 'wb'))  # dump into pickle mode
coef = alg.coef_
coef = coef.round(decimals=2)
np.set_printoptions(suppress=True) #gem 
print("The coefficients for the linear regression model learnt are\n")
print(coef)
print()
y_predict = alg.predict(X_test)
rmse = sqrt(mean_squared_error(y_predict, y_test))
print(rmse)
clf = LinearRegression()
scores = cross_val_score(clf, X, y, cv=5, scoring='neg_mean_squared_error')  	#Finding mean squared errors
for i in range(0,5):
    scores[i] = sqrt(-1*scores[i])
print(scores)
avg_rmse = scores.mean()
print("\n\nAvg RMSE is ",scores.mean())
yt = y_test.as_matrix()
print(type(yt))
p=pd.DataFrame()
p["y_predicted"] = y_predict/1000
p["y_test"] = yt/1000
p["y_predicted"] = p["y_predicted"].round(decimals=1)
# p["y_test"] = p["y_test"].round(decimals=1)
print(p.describe())
print(p)
