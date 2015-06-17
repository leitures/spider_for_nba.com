import MySQLdb
import urllib2
import json
from teaminfo.getAllTeams import getallteams

class getallseasons:
    def __init__(self):
        self.SEASONS = ["2000-01"]
        
    def getAllSeasons(self):

        numOfSeasons = len(self.SEASONS)
        
        for i in range(0,numOfSeasons):
            try:
                season = self.SEASONS[i]
                print"now is getting season:"+season
                getallteams.getAllID(season)
                print "finish a season!:"+season
            except:
                print "wrong at getallseasons"
getall = getallseasons()
getall.getAllSeasons()