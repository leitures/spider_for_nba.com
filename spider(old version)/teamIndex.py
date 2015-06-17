# _*_ coding:utf-8 _*_
import urllib
import urllib2
import re
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
page = 36082
url = 'http://china.nba.com/teamindex/'
headers = { 'User-Agent' : user_agent }
try:
	request = urllib2.Request(url,None,headers)
	response = urllib2.urlopen(request)
	print response.read()
	
except urllib2.URLError,e:
	if hasattr(e,"code"):
		print e.code
	if hasattr(e,"reason"):
		print e.reason
