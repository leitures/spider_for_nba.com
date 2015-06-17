# encoding: utf-8
#!/usr/bin/python

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost","root","199536abc","test" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()


# 如果数据表已经存在使用 execute() 方法删除表。
cursor.execute("DROP TABLE IF EXISTS PLAYER")

# 创建数据表SQL语句
sql = """CREATE TABLE PLAYER (
         GAME_ID  CHAR(20) NOT NULL,
         TEAM_ID INT,
         NAME CHAR(50)
          )"""

cursor.execute(sql)

# 关闭数据库连接
db.close()