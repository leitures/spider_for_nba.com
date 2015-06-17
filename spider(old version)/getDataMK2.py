# -*- coding: utf-8 -*-
import urllib2
import urllib
import os
import tool
import re
from bs4 import BeautifulSoup

class Spider:
    #页面初始化
    def __init__(self):
        self.siteURL = 'http://www.stat-nba.com/game/'
        self.tool = tool.Tool()
    
    
    #get html files
    def getPage(self,pageIndex):
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent }
        url = self.siteURL + str(pageIndex)+'.html'
        request = urllib2.Request(url,None,headers)
        response = urllib2.urlopen(request)
        return response.read()
    
    def mkdir(self,path):
        path = path.strip()
        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists=os.path.exists(path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            print u"偷偷新建了名字叫做",path,u'的文件夹'
            # 创建目录操作函数
            os.makedirs(path)
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            print u"名为",path,'的文件夹已经创建成功'
            return False


def savDetailData(self,page,fileName):
    soup = BeautifulSoup(page)
        player_ranks = []
        player=[]
        for tds in soup.find_all('tr'):
            j=0
            for a_tag in tds.find_all('a'):
                #                player.append(a_tag.string)
                f = open(fileName,"a")
                print u"正在保存球员名为：",a_tag
                f.write(a_tag.string.encode('utf-8')+':')
                f.close()
            for ranks in tds.find_all('td'):
                f = open(fileName,"a")
                print u"正在保存球员信息"
                rankTemp = str(ranks.get('rank'))
                if rankTemp=='None':
                    continue
                else:
                    j=j+1
                if(j<21):
                    f.write(rankTemp+',')
                else:
                    f.write(rankTemp)
                f.close()
            f = open(fileName,"a")
            print u"完成一个球员信息采集"
            
            
            f.write('\n')
            
            '''
                for ranks in tds.find_all('td'):
                player_ranks.append(ranks.get('rank'))
                f = open(fileName,"w+")
                print u"正在保存比赛信息为：",fileName
                f.write(ranks.string)
                '''


def getSingleData(self,page,matchText):
    pattern = re.compile(matchText,re.S)
        datas = re.findall(pattern,page)
        return datas
    
    
    
    
    
    def savePageInfo(self,pageIndex):
        page = self.getPage(pageIndex)
        
        #pattern
        quarters = self.getSingleData(page, '<td class="number">(.*?)</td>')
        season = self.getSingleData(page, '<meta name="description" content="(.*?)赛季,')
        date = self.getSingleData(page, '<div style="float: left;margin-top: 25px;margin-left: 10px;font-size: 16px;font-weight: bold;color: #009CFF">.*?-(.*?) <font style')
        team = self.getSingleData(page, '<div><a style="font-size:14px;" href="/team/(.*?).html')
        player_num = self.getSingleData(page, '<td colspan="2" class ="player_id">(.*?)人</td>')
        match_type = self.getSingleData(page, '<div class="title" style=margin-top:10px;>(.|\n).*?(.|\n).*?.*?赛季(.*?)(.|\n)</div>')
        
        # regular = [('\r', '\n', '\t\t\t\t\t\t14-15\xe8\xb5\x9b\xe5\xad\xa3\r\n\t\t\t\t\t\t\xe5\xad\xa3\xe5\x90\x8e\xe8\xb5\x9b\r\n\t\t\t\t', '\t')]
        
        regular = [('\r', '\n', '\r\n\t\t\t\t\t\t\xe5\xb8\xb8\xe8\xa7\x84\xe8\xb5\x9b\r\n\t\t\t\t', '\t')]
        if match_type == regular:
            match_kind = "regular"
        else:
            match_kind = "playoff"
        
        
        
        """                    <div class="title" style=margin-top:10px;>
            14-15赛季
            常规赛
            </div>
            """
        
        
        playername = self.getSingleData(page, '<td class ="normal player_name_out change_color col0 row.*?"><a href="/player/.*?" target="_blank">(.*?)</a></td>')
        data1 = self.getSingleData(page, '<td class ="current gs change_color col1 row.*?" rank=".*?">(.*?)</td>')
        data2 = self.getSingleData(page, '<td class ="normal mp change_color col2 row.*?" rank=".*?">(.*?)</td>')
        data3 = self.getSingleData(page, '<td class ="normal fgper change_color col3 row.*?" rank=".*?">(.*?)</td>')
        data4 = self.getSingleData(page, '<td class ="normal fg change_color col4 row.*?" rank=".*?">(.*?)</td>')
        data5 = self.getSingleData(page, '<td class ="normal fga change_color col5 row.*?" rank=".*?">(.*?)</td>')
        data6 = self.getSingleData(page, '<td class ="normal threepper change_color col6 row.*?" rank=".*?">(.*?)</td>')
        data7 = self.getSingleData(page, '<td class ="normal threep change_color col7 row.*?" rank=".*?">(.*?)</td>')
        data8 = self.getSingleData(page, '<td class ="normal threepa change_color col8 row.*?" rank=".*?">(.*?)</td>')
        data9 = self.getSingleData(page, '<td class ="normal ftper change_color col9 row.*?" rank=".*?">(.*?)</td>')
        data10 = self.getSingleData(page, '<td class ="normal ft change_color col10 row.*?" rank=".*?">(.*?)</td>')
        data11 = self.getSingleData(page, '<td class ="normal fta change_color col11 row.*?" rank=".*?">(.*?)</td>')
        data12 = self.getSingleData(page, '<td class ="normal ts change_color col12 row.*?" rank=".*?">(.*?)</td>')
        data13 = self.getSingleData(page, '<td class ="normal trb change_color col13 row.*?" rank=".*?">(.*?)</td>')
        data14 = self.getSingleData(page, '<td class ="normal orb change_color col14 row.*?" rank=".*?">(.*?)</td>')
        data15 = self.getSingleData(page, '<td class ="normal drb change_color col15 row.*?" rank=".*?">(.*?)</td>')
        data16 = self.getSingleData(page, '<td class ="normal ast change_color col16 row.*?" rank=".*?">(.*?)</td>')
        data17 = self.getSingleData(page, '<td class ="normal stl change_color col17 row.*?" rank=".*?">(.*?)</td>')
        data18 = self.getSingleData(page, '<td class ="normal blk change_color col18 row.*?" rank=".*?">(.*?)</td>')
        data19 = self.getSingleData(page, '<td class ="normal tov change_color col19 row.*?" rank=".*?">(.*?)</td>')
        data20 =self.getSingleData(page, '<td class ="normal pf change_color col20 row.*?" rank=".*?">(.*?)</td>')
        data21 = self.getSingleData(page, '<td class ="normal pts change_color col21 row.*?" rank=".*?">(.*?)</td>')
        
        if player_num == []:
            print "wrong!!!"
        
        
        team0_num = int(player_num[0])
        
        team1_num = int(player_num[1])
        
        
        
        
        #print (team[1])
        #print (season[0])
        #print (quarters)
        team_0_score = int(quarters[0])+int(quarters[1])+int(quarters[2])+int(quarters[3])
        team_1_score = int(quarters[4])+int(quarters[5])+int(quarters[6])+int(quarters[7])
        
        
        fileName = 'match' + "/" + season[0] + "_" + date[0] + "_" + team[0] + "-" + team[1] + "_" + match_kind
        
        f = open(fileName,"a")
        f.write(date[0]+";"+team[0] + "-" + team[1]+";"+str(team_0_score)+"-"+str(team_1_score)+";"+"\n")
        f.write(quarters[0]+"-"+quarters[4]+";"+quarters[1]+"-"+quarters[5]+";"+quarters[2]+"-"+quarters[6]+";"+quarters[3]+"-"+quarters[7]+";"+"\n")
        f.write(team[0]+"\n")
        n1=0
        while n1<team0_num:
            f.write(playername[n1]+";"+data1[n1]+";"+data2[n1]+";"+data3[n1]+";"+data4[n1]+";"+data5[n1]+";"+data6[n1]+";"+data7[n1]+";"+data8[n1]+";"+data9[n1]+";"+data10[n1]+";"+data11[n1]+";"+data12[n1]+";"+data13[n1]+";"+data14[n1]+";"+data15[n1]+";"+data16[n1]+";"+data17[n1]+";"+data18[n1]+";"+data19[n1]+";"+data20[n1]+";"+data21[n1]+";"+"\n")
            n1=n1+1
        f.write(team[1]+"\n")
        n2=0
        while n2<team1_num:
            f.write(playername[team0_num+n2]+";"+data1[team0_num+n2]+";"+data2[team0_num+n2]+";"+data3[team0_num+n2]+";"+data4[team0_num+n2]+";"+data5[team0_num+n2]+";"+data6[team0_num+n2]+";"+data7[team0_num+n2]+";"+data8[team0_num+n2]+";"+data9[team0_num+n2]+";"+data10[team0_num+n2]+";"+data11[team0_num+n2]+";"+data12[team0_num+n2]+";"+data13[team0_num+n2]+";"+data14[team0_num+n2]+";"+data15[team0_num+n2]+";"+data16[team0_num+n2]+";"+data17[team0_num+n2]+";"+data18[team0_num+n2]+";"+data19[team0_num+n2]+";"+data20[team0_num+n2]+";"+data21[team0_num+n2]+";"+"\n")
            n2=n2+1
        
        f.close()
        
                print "成功输出"+season[0] + "_" + date[0] + "_" + team[0] + "-" + team[1] + "_" + match_kind+ "_"+ str(pageIndex) +"的比赛数据"

#self.savDetailData(page, fileName)
def checkExist(self,pageIndex):
    page = self.getPage(pageIndex)
        player_num = self.getSingleData(page, '<td colspan="2" class ="player_id">(.*?)人</td>')
        if player_num == []:
            return 0
    else:
        return 1

def savePagesInfo(self,start,end):
    for i in range(start,end+1):
        if self.checkExist(i)==0:
            continue
            else:
                self.savePageInfo(i)


spider = Spider()
spider.savePagesInfo(575,27449)