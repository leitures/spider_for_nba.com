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
sql = """CREATE TABLE NEWTEAMINFO(
SEASON CHAR(20),
GAME_DATE CHAR(20),
GAME_ID CHAR(20),
TEAM_ID INT,
TEAM_ABBREVIATION CHAR(3),
TEAM_WINS_LOSSES CHAR(20),
QTR1 CHAR(20),
QTR2 CHAR(20),
QTR3 CHAR(20),
QTR4 CHAR(20),
OT1 CHAR(20),
OT2 CHAR(20),
OT3 CHAR(20),
OT4 CHAR(20),
OT5 CHAR(20),
OT6 CHAR(20),
OT7 CHAR(20),
PTS CHAR(20)

        )
        """

cursor.execute(sql)

# 关闭数据库连接
db.close()