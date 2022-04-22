import sqlite3
import pandas as pd

class DBconn():
    
    def __init__(self):
        #self.db = "/smc_work/data/smc_metadata_v06.db"
        self.db = "/smc_work/datanvme/smc/meta/smc_metadata_v07_2.db"
        self.conn = sqlite3.connect(self.db)
        self.cursor = self.conn.cursor()
    
    def ShowTables(self):
        sql = "SELECT name FROM sqlite_master WHERE type='table';"
        self.cursor.execute(sql)
        tables = [i[0] for i in self.cursor.fetchall()]
        return tables
        
    def selectTableData(self,table_name):
        sql = "SELECT * FROM " + table_name
        self.cursor.execute(sql)
        columns = [col[0] for col in self.cursor.description]
        df = pd.DataFrame(self.cursor.fetchall(),columns=columns)
        return df
    
    def DropTable(self,table_name):
        sql = "DROP TABLE '{}'".format(table_name)
        self.cursor.execute(sql)
    
if __name__ == '__main__':
    main()
