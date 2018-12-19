﻿#coding:utf-8
#!/usr/bin/python 
import os, sys

def get_Connection(ds):
    if ds.db_type == "Impala" :
        from impalaConnection  import ImpalaConnection
        conn = ImpalaConnection(ds)
    else:
        from com.phoenix.connections.mysqlConnection import MysqlConnection
        conn = MysqlConnection(ds)

    return conn

if __name__ == '__main__':
    print('作为主程序运行')
else:
    print('connectionFactory 初始化')
