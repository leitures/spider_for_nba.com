import MySQLdb
import urllib2
import json
from getRegularTeam import getREGTeam
from getRegularPlayer import getREGPlayer
from getTeamInfo import getTeamInfo
from getPlayoffPlayer import getPLAYOFFPlayer
from getPlayoffTeam import getPLAYOFFTeam


class getURL:
    def __init__(self):
        self.siteURL = 'http://www.stat-nba.com/game/'
      
    def getGameID(self,teamid,season):
        str1 = 'http://stats.nba.com/stats/teamgamelog?LeagueID=00&Season='+str(season)+'&SeasonType=Regular+Season&TeamID='+str(teamid)
        str2 = 'http://stats.nba.com/stats/teamgamelog?LeagueID=00&Season='+str(season)+'&SeasonType=Playoffs&TeamID='+str(teamid)
                

        try:
            page = urllib2.urlopen(str1)
            tempdata =  page.read()
            
            s = json.loads(tempdata)
            numOfGames = len(s["resultSets"][0]["rowSet"])
        
        
            for i in range(0,numOfGames):
                tempGameID =s["resultSets"][0]["rowSet"][i][1]
                jsonREGULARURL = 'http://stats.nba.com/stats/boxscoretraditionalv2?EndPeriod=10&EndRange=28800&GameID='+tempGameID+'&RangeType=2&Season='+str(season)+'&SeasonType=Regular+Season&StartPeriod=1&StartRange=0'
                jsonREGTeamInfoURL = 'http://stats.nba.com/stats/boxscoresummaryv2?GameID='+tempGameID
                print "now is getting game:"+"regular-team_data"+tempGameID
                
                getREGTeam.savePlayersInfo(jsonREGULARURL)
                
                print "now is getting game:"+"regular-player_data"+tempGameID                
                getREGPlayer.savePlayersInfo(jsonREGULARURL)
                
                print "now is getting game:"+"regular-team_info"+tempGameID                
                getTeamInfo.savePlayersInfo(jsonREGTeamInfoURL)
        except:
            print "wrong at getURL"
            
            
        try:
            page = urllib2.urlopen(str2)
            tempdata =  page.read()
            
            s2 = json.loads(tempdata)
            numOfGames = len(s2["resultSets"][0]["rowSet"])
        
        
            for i in range(0,numOfGames):
                tempGameID =s2["resultSets"][0]["rowSet"][i][1]
                jsonPLAYOFFURL = 'http://stats.nba.com/stats/boxscoretraditionalv2?EndPeriod=10&EndRange=28800&GameID='+tempGameID+'&RangeType=2&Season='+str(season)+'&SeasonType=Playoffs&StartPeriod=1&StartRange=0'
                
                
                jsonPLAYOFFTeamInfoURL = 'http://stats.nba.com/stats/boxscoresummaryv2?GameID='+tempGameID
                print "now is getting game:"+"playoff-team_data"+tempGameID                
                getPLAYOFFTeam.savePlayersInfo(jsonPLAYOFFURL)
                
                print "now is getting game:"+"playoff-player_data"+tempGameID
                getPLAYOFFPlayer.savePlayersInfo(jsonPLAYOFFURL)
                
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