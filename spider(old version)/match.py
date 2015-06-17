# -*- coding: utf-8 -*-
import urllib2
import urllib
import os
from bs4 import BeautifulSoup

#get html files
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

#class
page = 28283
url = 'http://www.stat-nba.com/game/' + str(page)+'.html'
request = urllib2.Request(url,None,headers) 
response = urllib2.urlopen(request)
page = response.read()
print page
#import the HTML File to beautifulsoup
soup = BeautifulSoup(page)
#print (soup.find_all('td'))

'''
for tds in soup.find_all('tr'):
	for a_tag in tds.find_all('a'):
		print(a_tag.string)
	for ranks in tds.find_all('td'):
		print(ranks.get('rank'))
'''
'''
print(soup.find_all('tr'))
'''