# -*- coding: utf-8 -*-
import urllib2
import json
import MySQLdb



class getTeamInfo:
    #页面初始化
    def __init__(self):
        self.siteURL = 'http://stats.nba.com/stats/boxscoretraditionalv2?EndPeriod=10&EndRange=28800&GameID=0021401024&RangeType=2&Season=2014-15&SeasonType=Regular+Season&StartPeriod=1&StartRange=0'

    def getJsonData(self,url):
        try:
            page = urllib2.urlopen(url)
            tempdata =  page.read()
            s = json.loads(tempdata)
            
            return s
        except:
            print "wrong at get json data"
                
    def getNumOfPlayers(self,s):
        return len(s["resultSets"][0]["rowSet"])
        

    def savePlayersInfo(self,url):
        try:
            
            jsonD = self.getJsonData(url)
      
        #print jsonD.keys()
            self.savePlayerInfo(jsonD,0)
            self.savePlayerInfo(jsonD,1)
            
            
        except:
            print "wrong at get JSON INFO"
        
               
    def savePlayerInfo(self,s,i):
        SEASON = s["resultSets"][0]["rowSet"][0][8]
        GAME_DATE = s["resultSets"][5]["rowSet"][i][0]
        GAME_ID = s["resultSets"][5]["rowSet"][i][2]
        TEAM_ID = s["resultSets"][5]["rowSet"][i][3]
        TEAM_ABBREVIATION = s["resultSets"][5]["rowSet"][i][4]
        TEAM_WINS_LOSSES = s["resultSets"][5]["rowSet"][i][7]
        QTR1 = s["resultSets"][5]["rowSet"][i][8]
        QTR2 = s["resultSets"][5]["rowSet"][i][9]
        QTR3 = s["resultSets"][5]["rowSet"][i][10]
        QTR4 = s["resultSets"][5]["rowSet"][i][11]
        OT1 = s["resultSets"][5]["rowSet"][i][12]
        OT2 = s["resultSets"][5]["rowSet"][i][13]
        OT3 = s["resultSets"][5]["rowSet"][i][14]
        OT4 = s["resultSets"][5]["rowSet"][i][15]
        OT5 = s["resultSets"][5]["rowSet"][i][16]
        OT6 = s["resultSets"][5]["rowSet"][i][17]
        OT7 = s["resultSets"][5]["rowSet"][i][18]
        
        PTS = s["resultSets"][5]["rowSet"][i][22]

        
           
        str1 ="'"+SEASON+"','"+GAME_DATE+"','"+GAME_ID+"','"+str(TEAM_ID)+"','"+TEAM_ABBREVIATION+"','"+TEAM_WINS_LOSSES+"','"+str(QTR1)+"','"+str(QTR2)+"','"+str(QTR3)+"','"+str(QTR4)+"','"+str(OT1)+"','"+str(OT2)+"','"+str(OT3)+"','"+str(OT4)+"','"+str(OT5)+"','"+str(OT6)+"','"+str(OT7)+"','"+str(PTS)+"'"                                         
        #打开数据库链接
        db = MySQLdb.connect("localhost","root","199536abc","data")
 
        
        #使用cursor()方法获取操作游标
        cursor = db.cursor()
        sql = "INSERT INTO TEAMINFO(SEASON,GAME_DATE,GAME_ID,TEAM_ID,TEAM_ABBREVIATION,TEAM_WINS_LOSSES,QTR1,QTR2,QTR3,QTR4,OT1,OT2,OT3,OT4,OT5,OT6,OT7,PTS) VALUES ("+str1+")"
        


        try:
            cursor.execute(sql)
            # 执行sql语句
        # 提交到数据库执行
            db.commit()
            
        except:
            # Rollback in case there is any error
            db.rollback()
            print "wrong"


        #print PLAYER_NAME

        
"""
url = 'http://stats.nba.com/stats/boxscoresummaryv2?GameID=0020300286'
getPlayer.savePlayersInfo(url)
"""

url = 'http://stats.nba.com/stats/boxscoresummaryv2?GameID=0029400557'
getTeamInfo = getTeamInfo()

getTeamInfo.savePlayersInfo(url)