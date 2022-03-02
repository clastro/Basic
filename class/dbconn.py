class DBconn():
    
    def __init__(self):
        self.db = "smc_metadata_v05.db"
        self.conn = sqlite3.connect(self.db)
        self.cursor = self.conn.cursor()
    
    def ShowTables(self):
        sql = "SELECT name FROM sqlite_master WHERE type='table';"
        self.cursor.execute(sql)
        print([i[0] for i in self.cursor.fetchall()])
        
    def selectTableData(self,table_name):
        sql = "SELECT * FROM " + table_name
        self.cursor.execute(sql)
        columns = [col[0] for col in self.cursor.description]
        df = pd.DataFrame(self.cursor.fetchall(),columns=columns)
        return df
