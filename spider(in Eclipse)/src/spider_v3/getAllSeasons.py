import MySQLdb
import urllib2
import json
from spider_v3.getAllTeams import getallteams

class getallseasons:
    def __init__(self):
        self.SEASONS = ["1980-81"]
        
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