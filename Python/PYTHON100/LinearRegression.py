from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np
import pandas as pd
import joblib


X = np.array([[1], [2], [3], [4], [5]])
Y = np.array([2, 4, 6, 8, 10]) 
J= np.array([[10], [12], [14], [16], [20]])
K = np.array([20, 24, 28, 32, 40]) 

model = LinearRegression()
model.fit(X,Y)
joblib.dump(model, "SavedModel.pkl")

print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)

y_pred = model.predict(J)

print("R² Score:", r2_score(K, y_pred))
print("MSE:", mean_squared_error(K, y_pred))
