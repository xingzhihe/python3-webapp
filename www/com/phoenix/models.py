#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'zhihe xing'

import time

from com.phoenix.orm import Model, StringField, BooleanField, FloatField, TextField, IntegerField
from com.phoenix.common import next_id

class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time)

class Blog(Model):
    __table__ = 'blogs'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)

class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)

class DataSource(Model):
    __table__ = 'datasources'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    db_type = StringField(ddl='varchar(10)')
    host = StringField(ddl='varchar(50)')
    port = IntegerField(ddl='int')
    database = StringField(ddl='varchar(50)')
    user = StringField(ddl='varchar(50)')
    password = StringField(ddl='varchar(50)')
    options = StringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time)

    def get_Connection_String(self):
        return '%s://%s:%d/%s' % (self.db_type, self.host, self.port, self.database)
    
    def show_Tables(self):
        connString = '%s://%s:%d/%s' % (self.db_type, self.host, self.port, self.database)
        return connString
    
    def get_Connection(self):
        connString = '%s://%s:%d/%s' % (self.db_type, self.host, self.port, self.database)
        return connString
    
    def get_MetadataSource(self):
        if self.db_type == 'Impala' :
            ds = DataSource(db_type="MySQL", host="10.10.8.102", database="hive_db", port=3306, user="etlusr", password="etlusr")
        else:
            ds = self
        return ds

if __name__ == '__main__':
    ds=DataSource(db_type='mysql', host='127.0.0.1', port=3306, database='awesome', user='etlusr', password='etlusr')
    print(ds.get_Connection_String())
    print('作为主程序运行')
else:
    print('models 初始化')