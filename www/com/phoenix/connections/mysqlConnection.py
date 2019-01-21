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

        cur.close()
        conn.close()

    def fetch(self, sql):
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
        rows=self.fetch(sql)

        return rows
    
    def showDatabases(self):
        arr = []
        sql = 'show databases'
        rows = self.fetch(sql)
        for row in rows:
            arr.append(dict(name=row[0], comment=""))
        
        return arr

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

    def analyse(self,db,tables):
        arr = []
        filter = ""
        if tables and len(tables) > 0:
            if isinstance(tables, list):
                filter = "AND t.TBL_NAME IN ('" + "','".join(tables) + "')"
            else:
                filter = "AND t.TBL_NAME IN ('" + tables + "')"

        sql = ("SELECT DB_NAME, TABLE_NAME, " 
                "sum(case when PARAM_KEY='numFiles' then PARAM_VALUE else 0 end) NUMFILES, " 
                "sum(case when PARAM_KEY='numRows' then PARAM_VALUE else 0 end) NUMROWS, " 
                "sum(case when PARAM_KEY='totalSize' then PARAM_VALUE else 0 end) TOTALSIZE " 
            "FROM ( " 
                "SELECT t.TBL_NAME as TABLE_NAME, t.TBL_TYPE, t.DB_ID, d.NAME as DB_NAME, " 
                        "p.PART_NAME,pp.* " 
                "FROM PARTITION_PARAMS pp " 
                        "LEFT OUTER JOIN PARTITIONS p ON pp.PART_ID=p.PART_ID " 
                        "LEFT OUTER JOIN TBLS t ON t.TBL_ID=p.TBL_ID " 
                        "LEFT OUTER JOIN DBS d ON t.DB_ID=d.DB_ID " 
                "WHERE d.NAME='" + db + "' " 
                        "" + filter + " "
                        "AND pp.PARAM_KEY IN ('numRows','numFiles', 'totalSize') " 
            ") aa " 
            "GROUP BY DB_NAME, TABLE_NAME ")
        rows = self.fetch(sql)        
        for row in rows:
            db_name = row[0]
            table_name = row[1]
            num_files = row[2]
            num_rows = row[3]
            total_size = row[4]
            arr.append(dict(db_name=db_name, table_name=table_name, num_files=num_files, num_rows=num_rows, total_size=total_size))

        return arr

    def analysePartition(self,db,table):
        arr = []

        sql = ("SELECT DB_NAME, TABLE_NAME, PART_NAME, " 
                "sum(case when PARAM_KEY='numFiles' then PARAM_VALUE else 0 end) NUMFILES, " 
                "sum(case when PARAM_KEY='numRows' then PARAM_VALUE else 0 end) NUMROWS, " 
                "sum(case when PARAM_KEY='totalSize' then PARAM_VALUE else 0 end) TOTALSIZE " 
            "FROM ( " 
                "SELECT t.TBL_NAME as TABLE_NAME, t.TBL_TYPE, t.DB_ID, d.NAME as DB_NAME, " 
                        "REPLACE(p.PART_NAME,  'etl_dt=','') AS PART_NAME, "
                        "pp.* " 
                "FROM PARTITION_PARAMS pp " 
                        "LEFT OUTER JOIN PARTITIONS p ON pp.PART_ID=p.PART_ID " 
                        "LEFT OUTER JOIN TBLS t ON t.TBL_ID=p.TBL_ID " 
                        "LEFT OUTER JOIN DBS d ON t.DB_ID=d.DB_ID " 
                "WHERE d.NAME='" + db + "' " 
                        "AND t.TBL_NAME IN ('" + table + "') "
                        "AND pp.PARAM_KEY IN ('numRows','numFiles', 'totalSize') " 
            ") aa " 
            "GROUP BY DB_NAME, TABLE_NAME, PART_NAME "
            "ORDER BY PART_NAME")
        rows = self.fetch(sql)        
        for row in rows:
            db_name = row[0]
            table_name = row[1]
            partition_name = row[2]
            num_files = row[3]
            num_rows = row[4]
            total_size = row[5]
            arr.append(dict(db_name=db_name, table_name=table_name, partition_name = partition_name, num_files=num_files, num_rows=num_rows, total_size=total_size))

        return arr

if __name__ == '__main__':
    print('作为主程序运行')
else:
    print('MysqlConnection 初始化')
