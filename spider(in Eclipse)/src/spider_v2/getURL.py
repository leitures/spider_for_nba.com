import MySQLdb
import urllib2
import json
from spider_v2.getRugularPlayer import getPlayer

class getURL:
    def __init__(self):
        self.siteURL = 'http://www.stat-nba.com/game/'
      
    def getGameID(self,teamid,season):
        str1 = 'http://stats.nba.com/stats/teamgamelog?LeagueID=00&Season='+str(season)+'&SeasonType=Regular+Season&TeamID='+str(teamid)
        page = urllib2.urlopen(str1)
        tempdata =  page.read()
        s = json.loads(tempdata)
        numOfGames = len(s["resultSets"][0]["rowSet"])
        
        
     
        for i in range(0,numOfGames):
            tempGameID =s["resultSets"][0]["rowSet"][i][1]
            jsonURL = 'http://stats.nba.com/stats/boxscoretraditionalv2?EndPeriod=10&EndRange=28800&GameID='+tempGameID+'&RangeType=2&Season='+str(season)+'&SeasonType=Regular+Season&StartPeriod=1&StartRange=0'
            print "now is getting game:"+tempGameID
            getPlayer.savePlayersInfo(jsonURL)
        
        
geturl = getURL()
"""
teamid = 1610612744
season = "2013-14"
geturl.getGameID(teamid, season)
"""