import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api  as sm
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

np.random.seed(2)

x = np.random.uniform(0,10,200)
y = 2 * x ** 2 - 5 * x + 3 + np.random.normal(0,10,200)

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

inputValuesTrain = {
    'x': x[:80],
    'y': y[:80]
}

data_train = pd.DataFrame(inputValuesTrain)

inputValuesTest = {
    'x': x[80:],
    'y': y[80:]
}

data_test = pd.DataFrame(inputValuesTest)

#Fit the ols model

X = sm.add_constant(data_train['x'])
model = sm.OLS(data_train['y'],X)
results = model.fit()

preidicted_train_y = results.predict(X)

r_squared_train = results.rsquared
mse_train = mean_squared_error(data_train['y'], preidicted_train_y) 

X_test = sm.add_constant(data_test['x'])
preidicted_test_y = results.predict(X_test)

r_squared_test = r2_score(data_test['y'], preidicted_test_y)
mse_test = mean_squared_error(data_test['y'], preidicted_test_y) 

print(f'r_squared_train is {r_squared_train},mse_train is {mse_train}')
print(f'r_squared_test is {r_squared_test},mse_test is {mse_test}')