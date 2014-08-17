#!/usr/bin/env python

# Approximate the relationship of a marathoner's height to weight.

import csv

def read_variables(filename):
  x = []
  y = []
  with open(filename, 'rb') as csvfile:
    next(csvfile) # Skip header
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
      a = row[3] # Height in cm
      b = row[4] # Weight in kg
      if (len(a) > 0 and len(b) > 0):
        x.append(float(a))
        y.append(float(b))
  return x,y

def amean(arr):
  return sum(arr) / len(arr)

# Variance equation given in class divides by N - 1,
#  but numpy et al divide by N
def variance(arr, m = None):
  l = len(arr)
  mean = m or amean(arr)
  return reduce(lambda acc, a: acc + (a - mean) ** 2, arr, 0) / (l - 1)

def covariance(arr1, arr2, m1 = None, m2 = None):
  l = len(arr1)
  mean1 = m1 or amean(arr1)
  mean2 = m2 or amean(arr2)
  return sum(map(lambda (x, y): (x - mean1) * (y - mean2),
                 zip(arr1, arr2))) / (l - 1)

def sum_of_squares(arr, m = None):
  mean = m or amean(arr)
  return sum(map(lambda a: (a - mean) ** 2, arr))

def sum_of_squares_res(arr1, arr2):
  return sum(map(lambda (a1, a2): (a1 - a2) ** 2, zip(arr1, arr2)))

def r_squared(ss_tot, ss_res):
  return 1 - (ss_res / ss_tot)

# Train model
x_train, y_train = read_variables("marathon_training.csv")
x_train_mean = sum(x_train) / len(x_train)
y_train_mean = sum(y_train) / len(y_train)
var = variance(x_train, x_train_mean)
cov = covariance(x_train, y_train, x_train_mean, y_train_mean)
beta = cov / var
alpha = (y_train_mean - (beta * x_train_mean))

print "model parameters: alpha = %f, beta = %f" % (alpha, beta)

# Test model
x_test, y_test = read_variables("marathon_testing.csv")
y_pred = map(lambda x: alpha + (beta * x), x_test)

# Evaluate model
ss_tot = sum_of_squares(y_test)
ss_res = sum_of_squares_res(y_test, y_pred)
r2 = r_squared(ss_tot, ss_res)

print "r-squared = %f" % r2

# Discussion
#
# $ ./linear_regression.py
# model parameters: alpha = -76.817132, beta = 0.780209
# r-squared = 0.690948
#
# The model is reasonably accurate at predicting marathoner's weights,
#  given their heights. I anticipate further accuracy gains by using
#  multiple explanatory variables.
