#coding:utf-8
# Embedded file name: /home/etlusr/etljob/lib/ImpalaTet.py
#!/usr/bin/python 
import os, sys
from impala.dbapi import connect
import pymysql.cursors

user_home = os.path.expanduser('~')
etl_home = os.environ['ETL_HOME']

def queryImpala():
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
def showTables():
    conn = connect(host='10.10.8.102', database='fdm_db', port=21050)
    cur = conn.cursor()
    sql = 'show tables'
    #sql = 'show create table f_fp_nsr_yue'
    cur.execute(sql)
    rows=cur.fetchall()
    
    log_file=os.path.join('.','qsc_hive.sql')
    output_log = open(log_file,'w')

    count = 1
    arr = []
    for row in rows:
        msg = row[0]
        if(msg[:8] =='f_fp_xf_' or msg[:8] =='f_fp_kh_' or msg[:9] =='f_fp_nsr_' or msg[:9] =='f_fp_khs_' or msg[:10] =='f_fp_fphj_'):
            print("\n-- %03d: %s\n" % (count, msg))
            output_log.write('\n-- %03d: %s\n' % (count, msg))
            arr.append(msg)
            count += 1
            
            sql = 'show create table %s' % msg
            #sql = 'describe %s' % msg
            cur.execute(sql)
            rows=cur.fetchall()
            for row in rows:
                printGBK(row[0])
                output_log.write(row[0])
                #printGBK('\t%s \t%s \t%s' % (row[0], row[1], row[2]))
    
    output_log.close()

    cur.close()
    conn.close()


def syncImpalaDB():
    conn = connect(host='10.10.8.102', port=21050)
    cur = conn.cursor()
    sql = 'select zsxm_dm,zsxmmc,zsxmjc,xybz,yxbz,sjzsxm_dm,yxqz,yxqq from odm_db.o_hx_qg_dm_gy_zsxm'
    cur.execute(sql)
    rows=cur.fetchall()

    # 打开mysql链接
    conn_mysql = pymysql.connect(host="10.10.8.104", user="root", passwd="", db="fdm_db", port=4000, charset='utf8')
    cur_mysql = conn_mysql.cursor()

    for row in rows:
        print("zsxm_dm:%s, zsxmmc:%s, zsxmjc:%s, xybz:%s, yxbz:%s, sjzsxm_dm:%s, yxqz:%s, yxqq:%s" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        cur_mysql.execute("insert into f_fp_qsc_zsxm (zsxm_dm,zsxmmc,zsxmjc,xybz,yxbz,sjzsxm_dm) values('%s','%s','%s','%s','%s','%s')" % (row[0],row[1],row[2],row[3],row[4],row[5]))

    cur.close()
    conn.close()

    cur_mysql.close()
    conn_mysql.commit()
    conn_mysql.close()

if __name__ == '__main__':
    print("hello welcome to my first python app!!!")
    print("var of ETL_HOME :" + etl_home)

    queryImpala()
    #syncImpalaDB()

    #showTables()
