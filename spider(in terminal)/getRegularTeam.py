# -*- coding: utf-8 -*-
import urllib2
import json
import MySQLdb


class getRegularTEAM:
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
            tempObj = getRegularTEAM()
            jsonD = tempObj.getJsonData(url)
        #print jsonD.keys()
            for i in range(0,2):
                self.savePlayerInfo(jsonD,i)
        except:
            print "wrong at get JSON INFO"
               
    def savePlayerInfo(self,s,i):
        GAME_ID = s["resultSets"][1]["rowSet"][i][0]
        TEAM_ID = s["resultSets"][1]["rowSet"][i][1]
#TEAM_ABBREVIATION CHAR(3)
        TEAM_NAME = s["resultSets"][1]["rowSet"][i][2]
        TEAM_ABBREVIATION = s["resultSets"][1]["rowSet"][i][3]
#TEAM_CITY CHAR(50)
        TEAM_CITY = s["resultSets"][1]["rowSet"][i][4]
#PLAYER_ID INT
#PLAYER_NAME CHAR(50)
#START_POSITION CHAR(1)
#COMMENT CHAR(50)
#MIN CHAR(10)
        MIN = s["resultSets"][1]["rowSet"][i][5]
#FGM INT
        FGM = s["resultSets"][1]["rowSet"][i][6]
#FGA INT
        FGA = s["resultSets"][1]["rowSet"][i][7]
#FG_PCT DOUBLE
        FG_PCT = s["resultSets"][1]["rowSet"][i][8]
#FG3M INT
        FG3M = s["resultSets"][1]["rowSet"][i][9]
#FG3A INT
        FG3A = s["resultSets"][1]["rowSet"][i][10]

#FG3_PCT DOUBLE
        FG3_PCT = s["resultSets"][1]["rowSet"][i][11]
#FTM INT
        FTM = s["resultSets"][1]["rowSet"][i][12]
#FTA INT
        FTA = s["resultSets"][1]["rowSet"][i][13]
#FT_PCT DOUBLE
        FT_PCT = s["resultSets"][1]["rowSet"][i][14]
#OREB INT
        OREB = s["resultSets"][1]["rowSet"][i][15]
#DREB INT
        DREB = s["resultSets"][1]["rowSet"][i][16]
#REB INT
        REB = s["resultSets"][1]["rowSet"][i][17]
#AST INT
        AST = s["resultSets"][1]["rowSet"][i][18]
#STL INT
        STL = s["resultSets"][1]["rowSet"][i][19]
#BLK INT
        BLK = s["resultSets"][1]["rowSet"][i][20]
#TOV INT
        TOV = s["resultSets"][1]["rowSet"][i][21]
#PF INT
        PF = s["resultSets"][1]["rowSet"][i][22]
#PTS INT
        PTS = s["resultSets"][1]["rowSet"][i][23]
#PLUS_MINUS CHAR(10)
        PLUS_MINUS = s["resultSets"][1]["rowSet"][i][24]
        
           
        str1 ="'"+GAME_ID+"','"+str(TEAM_ID)+"','"+TEAM_NAME+"','"+TEAM_ABBREVIATION+"','"+TEAM_CITY+"','"+str(MIN)+"','"+str(FGM)+"','"+str(FGA)+"','"+str(FG_PCT)+"','"+str(FG3M)+"','"+str(FG3A)+"','"+str(FG3_PCT)+"','"+str(FTM)+"','"+str(FTA)+"','"+str(FT_PCT)+"','"+str(OREB)+"','"+str(DREB)+"','"+str(REB)+"','"+str(AST)+"','"+str(STL)+"','"+str(BLK)+"','"+str(TOV)+"','"+str(PF)+"','"+str(PTS)+"','"+str(PLUS_MINUS)+"'"                                         
        #打开数据库链接
        db = MySQLdb.connect("localhost","root","199536abc","data")
        
        
        #使用cursor()方法获取操作游标
        cursor = db.cursor()
        sql = "INSERT INTO REGULARTEAM(GAME_ID,TEAM_ID,TEAM_NAME,TEAM_ABBREVIATION,TEAM_CITY,MIN,FGM,FGA,FG_PCT,FG3M,FG3A,FG3_PCT,FTM,FTA,FT_PCT,OREB,DREB,REB,AST,STL,BLK,TOV,PF,PTS,PLUS_MINUS) VALUES ("+str1+")"
        


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
        
        
getREGTeam = getRegularTEAM()
"""
url = 'http://stats.nba.com/stats/boxscoretraditionalv2?EndPeriod=10&EndRange=28800&GameID=0021401024&RangeType=2&Season=2014-15&SeasonType=Regular+Season&StartPeriod=1&StartRange=0'

getPlayer.savePlayersInfo(url)
"""
