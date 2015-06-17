# -*- coding: utf-8 -*-
import urllib2
import urllib
from bs4 import BeautifulSoup

#get html files
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
url = 'http://www.stat-nba.com/game/37439.html'
headers = { 'User-Agent' : user_agent }
request = urllib2.Request(url,None,headers) 
response = urllib2.urlopen(request)
page = response.read()

#import the HTML File to beautifulsoup
soup = BeautifulSoup(page)
#print (soup.find_all('td'))

for tds in soup.find_all('tr'):
	for a_tag in tds.find_all('a'):
		print(a_tag.string)
	for ranks in tds.find_all('td'):
		print(ranks.get('rank'))


"""
print(soup.find_all('tr'))
"""