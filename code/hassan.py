import pandas as pd
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
X_hr = pd.read_csv(r'C:\Users\user\Desktop\final\Hassan.csv')
print(X_hr)
X_finite = X_hr[np.isfinite(X_hr["X1"])]
X_finite = X_finite[np.isfinite(X_finite["X2"])]
X_finite = X_finite[np.isfinite(X_finite["X3"])]
X_finite = X_finite[np.isfinite(X_finite["X4"])]
Xn = X_finite
y = Xn["Y"]
X = Xn[["X1", "X2", "X3", "X4"]]
plt.figure(figsize=(9, 5))
plt.hist(y, bins=30)
plt.xlabel('Production Value',fontsize=15)
plt.ylabel('Occurences',fontsize=15)
plt.title('Distribution of the Rice Production Values',fontsize=18)
plt.grid(True)
Xplot = Xn[["X1", "X2", "X3", "X4","Y"]]
var_name = "X1"
plt.figure(figsize=(10,6))
sns.regplot(x=var_name, y='Y', data=Xplot, scatter_kws={'alpha':0.6, 's':20})
plt.xlabel(var_name + " (Crop Produce of Last Year)", fontsize=15)
plt.ylabel('Y', fontsize=15)
plt.title("Distribution of y variable with feature "+var_name, fontsize=18)
# Z-Score Normalization
cols = list(X.columns)

for col in cols:
    col_zscore = col + '_zscore'
    X[col_zscore] = (X[col] - X[col].mean())/X[col].std(ddof=0)
X = X[["X1_zscore", "X2_zscore", "X3_zscore", "X4_zscore"]]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
alg = LinearRegression()
alg.fit(X_train, y_train)
filename = 'hassan.pkl'  #name the file 
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
scores = cross_val_score(clf, X, y, cv=5, scoring='neg_mean_squared_error')
for i in range(0,5):
    scores[i] = sqrt(-1*scores[i])
print(scores)
avg_rmse = scores.mean()
print("\n\nAvg RMSE is ",scores.mean())
# print(type(y_test))
# print(type(y_predict))
yt = y_test.as_matrix()
print(type(yt))
p=pd.DataFrame()
p["y_predicted"] = y_predict/1000
p["y_test"] = yt/1000
p["y_predicted"] = p["y_predicted"].round(decimals=1)
# p["y_test"] = p["y_test"].round(decimals=1)
print(p.describe())
print(p)
