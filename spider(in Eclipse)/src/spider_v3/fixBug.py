import urllib2
import json

url = 'http://stats.nba.com/stats/boxscoresummaryv2?GameID=0020300286'
try:
    page = urllib2.urlopen(url)
    tempdata =  page.read()
    s = json.loads(tempdata)
except:
    print "wrong"

