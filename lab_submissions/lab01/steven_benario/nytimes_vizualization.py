#! /usr/bin/env python
import sys
import os
import json
import requests
import matplotlib.pyplot as plt

#this file will graph the number of articles written about a topic by year

def querySingleYear(term, year):
	#input: query term, year
	#output: number of results

	#this function calls the NYT api to get how many responses there are in a year
	#r = requests.get('http://api.nytimes.com/svc/search/v2/articlesearch.json?q=computers&begin_date=20130101&end_date=20131231&api-key=MYAPIKEYGOESHERE')
    
    requestString = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?q=%s&begin_date=%d0101&end_date=%d1231&api-key=%s' % (term, year, year, MyNYTKey)
    
    myResponse = requests.get(requestString).json()
    numHits = myResponse['response']['meta']['hits']
    
    return numHits

def generateListing(term, startyear):
	#This function generates the (DATASTRUCT) that has year, and # responses, for all years from 
	#1900 to 2013
	#startyear = 1950
	years = range(startyear,2014)   #note that range includes bottom number, and excludes top number

	myResults = []
	for i in range(len(years)):
		myResults.append(querySingleYear(term, years[i]))

	#we have now looped through and done a query for all years in the list.
	# currently we have years -- a list from startyear to 2013
	# and myResults, a list of the results for each year, with corresponding indexes

	return(years, myResults)


def main():
	#get user input

	print "We're going to get some information on the frequency of search terms in NYTimes Articles"
	print

	# We're using this section to prevent needing to store the API key in the code
	global MyNYTKey
	MyNYTKey = os.environ.get("NYTIMES_APIKEY")
	if MyNYTKey == None:
	    print 'Error! Please enter (export) your API key to the variable "NYTIMES_APIKEY"'
	    exit(2)


	searchterm = raw_input("What term would you like to search for? ")
	startyear = raw_input("And what year would you like to start from? ")

	print "Processing..."

	(yearRange, numHits) = generateListing(searchterm, int(startyear))

	# now we plot!
	#%matplotlib inline

	plt.figure()
	plt.plot(yearRange, numHits)
	plt.xlabel('Year')
	plt.ylabel('number of articles')
	plt.title('Number of Articles by year')
	plt.show()


#do I need this?
if __name__ == '__main__':
    main()
