#coding:utf-8
#!/usr/bin/python 
import os, sys
import cx_Oracle

class OracleConnection(object):
    def __init__(self, ds):
        self.ds = ds
    
    def execute(self, sql):
        conn = cx_Oracle.connect("%s/%s@%s:%s/%s" % (self.ds.user, self.ds.password, self.ds.host, self.ds.port, self.ds.database))
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
        sql = 'select name from v$database order by name'
        rows = self.execute(sql)
        for row in rows:
            arr.append(dict(name=row[0], comment=""))
        
        return arr

    def showUsers(self):
        arr = []
        sql = 'select username from all_users order by username'
        rows = self.execute(sql)        
        for row in rows:
            userName = row[0]
            arr.append(dict(name=userName))

        return arr

    def showTables(self, userName):
        arr = []
        sql = "select table_name from all_tables where owner='%s' order by table_name" % userName
        rows = self.execute(sql)        
        for row in rows:
            msg = row[0]
            arr.append(dict(name=msg))

        return arr

    def showFields(self,table):
        arr = []
        paras = table.split('.')
        sql = "select column_name, data_type from all_tab_columns where owner='%s' and table_name='%s' order by column_id" % (paras[0],paras[1])
        rows = self.execute(sql)        
        for row in rows:
            name = row[0]
            data_type = row[1]
            arr.append(dict(name=name, data_type=data_type))

        return arr

if __name__ == '__main__':
    print('作为主程序运行')
else:
    print('OracleConnection 初始化')
