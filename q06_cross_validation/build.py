# %load q06_cross_validation/build.py
# Default imports

from sklearn.model_selection import cross_val_score
import numpy as np
from greyatomlib.advanced_linear_regression.q01_load_data.build import load_data


data_set, X_train, X_test, y_train, y_test = load_data('data/house_prices_multivariate.csv')
np.random.seed(9)
def cross_validation(model,X,y):
    scores = cross_val_score(model, X, y, scoring='neg_mean_squared_error', cv=5)
    mean_error = scores.mean()
    return mean_error


# cross_validation(Model,X_test,y_train)
# Write your solution here





