import pandas as pd
import numpy as np
import pymysql

class DBconn():
    def __init__(self):
        self.host="database-1"
        self.port=3306
        self.user=""
        self.passwd=""
        self.db=""
        
        self.conn  = pymysql.connect(host=self.host, port=self.port,
                     user=self.user,passwd=self.passwd,  
                     db=self.db) 
        self.cursor = self.conn.cursor()    
        self.conn.set_charset('utf8')
        
    def selectDB(self,tb):
        sql = "Select * FROM " +tb
        self.cursor.execute(sql)
        columns = [i[0] for i in self.cursor.description]
        df = pd.DataFrame(self.cursor.fetchall(),columns=columns)
        return df
      
dbcon = DBconn()
df_video_cate = dbcon.selectDB('YT_video_category_class')
df_video_lists = dbcon.selectDB('YT_video_lists')
df_channel = dbcon.selectDB('youtuber_info')
