# -*- coding: utf-8 -*-
#!/usr/bin/python

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost","root","199536abc","data" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# 如果数据表已经存在使用 execute() 方法删除表。
#cursor.execute("DROP TABLE IF EXISTS REGULARPLAYER")

# 创建数据表SQL语句
sql = """CREATE TABLE REGULARPLAYER(
    GAME_ID CHAR(20),
    TEAM_ID INT,
    TEAM_ABBREVIATION CHAR(3),
    TEAM_CITY CHAR(50),
    PLAYER_ID CHAR(20),
    PLAYER_NAME CHAR(50),
    START_POSITION CHAR(1),
    COMMENT CHAR(50),
    MIN CHAR(10),
    FGM CHAR(20),
    FGA CHAR(20),
    FG_PCT CHAR(20),
    FG3M CHAR(20),
    FG3A CHAR(20),
    FG3_PCT CHAR(20),
    FTM CHAR(20),
    FTA CHAR(20),
    FT_PCT CHAR(20),
    OREB CHAR(20),
    DREB CHAR(20),
    REB CHAR(20),
    AST CHAR(20),
    STL CHAR(20),
    BLK CHAR(20),
    TOV CHAR(20),
    PF CHAR(20),
    PTS CHAR(20),
    PLUS_MINUS CHAR(10)
        
        )
        """

cursor.execute(sql)

# 关闭数据库连接
db.close()