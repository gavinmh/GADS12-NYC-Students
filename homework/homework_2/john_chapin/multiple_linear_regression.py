#!/usr/bin/env python

# Approximate the relationship of a marathoner's attributes to weight

import re
from csv import DictReader
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression

def extract_pob(s):
  m = re.search('\((.*)\)', s)
  if m != None:
    return m.group(1)
  else:
    return ''

key_mapping = {
    'Age': 'age',
    'Height, cm': 'height',
    'Sex': 'sex',
    'Weight': 'weight'}

val_mapping = {
    'age': int,
    'height': float,
    'sex': str,
    'weight': float,
    'country': str,
    'pob': extract_pob
    }

# TODO: Perhaps there is a more idiomatic way to do this in Python?
def valid_row(row):
  valid_values = filter(lambda s: len(s) > 0, row.values())
  return (len(row) == len(valid_values))

def read_variables(filename):
  X = []
  y = []
  with open(filename, 'rb') as csvfile:
    reader = DictReader(csvfile)
    for row in reader:
      filtered_row = {key_mapping[k]: row[k] for k in key_mapping.keys()}
      if valid_row(filtered_row):
        normalized_row = {k: val_mapping[k](v) for k, v in filtered_row.items()}
        y.append(normalized_row.pop('weight'))
        X.append(normalized_row)
  return X, y

dv = DictVectorizer()

# Train model
X_train_raw, y_train = read_variables("marathon_training.csv")
dv.fit(X_train_raw)
X_train_dense = dv.transform(X_train_raw).todense()

regressor = LinearRegression()
regressor.fit(X_train_dense, y_train)

print "model parameters: coef = %f" % regressor.coef_[0]

# Test model
X_test_raw, y_test = read_variables("marathon_testing.csv")
X_test_dense = dv.transform(X_test_raw).todense()
predictions = regressor.predict(X_test_dense)

# Evaluate model
r2 = regressor.score(X_test_dense, y_test)

print "r-squared = %f" % r2

# Discussion
#
# $ ./multiple_linear_regression.py
# model parameters: coef = 0.131689
# r-squared = 0.744332
#
# The model is quite accurate at predicting marathoner's weights, given their
#  ages, heights, and sex. Adding multiple explanatory variables significantly
#  improved the model's performance, compared to the simple linear model from
#  the previous homework assignment.
#
# However, the given set of explanatory variables used seems to be the best
#  available. Adding 'Country' or 'Place of birth' degrades model performance.
