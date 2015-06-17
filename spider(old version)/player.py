# _*_ coding:utf-8 _*_
import urllib
import urllib2
import re
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
page = 37439
url = 'http://www.stat-nba.com/game/' + str(page)+'.html'
headers = { 'User-Agent' : user_agent }
try:
	request = urllib2.Request(url,None,headers)
	response = urllib2.urlopen(request)
#	print response.read()
	content = response.read().decode('utf-8')
	pattern_g = re.compile('<td class ="normal .*? change_color col.*? row.*?>(.*?)</td>',re.S)
	items = re.findall(pattern_g,content)
	for item in items:
		print item
except urllib2.URLError,e:
	if hasattr(e,"code"):
		print e.code
	if hasattr(e,"reason"):
		print e.reason
