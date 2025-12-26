from sklearn.datasets import fetch_california_housing
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = fetch_california_housing()
dataset = pd.DataFrame(df.data)
dataset.columns = df.feature_names
dataset['Price'] = df.target
print(dataset.head(3))

X = dataset.iloc[:, :-1]
y = dataset.iloc[:, :-1]

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

lin_reg = LinearRegression()
mse = cross_val_score(lin_reg, X, y, scoring='neg_mean_squared_error', cv=5)

mean_mse = np.mean(mse)

# Ridge Regression
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

ridge = Ridge()

params = {'alpha': [1e-15, 1e-10, 1e-8, 1e-3, 1e-2, 1, 5, 10, 20, 30, 35, 40, 45, 50]}

ridge_regressor = GridSearchCV(ridge, params, scoring='neg_mean_squared_error', cv=5)
ridge_regressor.fit(X, y)

print(ridge_regressor.best_params_)
print(ridge_regressor.best_score_)

# Lasso Regression
from sklearn.linear_model import Lasso
from sklearn.model_selection import GridSearchCV

lasso = Lasso()

lasso_regressor = GridSearchCV(ridge, params, scoring='neg_mean_squared_error', cv=5)
lasso_regressor.fit(X, y)

print(lasso_regressor.best_params_)
print(lasso_regressor.best_score_)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

from sklearn.metrics import r2_score
lasso_y_pred = lasso_regressor.predict(X_test)
lasso_r2_score = r2_score(lasso_y_pred,y_test)
print(lasso_r2_score)

#Logistic Regression
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression

df = load_breast_cancer()
X = pd.DataFrame(df['data'],columns=df['feature_names'])
y = pd.DataFrame(df['target'],columns=['target'])

print(y['target'].value_counts())

params = [{'C': [1,5,10]},{'max_iter': [100,150]}]
models1 = LogisticRegression(C=100,max_iter=100)
model = GridSearchCV(models1,param_grid=params,scoring='f1',cv=5)
model.fit(X_train,y_train)

print("%"*100)
print(model.best_params_)
print(model.best_score_)
y_pred = model.predict(X_test)
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score

print(confusion_matrix(y_test,y_pred))
print(accuracy_score(y_test,y_pred))

print(classification_report(y_test,y_pred))
