
from new_spider.getURL import geturl

class getAllTeams:
    def __init__(self):
        self.TeamID = ['1610612766','1610612765','1610612764','1610612763','1610612762','1610612761','1610612760','1610612759','1610612758','1610612757','1610612756','1610612755','1610612754','1610612753','1610612752','1610612751','1610612750','1610612749','1610612748','1610612747','1610612746','1610612745','1610612744','1610612743','1610612742','1610612741','1610612740','1610612739','1610612738','1610612737']
    
    def getAllID(self,season):
        numOfTeams = len(self.TeamID)
        for i in range(0,numOfTeams):
            teamid = self.TeamID[i]
            print "now is getting team:"+teamid
            geturl.getGameID(teamid, season)
            
        
getallteams = getAllTeams()
