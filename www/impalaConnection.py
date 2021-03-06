﻿#coding:utf-8
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
        rows=cur.fetchall()

        cur.close()
        conn.close()

        return rows

    def query(self, sql):
        conn = connect(host=self.ds.host, database=self.ds.database, port=self.ds.port)
        cur = conn.cursor()
        cur.execute(sql)
        rows=cur.fetchall()

        cur.close()
        conn.close()

        return rows
    
    def showDatabases(self):
        arr = []
        sql = 'show databases'
        rows = self.query(sql)
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
        rows = self.query(sql)        
        for row in rows:
            msg = row[0]
            arr.append(dict(name=msg))

        return arr

if __name__ == '__main__':
    
    from ..models import DataSource
    ds = DataSource(db_type="Impala", host="10.10.8.102", database="fdm_db", port=21050)
    conn = ImpalaConnection(ds)
    sql = 'select zsxm_dm,zsxmmc,zsxmjc,xybz,yxbz,sjzsxm_dm,yxqz,yxqq from odm_db.o_hx_qg_dm_gy_zsxm'
    rows=conn.query(sql)
    for row in rows:
        print("zsxm_dm:%s, zsxmmc:%s, zsxmjc:%s, xybz:%s, yxbz:%s, sjzsxm_dm:%s, yxqz:%s, yxqq:%s" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

    #syncImpalaDB()

    #showTables()
