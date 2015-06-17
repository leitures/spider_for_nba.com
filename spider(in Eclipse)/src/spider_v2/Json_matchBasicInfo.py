import urllib2
import json

url = 'http://stats.nba.com/stats/commonplayoffseries?LeagueID=00&Season=2014-15&SeriesID=002140059' 
page = urllib2.urlopen(url)
tempdata =  page.read()
s = json.loads(tempdata)
print s.keys()
print "over"


#print s.keys()
#print s["resultSets"]
'''
s = json.loads('{"name":"test", "type":{"name":"seq", "parameter":["1", "2"]}}')
print s
print s.keys()
print s["name"]
print s["type"]["name"]
print s["type"]["parameter"][1]
'''

'''
{u'type': {u'parameter': [u'1', u'2'], u'name': u'seq'}, u'name': u'test'}
[u'type', u'name']
test
seq
2

'''