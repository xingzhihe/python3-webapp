#coding:utf-8
#!/usr/bin/python 
import os, sys
from impala.dbapi import connect
import pymysql.cursors

def query():
    conn = connect(host='10.10.8.102', port=21050)
    cur = conn.cursor()
    sql = 'select zsxm_dm,zsxmmc,zsxmjc,xybz,yxbz,sjzsxm_dm,yxqz,yxqq from odm_db.o_hx_qg_dm_gy_zsxm'
    cur.execute(sql)
    rows=cur.fetchall()

    for row in rows:
        print("zsxm_dm:%s, zsxmmc:%s, zsxmjc:%s, xybz:%s, yxbz:%s, sjzsxm_dm:%s, yxqz:%s, yxqq:%s" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

    cur.close()
    conn.close()

'''
SELECT * FROM TBLS WHERE TBL_ID=204386;
SELECT * FROM SDS WHERE SD_ID=315526;
SELECT * FROM COLUMNS_V2 WHERE CD_ID=204888 ORDER BY INTEGER_IDX;
'''
def showDatabases():
    conn = connect(host='10.10.8.102', port=21050)
    cur = conn.cursor()
    sql = 'show databases'
    #sql = 'show create table f_fp_nsr_yue'
    cur.execute(sql)
    rows=cur.fetchall()
    
    arr = []
    for row in rows:
        msg = row[0]
        arr.append(dict(name=msg))
    
    cur.close()
    conn.close()

    return arr
def showTables():
    conn = connect(host='10.10.8.102', database='fdm_db', port=21050)
    cur = conn.cursor()
    sql = 'show tables'
    #sql = 'show create table f_fp_nsr_yue'
    cur.execute(sql)
    rows=cur.fetchall()
    
    arr = []
    for row in rows:
        msg = row[0]
        arr.append(dict(name=msg))
    
    cur.close()
    conn.close()

    return arr


if __name__ == '__main__':
    query()
    #syncImpalaDB()

    #showTables()
