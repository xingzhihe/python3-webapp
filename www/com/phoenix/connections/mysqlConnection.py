#coding:utf-8
#!/usr/bin/python 
import os, sys
import pymysql

class MysqlConnection(object):
    def __init__(self, ds):
        self.ds = ds
    
    def execute(self, sql):
        if self.ds.database :
            conn = pymysql.connect(host=self.ds.host, user=self.ds.user, passwd=self.ds.password, db=self.ds.database, port=self.ds.port, charset='utf8')
        else:
            conn = pymysql.connect(host=self.ds.host, user=self.ds.user, passwd=self.ds.password, port=self.ds.port, charset='utf8')
        cur = conn.cursor()
        cur.execute(sql)
        rows=cur.fetchall()

        cur.close()
        conn.close()

        return rows

    def query(self, sql):
        rows=self.execute(sql)

        return rows
    
    def showDatabases(self):
        arr = []
        sql = 'show databases'
        rows = self.execute(sql)
        for row in rows:
            arr.append(dict(name=row[0], comment=""))
        
        return arr

    '''
    SELECT * FROM TBLS WHERE TBL_ID=204386;
    SELECT * FROM SDS WHERE SD_ID=315526;
    SELECT * FROM COLUMNS_V2 WHERE CD_ID=204888 ORDER BY INTEGER_IDX;
    '''  
    def showTables(self):
        arr = []
        sql = 'show tables'
        rows = self.execute(sql)        
        for row in rows:
            msg = row[0]
            arr.append(dict(name=msg))

        return arr

if __name__ == '__main__':
    print('作为主程序运行')
else:
    print('MysqlConnection 初始化')
