import urllib2
import json

url = 'http://stats.nba.com/stats/boxscoresummaryv2?GameID=0029400557'
page = urllib2.urlopen(url)
tempdata =  page.read()
s = json.loads(tempdata)

#GameInfo
"""
    "GAME_DATE",
    "ATTENDANCE",
    "GAME_TIME"
"""
url = 'http://stats.nba.com/stats/boxscoresummaryv2?GameID=0028000928'

SEASON = s["resultSets"][0]["rowSet"][0][8]
GAME_DATE = s["resultSets"][4]["rowSet"][0][0]
ATTENDANCE = s["resultSets"][4]["rowSet"][0][1]
GAME_TIME = s["resultSets"][4]["rowSet"][0][2]
print SEASON
#LineScore
"""
GAME_DATE_EST,
GAME_SEQUENCE,
GAME_ID,
TEAM_ID,
TEAM_ABBREVIATION,
TEAM_CITY_NAME,
TEAM_NICKNAME,
TEAM_WINS_LOSSES,
PTS_QTR1,
PTS_QTR2,
PTS_QTR3,
PTS_QTR4,
PTS_OT1,
PTS_OT2,
PTS_OT3,
PTS_OT4,
PTS_OT5,
PTS_OT6,
PTS_OT7,
PTS_OT8,
PTS_OT9,
PTS_OT10,
PTS,
"""
GAME_DATE = s["resultSets"][5]["rowSet"][0][0]
GAME_ID = s["resultSets"][5]["rowSet"][0][2]
TEAM_ID = s["resultSets"][5]["rowSet"][0][3]
TEAM_ABBREVIATION = s["resultSets"][5]["rowSet"][0][4]


TEAM_WINS_LOSSES = s["resultSets"][5]["rowSet"][0][7]
PTS_QTR1 = s["resultSets"][5]["rowSet"][0][8]
PTS_QTR2 = s["resultSets"][5]["rowSet"][0][9]
PTS_QTR3 = s["resultSets"][5]["rowSet"][0][10]
PTS_QTR4 = s["resultSets"][5]["rowSet"][0][11]
PTS_OT1 = s["resultSets"][5]["rowSet"][0][12]
PTS_OT2 = s["resultSets"][5]["rowSet"][0][13]
PTS_OT3 = s["resultSets"][5]["rowSet"][0][14]
PTS_OT4 = s["resultSets"][5]["rowSet"][0][15]
PTS_OT5 = s["resultSets"][5]["rowSet"][0][16]
PTS_OT6 = s["resultSets"][5]["rowSet"][0][17]
PTS_OT7 = s["resultSets"][5]["rowSet"][0][18]
PTS_OT8 = s["resultSets"][5]["rowSet"][0][19]
PTS_OT9 = s["resultSets"][5]["rowSet"][0][20]
PTS_OT10 = s["resultSets"][5]["rowSet"][0][21]
PTS = s["resultSets"][5]["rowSet"][0][22]
