import MySQLdb
import urllib2
import json
from new_spider.getRegularTeam import getREGTeam
from new_spider.getRegularPlayer import getREGPlayer
from new_spider.getTeamInfo import getTeamInfo
from new_spider.getPlayoffPlayer import getPLAYOFFPlayer
from new_spider.getPlayoffTeam import getPLAYOFFTeam


class getURL:
    def __init__(self):
        self.siteURL = 'http://www.stat-nba.com/game/'
      
    def getGameID(self,teamid,season):
        str2 = 'http://stats.nba.com/stats/teamgamelog?LeagueID=00&Season='+str(season)+'&SeasonType=Playoffs&TeamID='+str(teamid)
                


            
            
        try:
            page = urllib2.urlopen(str2)
            tempdata =  page.read()
            
            s2 = json.loads(tempdata)
            numOfGames = len(s2["resultSets"][0]["rowSet"])
        
        
            for i in range(0,numOfGames):
                tempGameID =s2["resultSets"][0]["rowSet"][i][1]
                
                
                jsonPLAYOFFTeamInfoURL = 'http://stats.nba.com/stats/boxscoresummaryv2?GameID='+tempGameID
   
                print "now is getting game:"+"playoff_team-info"+tempGameID
                getTeamInfo.savePlayersInfo(jsonPLAYOFFTeamInfoURL)
        except:
            print "wrong at getURL"
        
        
        
geturl = getURL()

"""
teamid = 1610612744
season = "2013-14"
geturl.getGameID(teamid, season)
"""