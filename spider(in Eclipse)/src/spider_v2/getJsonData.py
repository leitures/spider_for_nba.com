import urllib2
import json

url = 'http://stats.nba.com/stats/boxscoretraditionalv2?EndPeriod=10&EndRange=28800&GameID=0021401024&RangeType=2&Season=2014-15&SeasonType=Regular+Season&StartPeriod=1&StartRange=0'
page = urllib2.urlopen(url)
tempdata =  page.read()
s = json.loads(tempdata)

print s["resultSets"][1]["rowSet"][1][24]
numOfPlayers = len(s["resultSets"][0]["rowSet"])
i=0
##GAME_ID CHAR
GAME_ID = s["resultSets"][0]["rowSet"][i][0]
#TEAM_ID INT
TEAM_ID = s["resultSets"][0]["rowSet"][i][1]
#TEAM_ABBREVIATION CHAR(3)
TEAM_ABBREVIATION = s["resultSets"][0]["rowSet"][i][2]
#TEAM_CITY CHAR(50)
TEAM_CITY = s["resultSets"][0]["rowSet"][i][3]
#PLAYER_ID INT
PLAYER_ID = s["resultSets"][0]["rowSet"][i][4]
#PLAYER_NAME CHAR(50)
PLAYER_NAME = s["resultSets"][0]["rowSet"][i][5]
#START_POSITION CHAR(1)
START_POSITION = s["resultSets"][0]["rowSet"][i][6]
#COMMENT CHAR(50)
COMMENT = s["resultSets"][0]["rowSet"][i][7]
#MIN CHAR(10)
MIN = s["resultSets"][0]["rowSet"][i][8]
#FGM INT
FGM = s["resultSets"][0]["rowSet"][i][9]
#FGA INT
FGA = s["resultSets"][0]["rowSet"][i][10]
#FG_PCT DOUBLE
FG_PCT = s["resultSets"][0]["rowSet"][i][11]
#FG3M INT
FG3M = s["resultSets"][0]["rowSet"][i][12]
#FG3A INT
FG3A = s["resultSets"][0]["rowSet"][i][13]
#FG3_PCT DOUBLE
FG3_PCT = s["resultSets"][0]["rowSet"][i][14]
#FTM INT
FTM = s["resultSets"][0]["rowSet"][i][15]
#FTA INT
FTA = s["resultSets"][0]["rowSet"][i][16]
#FT_PCT DOUBLE
FT_PCT = s["resultSets"][0]["rowSet"][i][17]
#OREB INT
OREB = s["resultSets"][0]["rowSet"][i][18]
#DREB INT
DREB = s["resultSets"][0]["rowSet"][i][19]
#REB INT
REB = s["resultSets"][0]["rowSet"][i][20]
#AST INT
AST = s["resultSets"][0]["rowSet"][i][21]
#STL INT
STL = s["resultSets"][0]["rowSet"][i][22]
#BLK INT
BLK = s["resultSets"][0]["rowSet"][i][23]
#TOV INT
TOV = s["resultSets"][0]["rowSet"][i][24]
#PF INT
PF = s["resultSets"][0]["rowSet"][i][25]
#PTS INT
PTS = s["resultSets"][0]["rowSet"][i][26]
#PLUS_MINUS CHAR(10)
PLUS_MINUS = s["resultSets"][0]["rowSet"][i][27]


str1 ="'"+GAME_ID+"','"+str(TEAM_ID)+"','"+TEAM_ABBREVIATION+"','"+TEAM_CITY+"','"+str(PLAYER_ID)+"','"+PLAYER_NAME+"','"+START_POSITION+"','"+COMMENT+"','"+MIN+"','"+str(FGM)+"','"+str(FGA)+"','"+str(FG_PCT)+"','"+str(FG3M)+"','"+str(FG3A)+"','"+str(FG3_PCT)+"','"+str(FTM)+"','"+str(FTA)+"','"+str(FT_PCT)+"','"+str(OREB)+"','"+str(DREB)+"','"+str(REB)+"','"+str(AST)+"','"+str(STL)+"','"+str(BLK)+"','"+str(TOV)+"','"+str(PF)+"','"+str(PTS)+"','"+str(PLUS_MINUS)+"'"                                       
        
'''
print GAME_ID
print TEAM_ID
print TEAM_ABBREVIATION
print TEAM_CITY
print PLAYER_ID
print PTS
print PLAYER_NAME

'''

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