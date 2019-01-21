#coding:utf-8
#!/usr/bin/python 
import os, sys
from impala.dbapi import connect
import pymysql.cursors

class ImpalaConnection(object):
    def __init__(self, ds):
        self.ds = ds
    
    def execute(self, sql):
        if self.ds.database :
            conn = connect(host=self.ds.host, database=self.ds.database, port=self.ds.port)
        else:
            conn = connect(host=self.ds.host, port=self.ds.port)
        cur = conn.cursor()
        cur.execute(sql)

        cur.close()
        conn.close()
    
    def fetch(self, sql):
        if self.ds.database :
            conn = connect(host=self.ds.host, database=self.ds.database, port=self.ds.port)
        else:
            conn = connect(host=self.ds.host, port=self.ds.port)
        cur = conn.cursor()
        cur.execute(sql)
        rows=cur.fetchall()

        cur.close()
        conn.close()

        return rows

    def query(self, sql):
        rows=self.fetch(sql)

        return rows
    
    def showDatabases(self):
        arr = []
        sql = 'show databases'
        rows = self.fetch(sql)
        for row in rows:
            arr.append(dict(name=row[0], comment=row[1]))
        
        return arr

    '''
    SELECT * FROM TBLS WHERE TBL_ID=204386;
    SELECT * FROM SDS WHERE SD_ID=315526;
    SELECT * FROM COLUMNS_V2 WHERE CD_ID=204888 ORDER BY INTEGER_IDX;
    '''  
    def showTables(self):
        arr = []
        sql = 'show tables'
        rows = self.fetch(sql)        
        for row in rows:
            msg = row[0]
            arr.append(dict(name=msg))

        return arr

    def showFields(self,table):
        arr = []
        sql = "describe %s" % table
        rows = self.fetch(sql)        
        for row in rows:
            name = row[0]
            data_type = row[1]
            arr.append(dict(name=name, data_type=data_type))

        return arr
    
    def computeStats(self, db, table):
        sql = "compute stats  %s.%s" % (db,table)
        self.execute(sql)

if __name__ == '__main__':
    print('作为主程序运行')
else:
    print('ImpalaConnection 初始化')
