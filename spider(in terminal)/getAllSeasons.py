from getAllTeams import getallteams

class getallseasons:
    def __init__(self):
        self.SEASONS = ["1980-81","1981-82"]
        
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