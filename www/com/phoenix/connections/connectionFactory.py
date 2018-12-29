#coding:utf-8
#!/usr/bin/python 
import os, sys

def get_Connection(ds):
    if ds.db_type == "Oracle" :
        from com.phoenix.connections.oracleConnection  import OracleConnection
        conn = OracleConnection(ds)
    elif ds.db_type == "Impala" :
        from com.phoenix.connections.impalaConnection  import ImpalaConnection
        conn = ImpalaConnection(ds)
    else:
        from com.phoenix.connections.mysqlConnection import MysqlConnection
        conn = MysqlConnection(ds)

    return conn

if __name__ == '__main__':
    print('作为主程序运行')
else:
    print('connectionFactory 初始化')
