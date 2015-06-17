import MySQLdb
import urllib2
import json
from spider_v2.getAllTeams import getallteams

class getallseasons:
    def __init__(self):
        self.SEASONS = ["2000-01","2001-02","2002-03","2003-04","2004-05","2005-06","2006-07","2007-08","2008-09","2009-10","2010-11","2011-12","2012-13","2013-14","2014-15"]
        
    def getAllSeasons(self):

        numOfSeasons = len(self.SEASONS)
        
        for i in range(0,numOfSeasons):
            season = self.SEASONS[i]
            print"now is getting season:"+season
            getallteams.getAllID(season)
            print "finish a season!:"+season

getall = getallseasons()
getall.getAllSeasons()