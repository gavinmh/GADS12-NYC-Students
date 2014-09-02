# GA Data Science 12

# Ryan Tuck
# 12 Aug 2014

# lab 2
# linear regression

# to run:
# $ import rt_linear_regression
# $ rt_linear_regression.lab2()

# ======================================================================

import numpy

def lab2():
	
	# establish data
	training = [1,2,3,4,5]
	prepTime = [8,15,22,1,35]
	quality  = [8,7.8,4,9.4,3]
	
	# Question 1
	print "1. Variance of explanatory variable, prep time: %f" % variance(prepTime)
	
	# Question 2
	print "2. Covariance of prep time and quality of lectures: %f" % covariance(prepTime,quality)
	
	# Question 3
	beta = covariance(prepTime,quality) / variance(prepTime)
	print "3. Beta (cov/var) = %f" % beta
	
	# Question 4
	alpha = average(quality) - beta * average(prepTime)
	print "4. Alpha (y - Bx) = %f" % alpha
	
	#Question 5
	testTraining = [1,2,3,4]
	testPrepTime = [11,10,3,24]
	testQuality  = [7.9,7.2,9.2,4]
	predictedQuality = [0,0,0,0]
	print "5. Predicted qualities for new test set:"
	
	for n in range(0,len(testPrepTime)):
		predictedQuality[n] = fOfX(alpha,beta,testPrepTime[n])
		print " - Prep: %i yields quality: %f" % (testPrepTime[n], predictedQuality[n])
	
	# Question 6
	print "6. R^2 value for test data: %f" % rSquared(testPrepTime,testQuality,alpha,beta)
	
	# Question 7
	print "7. Conclusion: Surprisingly, we can be fairly confident that the quality of a lecture decreases with amount of times spent shoehorning memes into slide deck."
	
	
def rSquared(x,y,alpha,beta):
	
	r2 = 0
	
	sameLength = False
	if len(x) == len(y):
		sameLength = True
	
	if not sameLength:
		print "not same length!"
	else:	
		# calculate ssRes
		ssRes = 0
		for n in range(0,len(y)):
			dist = y[n] - fOfX(alpha,beta,x[n])
			ssRes += pow(dist,2)
	
		# calculate ssTot
		ssTot = 0
		for n in range (0,len(y)):
			dist = y[n] - average(y)
			ssTot += pow(dist,2)
	
		r2 = 1 - ssRes/ssTot
	
	return r2
	

def fOfX(alpha,beta,x):
	return alpha + beta*x
	
def variance(x):
	
	# get basics
	length = len(x)
	avg = average(x)
	
	# run through and calculate sum of distances^2
	sumOfDistSquared = 0
	for n in x:
		dist = n - avg
		sumOfDistSquared += pow(dist,2)
	
	# divide by n-1 to get variance
	var = sumOfDistSquared / (length-1)
	
	return var

def covariance(x,y):

	# check that data sets are same length
	sameLength = False
	if len(x) == len(y): 
		sameLength = True
	
	if not sameLength:
		print "Data sets aren't same length"
	else:
		# get basics
		xAvg = average(x)
		yAvg = average(y)
	
		# sum distance products
		sumOfDistanceProducts  = 0
		for n in range(0,len(x)):
			xDist = x[n] - xAvg
			yDist = y[n] - yAvg
			
			sumOfDistanceProducts += xDist * yDist
		
		cov = sumOfDistanceProducts / (len(x)-1)
		
		return cov
		

def average(x):
	
	length = len(x)
	
	sum = 0
	for n in x:
		sum = sum + n
	avg = sum / length

	return avg
